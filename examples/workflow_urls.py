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
