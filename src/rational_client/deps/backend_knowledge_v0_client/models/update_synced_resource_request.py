from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.synced_resource_status import SyncedResourceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSyncedResourceRequest")


@_attrs_define
class UpdateSyncedResourceRequest:
    """
    Attributes:
        name (str | Unset):
        size (int | None | Unset):
        digest (None | str | Unset):
        mime_type (None | str | Unset):
        status (SyncedResourceStatus | Unset):
        last_error (None | str | Unset):
        processing_workflow_id (None | Unset | UUID):
        processing_workflow_options (Any | Unset):
    """

    name: str | Unset = UNSET
    size: int | None | Unset = UNSET
    digest: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    status: SyncedResourceStatus | Unset = UNSET
    last_error: None | str | Unset = UNSET
    processing_workflow_id: None | Unset | UUID = UNSET
    processing_workflow_options: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        processing_workflow_id: None | str | Unset
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
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if processing_workflow_id is not UNSET:
            field_dict["processingWorkflowId"] = processing_workflow_id
        if processing_workflow_options is not UNSET:
            field_dict["processingWorkflowOptions"] = processing_workflow_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

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

        _status = d.pop("status", UNSET)
        status: SyncedResourceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SyncedResourceStatus(_status)

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

        def _parse_processing_workflow_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processing_workflow_id_type_0 = UUID(data)

                return processing_workflow_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        processing_workflow_id = _parse_processing_workflow_id(d.pop("processingWorkflowId", UNSET))

        processing_workflow_options = d.pop("processingWorkflowOptions", UNSET)

        update_synced_resource_request = cls(
            name=name,
            size=size,
            digest=digest,
            mime_type=mime_type,
            status=status,
            last_error=last_error,
            processing_workflow_id=processing_workflow_id,
            processing_workflow_options=processing_workflow_options,
        )

        return update_synced_resource_request
