#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rational-client"
# ]
# ///
import json
import sqlite3
import tempfile

from rational_client.core import File, Knowledge, SyncedResource


def generate_product_markdown(product: dict) -> str:
    """Generate a markdown summary for a product."""
    title = product.get("title", "Untitled Product")
    description = product.get("description", "No description available")
    collection = product.get("collection", "Uncategorized")
    vendor = product.get("vendor", "N/A")
    price = product.get("price", "N/A")
    available = "In stock" if product.get("available") else "Out of stock"
    sku = product.get("sku", "N/A")
    handle = product.get("handle", "N/A")

    markdown = f"## Product: {title}\n\n"
    markdown += f"**Description:** {description}\n\n"
    markdown += f"**Collection:** {collection}\n\n"
    markdown += f"**Vendor:** {vendor}\n\n"
    markdown += f"**SKU:** {sku}\n\n"
    markdown += f"**Handle:** {handle}\n\n"
    markdown += f"**Price:** {price}\n\n"
    markdown += f"**Availability:** {available}\n\n"

    # Add variant information
    variants = product.get("variants", [])
    if variants:
        markdown += f"**Variants:** {len(variants)} available\n\n"

    # Add image information
    images = product.get("images", [])
    if images:
        markdown += f"**Images:** {len(images)} image(s)\n"

    return markdown


def generate_variant_markdown(product: dict, variant: dict) -> str:
    """Generate a markdown summary for a product variant."""
    product_title = product.get("title", "Untitled Product")
    variant_title = variant.get("title", "Variant")
    price = variant.get("price", "N/A")
    sku = variant.get("sku", "N/A")
    available = "In stock" if variant.get("available") else "Out of stock"

    markdown = f"## Variant: {product_title} - {variant_title}\n\n"
    markdown += f"**Product:** {product_title}\n\n"
    markdown += f"**SKU:** {sku}\n\n"
    markdown += f"**Price:** {price}\n\n"
    markdown += f"**Availability:** {available}\n\n"

    # Add option details
    options = []
    if variant.get("options1"):
        options.append(f"Option 1: {variant['options1']}")
    if variant.get("options2"):
        options.append(f"Option 2: {variant['options2']}")
    if variant.get("options3"):
        options.append(f"Option 3: {variant['options3']}")

    if options:
        markdown += "**Options:**\n\n"
        for option in options:
            markdown += f"- {option}\n"
        markdown += "\n"

    # Add image information
    images = variant.get("images", [])
    if images:
        markdown += f"**Images:** {len(images)} image(s)\n"

    return markdown


def extract_materials(description: str, components: dict | None = None) -> set:
    """Extract material names from product description and components."""
    # Common materials to look for in descriptions
    materials = [
        # Woods
        "oak",
        "teak",
        "pine",
        "walnut",
        "mahogany",
        "beech",
        "ash",
        "mindi",
        "elm",
        "parawood",
        "larch",
        "catalpa",
        "spruce",
        "cherry",
        "maple",
        "birch",
        "bamboo",
        # Stone/Mineral
        "marble",
        "stone",
        "bluestone",
        "carrara",
        "petrified wood",
        # Metals
        "brass",
        "zinc",
        "iron",
        "steel",
        "aluminum",
        "copper",
        "metal",
        # Natural fibers
        "rattan",
        "wicker",
        "cane",
        "sea grass",
        "seagrass",
        # Fabrics/Textiles
        "leather",
        "fabric",
        "linen",
        "cotton",
        "velvet",
        "polyester",
        "faux leather",
        "crypton",
        # Other
        "lacquer",
        "wood",
        "glass",
        "ceramic",
        "plastic",
        "foam",
        "veneer",
        "wax",
        "elastic",
    ]

    found_materials = set()
    desc_lower = description.lower()

    # Extract from description
    for material in materials:
        if material in desc_lower:
            found_materials.add(material)

    # Extract from components if available
    if components and "components" in components:
        for component in components["components"]:
            material = component.get("material", "")
            if material and material.lower() not in ["null", "none", ""]:
                # Normalize the material name
                material_lower = material.lower()

                # Try to match with our known materials
                for known_material in materials:
                    if known_material in material_lower:
                        found_materials.add(known_material)

    return found_materials


def process(document: SyncedResource, options: dict):
    # Parse the JSON data from the resource
    content = document.get_data()
    products = json.loads(content)

    # Dictionary to store resource_id -> markdown mappings
    markdown_summaries = {}

    # Create a temp SQLite database file
    with tempfile.NamedTemporaryFile(suffix=".db") as db_file:
        db_path = db_file.name

        # Create the schema
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    collection TEXT COLLATE NOCASE,
                    title TEXT COLLATE NOCASE,
                    description TEXT COLLATE NOCASE,
                    images TEXT COLLATE NOCASE,
                    vendor TEXT COLLATE NOCASE,
                    handle TEXT COLLATE NOCASE,
                    sku TEXT COLLATE NOCASE,
                    price INTEGER,
                    available BOOLEAN,
                    resource_id TEXT
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS variants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    title TEXT COLLATE NOCASE,
                    price INTEGER,
                    sku TEXT COLLATE NOCASE,
                    options1 TEXT COLLATE NOCASE,
                    options2 TEXT COLLATE NOCASE,
                    options3 TEXT COLLATE NOCASE,
                    available BOOLEAN,
                    images TEXT COLLATE NOCASE,
                    resource_id TEXT
                );
            """)

            knowledge = Knowledge(document.knowledge_id)

            # Track all product resources for creating relations later
            product_resources_with_metadata = []

            for product in products:
                # Create rational resource for product
                tags = []
                if product.get("collection"):
                    tags.append(product["collection"])
                if product.get("vendor"):
                    tags.append(product["vendor"])
                product_resource = knowledge.create_resource(
                    name=product.get("title", "Untitled Product"),
                    category=product.get("collection", "Uncategorized"),
                    notes=product.get("description", ""),
                    tags=tags,
                    synced_resource_id=document.id,
                )

                resource_id = product_resource.resource_id

                # Generate and store markdown summary for the product
                product_markdown = generate_product_markdown(product)
                markdown_summaries[str(resource_id)] = product_markdown

                # Extract materials from description and components, and track metadata
                materials = extract_materials(product.get("description", ""), product.get("components"))
                category = product.get("collection", "Uncategorized")

                product_resources_with_metadata.append(
                    {
                        "resource": product_resource,
                        "materials": materials,
                        "category": category,
                    }
                )

                # Insert product into DB
                cur.execute(
                    """
                    INSERT INTO products (
                        product_id, collection, title, description, images, vendor, handle, sku, price, available,
                        resource_id
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        product.get("id"),
                        product.get("collection"),
                        product.get("title"),
                        product.get("description"),
                        json.dumps(product.get("images")),
                        product.get("vendor"),
                        product.get("handle"),
                        product.get("sku"),
                        product.get("price"),
                        product.get("available"),
                        str(resource_id),
                    ),
                )

                # Add "has_picture" relation for product images
                for image_name in product.get("images", []):
                    try:
                        image_resource = knowledge.get_resource_by_name(image_name)
                        product_resource.add_relation(image_resource, type="has_picture")
                    except Exception:
                        pass  # Do nothing if image resource not found

                # Insert variants and create resources/relations
                variant_resources = []
                for variant in product.get("variants", []):
                    # Create rational resource for variant
                    variant_resource = knowledge.create_resource(
                        name=f"{product.get('title', 'Untitled Product')} - {variant.get('title', 'Variant')}",
                        category=product.get("collection", "Uncategorized"),
                        notes="",
                        tags=tags,
                        synced_resource_id=document.id,
                    )
                    variant_resource_id = variant_resource.resource_id

                    # Generate and store markdown summary for the variant
                    variant_markdown = generate_variant_markdown(product, variant)
                    markdown_summaries[str(variant_resource_id)] = variant_markdown

                    cur.execute(
                        """
                        INSERT INTO variants (
                            product_id, title, price, sku, options1, options2, options3, available, images, resource_id
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            variant.get("product_id"),
                            variant.get("title"),
                            variant.get("price"),
                            variant.get("sku"),
                            variant.get("options1"),
                            variant.get("options2"),
                            variant.get("options3"),
                            variant.get("available"),
                            json.dumps(variant.get("images")),
                            str(variant_resource_id),
                        ),
                    )
                    # Add "has_picture" relation for variant images
                    for image_name in variant.get("images", []):
                        try:
                            image_resource = knowledge.get_resource_by_name(image_name)
                            variant_resource.add_relation(image_resource, type="has_picture")
                        except Exception:
                            pass  # Do nothing if image resource not found

                    variant_resources.append(variant_resource)

                # Add "variant" relation from product to each variant
                for variant_resource in variant_resources:
                    product_resource.add_relation(variant_resource, type="variant")

            # Create relations between products based on shared attributes
            for i, item1 in enumerate(product_resources_with_metadata):
                for item2 in product_resources_with_metadata[i + 1 :]:
                    # Same category relation
                    if item1["category"] == item2["category"]:
                        item1["resource"].add_relation(item2["resource"], type="same_category")

                    # Same material relation - create one relation if they share any materials
                    shared_materials = item1["materials"] & item2["materials"]
                    if shared_materials:
                        item1["resource"].add_relation(item2["resource"], type="same_material")

            conn.commit()

        # Create a RationalResource for the SQLite database
        with open(db_path, "rb") as f:
            _ = knowledge.upload_synced_resource(
                name="products.db",
                contents=File(f, file_name="products.db", mime_type="application/x-sqlite3"),
                parent_id=document.id,
            )

    # Return markdown summaries for chunking and embedding
    return markdown_summaries


if __name__ == "__main__":
    from json import dump, load
    from sys import argv, stdin, stdout

    if not len(argv) > 1:
        # Read from stdin
        input: dict = load(stdin)
    else:
        # Read from file
        with open(argv[1]) as f:
            input: dict = load(f)

    synced_resource = input["synced_resource"]
    options = input.get("options", {})
    document = SyncedResource(synced_resource["knowledge_id"], synced_resource["id"])
    result = process(document, options)
    dump(result, stdout)
