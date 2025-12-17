from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeNodeDto")


@_attrs_define
class KnowledgeNodeDto:
    """
    Attributes:
        id (UUID):
        tags (list[str]):
        name (Union[None, Unset, str]):
        category (Union[None, Unset, str]):
        source_id (Union[None, UUID, Unset]):
    """

    id: UUID
    tags: list[str]
    name: Union[None, Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    source_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        tags = self.tags

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

        source_id: Union[None, Unset, str]
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "tags": tags,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        tags = cast(list[str], d.pop("tags"))

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

        def _parse_source_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_id_type_0 = UUID(data)

                return source_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        source_id = _parse_source_id(d.pop("sourceId", UNSET))

        knowledge_node_dto = cls(
            id=id,
            tags=tags,
            name=name,
            category=category,
            source_id=source_id,
        )

        return knowledge_node_dto
