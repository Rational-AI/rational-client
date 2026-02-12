from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.synced_resource_status import SyncedResourceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processing_workflow_dto import ProcessingWorkflowDto


T = TypeVar("T", bound="SyncedResourceDto")


@_attrs_define
class SyncedResourceDto:
    """
    Attributes:
        id (UUID):
        name (str):
        status (SyncedResourceStatus):
        knowledge_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        size (int | None | Unset):
        digest (None | str | Unset):
        mime_type (None | str | Unset):
        last_error (None | str | Unset):
        knowledge_source_id (None | Unset | UUID):
        parent_id (None | Unset | UUID):
        processing_workflow (ProcessingWorkflowDto | Unset):
        processing_workflow_options (Any | Unset):
    """

    id: UUID
    name: str
    status: SyncedResourceStatus
    knowledge_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    size: int | None | Unset = UNSET
    digest: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    last_error: None | str | Unset = UNSET
    knowledge_source_id: None | Unset | UUID = UNSET
    parent_id: None | Unset | UUID = UNSET
    processing_workflow: ProcessingWorkflowDto | Unset = UNSET
    processing_workflow_options: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        status = self.status.value

        knowledge_id = str(self.knowledge_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        digest: None | str | Unset
        if isinstance(self.digest, Unset):
            digest = UNSET
        else:
            digest = self.digest

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        knowledge_source_id: None | str | Unset
        if isinstance(self.knowledge_source_id, Unset):
            knowledge_source_id = UNSET
        elif isinstance(self.knowledge_source_id, UUID):
            knowledge_source_id = str(self.knowledge_source_id)
        else:
            knowledge_source_id = self.knowledge_source_id

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        processing_workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.processing_workflow, Unset):
            processing_workflow = self.processing_workflow.to_dict()

        processing_workflow_options = self.processing_workflow_options

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "knowledgeId": knowledge_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if digest is not UNSET:
            field_dict["digest"] = digest
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if knowledge_source_id is not UNSET:
            field_dict["knowledgeSourceId"] = knowledge_source_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if processing_workflow is not UNSET:
            field_dict["processingWorkflow"] = processing_workflow
        if processing_workflow_options is not UNSET:
            field_dict["processingWorkflowOptions"] = processing_workflow_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_workflow_dto import ProcessingWorkflowDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        status = SyncedResourceStatus(d.pop("status"))

        knowledge_id = UUID(d.pop("knowledgeId"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_digest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        digest = _parse_digest(d.pop("digest", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

        def _parse_knowledge_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_source_id_type_0 = UUID(data)

                return knowledge_source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        knowledge_source_id = _parse_knowledge_source_id(d.pop("knowledgeSourceId", UNSET))

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        _processing_workflow = d.pop("processingWorkflow", UNSET)
        processing_workflow: ProcessingWorkflowDto | Unset
        if isinstance(_processing_workflow, Unset):
            processing_workflow = UNSET
        else:
            processing_workflow = ProcessingWorkflowDto.from_dict(_processing_workflow)

        processing_workflow_options = d.pop("processingWorkflowOptions", UNSET)

        synced_resource_dto = cls(
            id=id,
            name=name,
            status=status,
            knowledge_id=knowledge_id,
            created_at=created_at,
            updated_at=updated_at,
            size=size,
            digest=digest,
            mime_type=mime_type,
            last_error=last_error,
            knowledge_source_id=knowledge_source_id,
            parent_id=parent_id,
            processing_workflow=processing_workflow,
            processing_workflow_options=processing_workflow_options,
        )

        return synced_resource_dto
