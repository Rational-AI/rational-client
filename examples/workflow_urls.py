#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rational-client",
#     "requests",
# ]
# ///
from io import BytesIO

import requests

from rational_client.core import (
    File,
    Knowledge,
    SyncedResource,
)
from rational_client.utils import run


def process(document: SyncedResource, options: dict):
    content = document.get_data()
    # Assume that content is a list of URLs to be parsed
    urls = content.decode("utf-8").splitlines()

    knowledge = Knowledge(document.knowledge_id)

    # We can now use docling to extract the content of each webpage and resource in the Knowledge
    for url in urls:
        # Using docling to extract content
        result = requests.get(url)
        filename = url.split("/")[-1]
        mime_type = result.headers.get("Content-Type", None)
        f = File(BytesIO(result.content), mime_type=mime_type, file_name=filename)
        _ = knowledge.upload_synced_resource(filename, contents=f, parent_id=document.id)


run(process)
