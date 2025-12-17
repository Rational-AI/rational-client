from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateResourceRequest")


@_attrs_define
class CreateResourceRequest:
    """
    Attributes:
        name (Union[None, Unset, str]):
        category (Union[None, Unset, str]):
        notes (Union[None, Unset, str]):
        synced_resource_id (Union[None, UUID, Unset]):
        tags (Union[None, Unset, list[str]]):
    """

    name: Union[None, Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    synced_resource_id: Union[None, UUID, Unset] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        synced_resource_id: Union[None, Unset, str]
        if isinstance(self.synced_resource_id, Unset):
            synced_resource_id = UNSET
        elif isinstance(self.synced_resource_id, UUID):
            synced_resource_id = str(self.synced_resource_id)
        else:
            synced_resource_id = self.synced_resource_id

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if notes is not UNSET:
            field_dict["notes"] = notes
        if synced_resource_id is not UNSET:
            field_dict["syncedResourceId"] = synced_resource_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_synced_resource_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_resource_id_type_0 = UUID(data)

                return synced_resource_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        synced_resource_id = _parse_synced_resource_id(d.pop("syncedResourceId", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        create_resource_request = cls(
            name=name,
            category=category,
            notes=notes,
            synced_resource_id=synced_resource_id,
            tags=tags,
        )

        return create_resource_request
