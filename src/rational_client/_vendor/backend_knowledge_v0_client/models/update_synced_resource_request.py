from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.synced_resource_status import SyncedResourceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSyncedResourceRequest")


@_attrs_define
class UpdateSyncedResourceRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        size (Union[None, Unset, int]):
        digest (Union[None, Unset, str]):
        mime_type (Union[None, Unset, str]):
        status (Union[Unset, SyncedResourceStatus]):
        processing_workflow_id (Union[None, UUID, Unset]):
        processing_workflow_options (Union[Unset, Any]):
    """

    name: Union[Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    digest: Union[None, Unset, str] = UNSET
    mime_type: Union[None, Unset, str] = UNSET
    status: Union[Unset, SyncedResourceStatus] = UNSET
    processing_workflow_id: Union[None, UUID, Unset] = UNSET
    processing_workflow_options: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        processing_workflow_id: Union[None, Unset, str]
        if isinstance(self.processing_workflow_id, Unset):
            processing_workflow_id = UNSET
        elif isinstance(self.processing_workflow_id, UUID):
            processing_workflow_id = str(self.processing_workflow_id)
        else:
            processing_workflow_id = self.processing_workflow_id

        processing_workflow_options = self.processing_workflow_options

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if digest is not UNSET:
            field_dict["digest"] = digest
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if status is not UNSET:
            field_dict["status"] = status
        if processing_workflow_id is not UNSET:
            field_dict["processingWorkflowId"] = processing_workflow_id
        if processing_workflow_options is not UNSET:
            field_dict["processingWorkflowOptions"] = processing_workflow_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, SyncedResourceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SyncedResourceStatus(_status)

        def _parse_processing_workflow_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processing_workflow_id_type_0 = UUID(data)

                return processing_workflow_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        processing_workflow_id = _parse_processing_workflow_id(d.pop("processingWorkflowId", UNSET))

        processing_workflow_options = d.pop("processingWorkflowOptions", UNSET)

        update_synced_resource_request = cls(
            name=name,
            size=size,
            digest=digest,
            mime_type=mime_type,
            status=status,
            processing_workflow_id=processing_workflow_id,
            processing_workflow_options=processing_workflow_options,
        )

        return update_synced_resource_request
