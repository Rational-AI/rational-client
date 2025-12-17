from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        size (Union[None, Unset, int]):
        digest (Union[None, Unset, str]):
        mime_type (Union[None, Unset, str]):
    """

    name: str
    knowledge_source_id: UUID
    size: Union[None, Unset, int] = UNSET
    digest: Union[None, Unset, str] = UNSET
    mime_type: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        knowledge_source_id = str(self.knowledge_source_id)

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

        create_synced_resource_request = cls(
            name=name,
            knowledge_source_id=knowledge_source_id,
            size=size,
            digest=digest,
            mime_type=mime_type,
        )

        return create_synced_resource_request
