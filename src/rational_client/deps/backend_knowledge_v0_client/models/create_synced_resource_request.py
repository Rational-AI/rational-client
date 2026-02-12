from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSyncedResourceRequest")


@_attrs_define
class CreateSyncedResourceRequest:
    """
    Attributes:
        name (str):
        knowledge_source_id (UUID):
        size (int | None | Unset):
        digest (None | str | Unset):
        mime_type (None | str | Unset):
    """

    name: str
    knowledge_source_id: UUID
    size: int | None | Unset = UNSET
    digest: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        knowledge_source_id = str(self.knowledge_source_id)

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "knowledgeSourceId": knowledge_source_id,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if digest is not UNSET:
            field_dict["digest"] = digest
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        knowledge_source_id = UUID(d.pop("knowledgeSourceId"))

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

        create_synced_resource_request = cls(
            name=name,
            knowledge_source_id=knowledge_source_id,
            size=size,
            digest=digest,
            mime_type=mime_type,
        )

        return create_synced_resource_request
