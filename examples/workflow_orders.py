#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rational-client",
# ]
# ///
import json
import sqlite3
import tempfile

from rational_client.core import (
    File,
    Knowledge,
    SyncedResource,
)
from rational_client.utils import run


def process(document: SyncedResource, options: dict):
    # Parse the JSON data from the resource
    content = document.get_data()
    orders = json.loads(content)

    # Dictionary to keep track of user resources
    user_resources = {}
    product_resources = {}

    # Create a temp SQLite database file
    with tempfile.NamedTemporaryFile(suffix=".db") as db_file:
        db_path = db_file.name

        # Create the schema
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()

            # Create orders table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                customer_email TEXT COLLATE NOCASE,
                customer_name TEXT COLLATE NOCASE,
                status TEXT COLLATE NOCASE,
                currency TEXT COLLATE NOCASE,
                payment_method TEXT COLLATE NOCASE,
                payment_method_title TEXT COLLATE NOCASE,
                date_created TEXT COLLATE NOCASE,
                date_paid TEXT COLLATE NOCASE,
                date_completed TEXT COLLATE NOCASE,
                total REAL,
                subtotal REAL,
                tax_total REAL,
                shipping_total REAL,
                discount_total REAL,
                shipping_country TEXT COLLATE NOCASE,
                shipping_city TEXT COLLATE NOCASE,
                resource_id TEXT
            )
            """)

            # Create order_items table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                order_id INTEGER,
                sku STRING,
                quantity INTEGER,
                price REAL,
                total REAL,
                FOREIGN KEY(order_id) REFERENCES orders(id)
            )
            """)

            knowledge = Knowledge(document.knowledge_id)

            # Insert orders into the database
            for order in orders:
                # Extract shipping_country and shipping_city from nested shipping dict
                shipping = order.get("shipping", {})
                order["shipping_country"] = shipping.get("country", "Unknown Country")
                order["shipping_city"] = shipping.get("city", "Unknown City")

                # Use shipping country and city as tags, and country as category
                shipping_country = order.get("shipping_country", "Unknown Country")
                shipping_city = order.get("shipping_city", "Unknown City")
                order_tags = []
                if order.get("status"):
                    order_tags.append(order["status"])
                if shipping_country:
                    order_tags.append(shipping_country)
                if shipping_city:
                    order_tags.append(shipping_city)
                order_resource = knowledge.create_resource(
                    name=f"Order #{order.get('id')}",
                    category=shipping_country,
                    notes=f"Total: {order.get('total', 0)}, Status: {order.get('status', '')}",
                    tags=order_tags,
                    synced_resource_id=document.id,
                )
                order_resource_id = order_resource.resource_id

                cur.execute(
                    """
                    INSERT OR IGNORE INTO orders (
                        id, customer_id, customer_email, customer_name, status, currency,
                        payment_method, payment_method_title, date_created, date_paid,
                        date_completed, total, subtotal, tax_total, shipping_total, discount_total,
                        shipping_country, shipping_city, resource_id
                    ) VALUES (
                        :id, :customer_id, :customer_email, :customer_name, :status, :currency,
                        :payment_method, :payment_method_title, :date_created, :date_paid,
                        :date_completed, :total, :subtotal, :tax_total, :shipping_total, :discount_total,
                        :shipping_country, :shipping_city, :resource_id
                    )
                    """,
                    {**order, "resource_id": str(order_resource_id)},
                )

                # Create rational resource for the user if not already created
                customer_name = order.get("customer_name", "Unknown User")
                if customer_name not in user_resources:
                    user_resource = knowledge.create_resource(
                        name=customer_name,
                        category="User",
                        notes=f"Email: {order.get('customer_email', '')}",
                        tags=["user"],
                        synced_resource_id=document.id,
                    )
                    user_resources[customer_name] = user_resource
                else:
                    user_resource = user_resources[customer_name]

                # Connect order to user
                order_resource.add_relation(user_resource, type="user")

                for item in order.get("items", []):
                    cur.execute(
                        """
                    INSERT INTO order_items (
                        order_id, sku, quantity, price, total
                    ) VALUES (
                        :order_id, :sku, :quantity, :price, :total
                    )
                    """,
                        {
                            "order_id": order.get("id"),
                            "sku": item.get("sku"),
                            "quantity": item.get("quantity"),
                            "price": item.get("price"),
                            "total": item.get("total"),
                        },
                    )

                    # Create rational resource for the product if not already created
                    item_sku = item.get("sku", None)
                    if item_sku and item_sku not in product_resources:
                        product_resource = knowledge.create_resource(
                            name=item_sku,
                            category="Products",
                            notes=f"Price: {item.get('price', 0)}",
                            tags=["products"],
                            synced_resource_id=document.id,
                        )
                        product_resources[item_sku] = product_resource
                    else:
                        product_resource = product_resources[item_sku]
                    order_resource.add_relation(product_resource, type="item")

            conn.commit()

        # Create a SyncedResource for the SQLite database
        with open(db_path, "rb") as f:
            _ = knowledge.upload_synced_resource(
                name="orders.db",
                contents=File(f, file_name="orders.db", mime_type="application/x-sqlite3"),
                parent_id=document.id,
            )


run(process)
