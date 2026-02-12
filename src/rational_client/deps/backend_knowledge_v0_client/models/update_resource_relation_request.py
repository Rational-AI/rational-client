from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateResourceRelationRequest")


@_attrs_define
class UpdateResourceRelationRequest:
    """
    Attributes:
        type_ (str | Unset):
    """

    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        update_resource_relation_request = cls(
            type_=type_,
        )

        return update_resource_relation_request
