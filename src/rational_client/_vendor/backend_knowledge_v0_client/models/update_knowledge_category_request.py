from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKnowledgeCategoryRequest")


@_attrs_define
class UpdateKnowledgeCategoryRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        color (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        color = self.color

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        update_knowledge_category_request = cls(
            name=name,
            color=color,
        )

        return update_knowledge_category_request
