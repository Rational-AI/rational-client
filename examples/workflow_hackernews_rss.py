#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rational-client",
#     "requests",
# ]
# ///
import contextlib
import re
import xml.etree.ElementTree as ET
from io import BytesIO
from typing import Any
from urllib.parse import urlparse

import requests

from rational_client.core import (
    File,
    Knowledge,
    SyncedResource,
)


def _sanitize_filename(name: str, max_len: int = 80, ext: str = ".html") -> str:
    base = re.sub(r"[^\w\s\-\.]", "", name).strip().replace(" ", "_")
    if not base:
        base = "hn_entry"
    if len(base) > max_len:
        base = base[:max_len]
    if not base.lower().endswith(ext.lower()):
        base += ext
    return base


def _parse_rss(xml_bytes: bytes) -> list[dict[str, Any]]:
    root = ET.fromstring(xml_bytes)
    channel = root.find("channel")
    items = channel.findall("item") if channel is not None else []
    entries: list[dict[str, Any]] = []
    for it in items:
        entries.append(
            {
                "title": (it.findtext("title") or "").strip(),
                "link": (it.findtext("link") or "").strip(),
                "comments": (it.findtext("comments") or "").strip(),
                "pubDate": (it.findtext("pubDate") or "").strip(),
            }
        )
    return entries


def process(document: SyncedResource, options: dict):
    """
    Assumes the input synced resource IS the dumped RSS feed to be parsed.
    It parses the RSS, fetches each entry's linked HTML, uploads it as a synced resource
    under the input document, and creates a resource that points to it.
    """
    # Read the RSS XML bytes directly from the input synced resource
    content = document.get_data()
    entries = _parse_rss(content)

    # Optional limit; if not provided, process all entries
    limit = options.get("limit")
    if limit is not None:
        with contextlib.suppress(Exception):
            entries = entries[: int(limit)]

    knowledge = Knowledge(document.knowledge_id)

    # Create a resource for the RSS feed itself
    _ = knowledge.create_resource(
        name=document.name,
        category="RSS Feeds",
        notes=f"Imported from SyncedResource ID {document.id}",
        tags=["rss", "hn"],
        synced_resource_id=document.id,
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; RationaleAI/1.0; +https://news.ycombinator.com/)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    for i, entry in enumerate(entries, start=1):
        url = entry.get("link") or ""
        title = entry.get("title") or url or f"HN Entry #{i}"

        if not url:
            continue

        try:
            resp = requests.get(url, headers=headers, timeout=30)
            resp.raise_for_status()
        except Exception:
            # Skip entries that fail to fetch
            continue

        html_bytes = resp.content
        mime_type = resp.headers.get("Content-Type", "text/html")

        # Build filename from title (fallback to host_path)
        filename = _sanitize_filename(title, ext=".html")
        if filename == "hn_entry.html":
            parsed = urlparse(url)
            fallback = (parsed.netloc + parsed.path).strip("/").replace("/", "_") or "page"
            filename = _sanitize_filename(fallback, ext=".html")

        # Upload HTML as a synced resource under the input document (the RSS feed)
        f = File(BytesIO(html_bytes), mime_type=mime_type, file_name=filename)
        _ = knowledge.upload_synced_resource(
            name=filename,
            contents=f,
            parent_id=document.id,
        )


if __name__ == "__main__":
    from json import dump, load
    from sys import argv, stdin, stdout

    if not len(argv) > 1:
        # Read input JSON from stdin
        input: dict = load(stdin)
    else:
        # Or from file path
        with open(argv[1]) as f:
            input: dict = load(f)

    synced_resource = input["synced_resource"]
    options = input.get("options", {})
    document = SyncedResource(synced_resource["knowledge_id"], synced_resource["id"])
    result = process(document, options)
    dump(result, stdout)
