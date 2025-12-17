import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
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
        size (Union[None, Unset, int]):
        digest (Union[None, Unset, str]):
        mime_type (Union[None, Unset, str]):
        knowledge_source_id (Union[None, UUID, Unset]):
        parent_id (Union[None, UUID, Unset]):
        processing_workflow (Union[Unset, ProcessingWorkflowDto]):
        processing_workflow_options (Union[Unset, Any]):
    """

    id: UUID
    name: str
    status: SyncedResourceStatus
    knowledge_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    size: Union[None, Unset, int] = UNSET
    digest: Union[None, Unset, str] = UNSET
    mime_type: Union[None, Unset, str] = UNSET
    knowledge_source_id: Union[None, UUID, Unset] = UNSET
    parent_id: Union[None, UUID, Unset] = UNSET
    processing_workflow: Union[Unset, "ProcessingWorkflowDto"] = UNSET
    processing_workflow_options: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        status = self.status.value

        knowledge_id = str(self.knowledge_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        digest: Union[None, Unset, str]
        if isinstance(self.digest, Unset):
            digest = UNSET
        else:
            digest = self.digest

        mime_type: Union[None, Unset, str]
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        knowledge_source_id: Union[None, Unset, str]
        if isinstance(self.knowledge_source_id, Unset):
            knowledge_source_id = UNSET
        elif isinstance(self.knowledge_source_id, UUID):
            knowledge_source_id = str(self.knowledge_source_id)
        else:
            knowledge_source_id = self.knowledge_source_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        processing_workflow: Union[Unset, dict[str, Any]] = UNSET
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

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_digest(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        digest = _parse_digest(d.pop("digest", UNSET))

        def _parse_mime_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mime_type = _parse_mime_type(d.pop("mimeType", UNSET))

        def _parse_knowledge_source_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_source_id_type_0 = UUID(data)

                return knowledge_source_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        knowledge_source_id = _parse_knowledge_source_id(d.pop("knowledgeSourceId", UNSET))

        def _parse_parent_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        _processing_workflow = d.pop("processingWorkflow", UNSET)
        processing_workflow: Union[Unset, ProcessingWorkflowDto]
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
            knowledge_source_id=knowledge_source_id,
            parent_id=parent_id,
            processing_workflow=processing_workflow,
            processing_workflow_options=processing_workflow_options,
        )

        return synced_resource_dto
