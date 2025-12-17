#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "psycopg2-binary",
#     "rational-client",
# ]
# ///
import json
import logging
import os
from datetime import datetime
from uuid import UUID

import psycopg2
import psycopg2.extras

from rational_client.core import AnnotationType, Knowledge, SyncedResource

# Global DB connection variables (read from environment)
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "secret-password")
DB_NAME = os.environ.get("DB_NAME", "pengo")

PRODUCTS_TABLE = "products"


def _ensure_table(conn):
    """Create products table if it doesn't exist with a schema compatible with Pengo product JSON."""
    with conn.cursor() as cur:
        cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {PRODUCTS_TABLE} (
                document_id TEXT PRIMARY KEY,
                sku TEXT,
                name TEXT,
                description TEXT,
                price NUMERIC,
                sale_price NUMERIC,
                stock_count INTEGER,
                unlimited BOOLEAN,
                low_stock_alert BOOLEAN,
                category TEXT,
                parent_category TEXT,
                brand TEXT,
                line TEXT,
                product_size JSONB,
                packing_size JSONB,
                tags TEXT[],
                mpn TEXT,
                state TEXT,
                min_quantity INTEGER,
                inc_quantity INTEGER,
                max_quantity INTEGER,
                tax_percentage INTEGER,
                total_sales INTEGER,
                created_at TIMESTAMP WITH TIME ZONE,
                updated_at TIMESTAMP WITH TIME ZONE,
                published_at TIMESTAMP WITH TIME ZONE,
                resource_id TEXT
            );
            """
        )
        # ensure unique mapping between a knowledge resource and a product row
        cur.execute(
            f"CREATE UNIQUE INDEX IF NOT EXISTS idx_{PRODUCTS_TABLE}_resource_id ON {PRODUCTS_TABLE}(resource_id);"
        )


def _connect_db():
    base_params = dict(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    # include dbname explicitly in params passed to psycopg2.connect to avoid typing confusion
    params = {**base_params, "dbname": DB_NAME}

    try:
        # try connecting to the requested database
        conn = psycopg2.connect(**params)
    except psycopg2.OperationalError as e:
        msg = str(e)
        # if database does not exist, attempt to create it by connecting to the default 'postgres' DB
        if "does not exist" in msg.lower():
            tmp_params = {**base_params, "dbname": "postgres"}
            tmp_conn = psycopg2.connect(**tmp_params)
            try:
                from psycopg2 import sql
                from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

                tmp_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                with tmp_conn.cursor() as cur:
                    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            finally:
                tmp_conn.close()
            # reconnect to the newly created database
            conn = psycopg2.connect(**params)
        else:
            # propagate other connection errors
            raise

    # ensure products table exists
    _ensure_table(conn)

    # Use json adapter for convenience
    psycopg2.extras.register_default_jsonb(conn, loads=lambda s: json.loads(s))

    return conn


def _parse_ts(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except Exception:
        return None


def dict_to_markdown_description_list(data_dict: dict) -> str:
    """
    Converts a Python dictionary into a Markdown description list (GFM syntax).

    Args:
        data_dict: The dictionary where keys are terms and values are descriptions.

    Returns:
        A string formatted as a Markdown description list.
    """
    markdown_list = []
    for term, description in data_dict.items():
        if term == "id":
            continue
        # Ensure description is a string, especially if it was a number or list
        description_str = str(description).replace("\n", " ")

        # Append the term (key)
        markdown_list.append(f"{term}")

        # Append the definition (value), starting with a colon and space
        markdown_list.append(f": {description_str}")

        # Add an extra newline for separation (improves readability in the raw markdown)
        markdown_list.append("")

    return "\n".join(markdown_list).strip()


def generate_product_summary(
    product, product_resource_name, name, sku, category_name, parent_category_name, brand_name, line, tags
):
    product_size_val = product.get("product_size")
    packing_size_val = product.get("packing_size")

    def _display_val(v):
        if v is None or v == "":
            return "N/A"
        if isinstance(v, dict):
            return dict_to_markdown_description_list(v)
        elif isinstance(v, list):
            return json.dumps(v)
        return str(v)

    price = product.get("price")
    sale_price = product.get("sale_price")
    if price is None and sale_price is None:
        price_display = "N/A"
    elif sale_price not in (None, "") and sale_price != price:
        price_display = f"{sale_price} (was {price})"
    else:
        price_display = str(price)

    stock_count = product.get("stock_count")
    unlimited = product.get("unlimited")
    low_stock_alert = product.get("low_stock_alert")

    if unlimited:
        availability = "Available (unlimited)"
    elif stock_count is None:
        availability = "Unknown"
    elif stock_count > 0:
        availability = f"In stock ({stock_count})"
    else:
        availability = "Out of stock"

    if low_stock_alert:
        availability += " — Low stock alert"

    # Format tags into markdown list
    md_tags = "\n - ".join(tags) if tags else "N/A"

    markdown = f"## Product {product_resource_name}\n\n"
    markdown += f"**SKU:** {sku or 'N/A'}\n\n"
    markdown += f"**Name:** {name or 'N/A'}\n\n"
    markdown += f"**Description:** {product.get('description') or 'N/A'}\n\n"
    markdown += f"**Category:** {category_name or 'Uncategorized'}\n\n"
    markdown += f"**Parent category:** {parent_category_name or 'N/A'}\n\n"
    markdown += f"**Brand:** {brand_name or 'N/A'}\n\n"
    markdown += f"**Line:** {line or 'N/A'}\n\n"
    markdown += f"**Tags:** \n{md_tags}\n\n"
    markdown += f"**Price:** {price_display}\n\n"
    markdown += f"**Product size:** {_display_val(product_size_val)}\n\n"
    markdown += f"**Packing size:** {_display_val(packing_size_val)}\n\n"
    markdown += f"**Total sales:** {product.get('total_sales', 0)}\n\n"
    markdown += f"**Stock / Availability:** {availability}\n"

    return markdown


def delete_pengo_product(product: dict, document: SyncedResource) -> dict[str, str]:
    # Extract documentId and product name
    document_id = product.get("documentId", "unknown-documentId")

    # Remove DB row and try to fetch stored resource_id
    found_resource_id = None

    with _connect_db() as conn, conn.cursor() as cur:
        cur.execute(
            f"""
                DELETE FROM {PRODUCTS_TABLE}
                WHERE (document_id = %(document_id)s)
                RETURNING resource_id
                """,
            {"document_id": document_id},
        )
        deleted_row = cur.fetchone()
        found_resource_id = str(deleted_row[0]) if (deleted_row and deleted_row[0] is not None) else None

    # If DB gave us resource_id, delete it from the Knowledge
    if found_resource_id:
        knowledge = Knowledge(document.knowledge_id)
        logging.info(f"Deleting Knowledge resource '{found_resource_id}' for deleted product '{document_id}'")
        knowledge.delete_synced_resource(UUID(found_resource_id))

    return {}


def insert_pengo_product(product: dict, document: SyncedResource) -> dict[str, str]:
    # Setup Knowledge
    knowledge = Knowledge(document.knowledge_id)

    # Build product resource metadata
    sku = product.get("sku", "unknown-sku")
    name = product.get("name", "")
    product_resource_name = f"{sku} - {name}"
    # category may be object, use name if present
    category_obj = product.get("category", {})
    category_name = category_obj.get("name") if isinstance(category_obj, dict) else category_obj
    parent_obj = category_obj.get("parent") if isinstance(category_obj, dict) else None
    parent_category_name = parent_obj.get("name") if isinstance(parent_obj, dict) else parent_obj
    # brand may be object, use name if present
    brand_obj = product.get("brand", {})
    brand_name = brand_obj.get("name") if isinstance(brand_obj, dict) else (brand_obj or "")
    # line from product.line
    line = product.get("line")

    # tags: product['tags'] is list of tag objects; use their names
    raw_tags = product.get("tags", [])
    tags = [str(x) for x in (t.get("name") if isinstance(t, dict) else t for t in raw_tags) if x is not None]

    # Create or get product resource
    product_resource = knowledge.create_resource(
        name=product_resource_name,
        category=category_name or "Uncategorized",
        notes=product.get("description", ""),
        tags=tags,
        synced_resource_id=document.id,
    )
    resource_id = product_resource.id
    synced_resource_id = product_resource.synced_resource.id

    # Insert or upsert product row
    with _connect_db() as conn, conn.cursor() as cur:
        cur.execute(
            f"""
            INSERT INTO {PRODUCTS_TABLE} (
                document_id, sku, name, description, price, sale_price, stock_count,
                unlimited, low_stock_alert, category, parent_category,
                brand, line, product_size, packing_size, tags,
                mpn, state, min_quantity, inc_quantity, max_quantity, tax_percentage,
                total_sales, created_at, updated_at, published_at, resource_id
            ) VALUES (
                %(document_id)s, %(sku)s, %(name)s, %(description)s, %(price)s, %(sale_price)s, %(stock_count)s,
                %(unlimited)s, %(low_stock_alert)s, %(category)s, %(parent_category)s,
                %(brand)s, %(line)s, %(product_size)s, %(packing_size)s, %(tags)s,
                %(mpn)s, %(state)s, %(min_quantity)s, %(inc_quantity)s, %(max_quantity)s, %(tax_percentage)s,
                %(total_sales)s, %(created_at)s, %(updated_at)s, %(published_at)s, %(resource_id)s
            )
            ON CONFLICT (document_id) DO UPDATE SET
                sku = EXCLUDED.sku,
                name = EXCLUDED.name,
                description = EXCLUDED.description,
                price = EXCLUDED.price,
                sale_price = EXCLUDED.sale_price,
                stock_count = EXCLUDED.stock_count,
                unlimited = EXCLUDED.unlimited,
                low_stock_alert = EXCLUDED.low_stock_alert,
                category = EXCLUDED.category,
                parent_category = EXCLUDED.parent_category,
                brand = EXCLUDED.brand,
                line = EXCLUDED.line,
                product_size = EXCLUDED.product_size,
                packing_size = EXCLUDED.packing_size,
                tags = EXCLUDED.tags,
                mpn = EXCLUDED.mpn,
                state = EXCLUDED.state,
                min_quantity = EXCLUDED.min_quantity,
                inc_quantity = EXCLUDED.inc_quantity,
                max_quantity = EXCLUDED.max_quantity,
                tax_percentage = EXCLUDED.tax_percentage,
                total_sales = EXCLUDED.total_sales,
                created_at = EXCLUDED.created_at,
                updated_at = EXCLUDED.updated_at,
                published_at = EXCLUDED.published_at,
                resource_id = EXCLUDED.resource_id
            """,
            {
                "document_id": product.get("documentId"),
                "sku": sku,
                "name": name,
                "description": product.get("description"),
                "price": product.get("price"),
                "sale_price": product.get("sale_price"),
                "stock_count": product.get("stock_count"),
                "unlimited": product.get("unlimited"),
                "low_stock_alert": product.get("low_stock_alert"),
                "category": category_name,
                "parent_category": parent_category_name,
                "brand": brand_name,
                "line": line,
                "product_size": json.dumps(product.get("product_size")),
                "packing_size": json.dumps(product.get("packing_size")),
                "tags": tags,
                "mpn": product.get("mpn"),
                "state": product.get("state"),
                "min_quantity": product.get("min_quantity"),
                "inc_quantity": product.get("inc_quantity"),
                "max_quantity": product.get("max_quantity"),
                "tax_percentage": product.get("tax_percentage"),
                "total_sales": product.get("total_sales"),
                "created_at": _parse_ts(product.get("createdAt")),
                "updated_at": _parse_ts(product.get("updatedAt")),
                "published_at": _parse_ts(product.get("publishedAt")),
                "resource_id": str(synced_resource_id),
            },
        )

    # Process gallery images: download each format and upload as synced resources
    gallery = product.get("gallery", [])
    for image in gallery:
        image_document_id = image.get("documentId") or image.get("id") or "unknown"

        formats = image.get("formats", {})
        for fmt_name, fmt in formats.items():
            image_resource_name = f"{sku} - {fmt.get('name', f'{image_document_id} - {fmt_name}')}"

            url = fmt.get("url")
            if not url:
                continue

            # Create a annotation of type Image for the product resource
            product_resource.add_annotation(
                annotation_type=AnnotationType.IMAGE,
                data={"name": image_resource_name, "url": url},
            )

    # generate markdown using the helper
    markdown = generate_product_summary(
        product, product_resource_name, name, sku, category_name, parent_category_name, brand_name, line, tags
    )
    return {str(resource_id): markdown}


def process(document: SyncedResource, options: dict):
    content = document.get_data()
    product = json.loads(content)
    if product.get("state") == "deleted":
        result = delete_pengo_product(product, document)
    else:
        result = insert_pengo_product(product, document)

    return result


if __name__ == "__main__":
    from json import dump, load
    from sys import argv, stdin, stdout

    if not len(argv) > 1:
        input_doc = load(stdin)
    else:
        with open(argv[1]) as f:
            input_doc = load(f)

    synced_resource = input_doc["synced_resource"]
    options = input_doc.get("options", {})
    document = SyncedResource(synced_resource["knowledge_id"], synced_resource["id"])
    result = process(document, options)
    dump(result, stdout)
