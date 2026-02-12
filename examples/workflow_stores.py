#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rational-client",
# ]
# ///
import json

from rational_client.core import (
    Knowledge,
    SyncedResource,
)
from rational_client.utils import run


def process(document: SyncedResource, options: dict):
    # Parse the JSON data from the resource
    content = document.get_data()
    stores = json.loads(content)

    # Create markdown content
    markdown_lines = []
    markdown_lines.append("# Store Locations")
    markdown_lines.append("")
    markdown_lines.append("A comprehensive list of our retail store locations across Italy.")
    markdown_lines.append("")

    # Add summary statistics
    total_stores = len(stores)
    cities = set(store.get("City", "Unknown") for store in stores)
    markdown_lines.append(f"**Total Stores:** {total_stores}")
    markdown_lines.append(f"**Cities:** {len(cities)}")
    markdown_lines.append("")

    # Create table header
    markdown_lines.append("## Store Directory")
    markdown_lines.append("")
    markdown_lines.append("| # | City | Address | Coordinates |")
    markdown_lines.append("|---|------|---------|-------------|")

    # Add each store as a table row
    for store in stores:
        store_num = store.get("#", "N/A")
        city = store.get("City", "Unknown")
        address = store.get("Address", "No address provided")
        lat = store.get("Latitude", "")
        lon = store.get("Longitude", "")

        # Format coordinates
        coordinates = f"{lat}, {lon}" if lat and lon else "Not available"

        markdown_lines.append(f"| {store_num} | {city} | {address} | {coordinates} |")

    markdown_lines.append("")

    # Add city breakdown
    markdown_lines.append("## Cities Overview")
    markdown_lines.append("")
    city_list = sorted(cities)
    for city in city_list:
        city_stores = [s for s in stores if s.get("City") == city]
        markdown_lines.append(f"- **{city}**: {len(city_stores)} store{'s' if len(city_stores) != 1 else ''}")

    markdown_content = "\n".join(markdown_lines)

    # Create a resource for the processed data
    knowledge = Knowledge(document.knowledge_id)
    resource = knowledge.create_resource(
        name=document.name,
        synced_resource_id=document.id,
    )

    # Return the markdown content
    return {str(resource.resource_id): markdown_content}


run(process)
