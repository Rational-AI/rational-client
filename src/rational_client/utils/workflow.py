import mimetypes
from json import dump, load
from pathlib import Path
from sys import argv, stdin, stdout
from typing import Callable
from uuid import UUID

from rational_client.deps.backend_knowledge_v0_client.api.synced_resource import upload_synced_resource
from rational_client.deps.backend_knowledge_v0_client.models import (
    SyncedResourceDto,
    UploadSyncedResourceRequest,
)
from rational_client.deps.backend_knowledge_v0_client.types import File

from ..core.backend_clients import knowledge_client
from ..core.public_api import SyncedResource


def upload_to_knowledge(knowledge_id: str | UUID, filepath: str):
    """Upload a local file to a knowledge base."""

    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    mime_type, _ = mimetypes.guess_type(filepath)
    file_name = path.name

    resource = None
    with open(filepath, "rb") as f:
        file_payload = File(payload=f, file_name=file_name, mime_type=mime_type)
        request = UploadSyncedResourceRequest(
            name=file_name,
            data=file_payload,
            knowledge_id=knowledge_id if isinstance(knowledge_id, UUID) else UUID(knowledge_id),
        )
        result = upload_synced_resource.sync(
            client=knowledge_client,
            body=request,
        )
        if not isinstance(result, SyncedResourceDto):
            raise ValueError("Failed to upload file to knowledge base.")
        resource = result

    return SyncedResource(
        knowledge_id=resource.knowledge_id,
        id=resource.id,
        internal_dto=resource,
    )


def run(process: Callable[["SyncedResource", dict], dict[str, str] | None]):

    # Load input from file argument or stdin
    if len(argv) > 1:
        with open(argv[1]) as f:
            data = load(f)
    else:
        data = load(stdin)

    options = data.get("options", {})

    # 1. Standard nested format: {"synced_resource": {"knowledge_id": "...", "id": "..."}}
    sr_data = data.get("synced_resource")
    if sr_data:
        k_id = UUID(str(sr_data["knowledge_id"]))
        r_id = UUID(str(sr_data["id"]))
        document = SyncedResource(k_id, r_id)

    # 2. Local-path format (Enhanced UX): {"knowledge_id": "...", "path": "..."}"
    elif "path" in data and "knowledge_id" in data:
        document = upload_to_knowledge(data["knowledge_id"], data["path"])

    # 3. Flat ID format: {"knowledge_id": "...", "synced_resource_id": "..."}
    elif "knowledge_id" in data and "synced_resource_id" in data:
        k_id = UUID(str(data["knowledge_id"]))
        r_id = UUID(str(data["synced_resource_id"]))
        document = SyncedResource(k_id, r_id)
    else:
        raise ValueError("Invalid input format. Expected 'synced_resource' or 'path'.")

    result = process(document, options)
    dump(result, stdout)
