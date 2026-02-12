from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Param")


@_attrs_define
class Param:
    """
    Attributes:
        type_ (str):
        is_required (bool):
        is_hidden (bool):
        alias (None | str | Unset):
        description (None | str | Unset):
        default_value (Any | Unset):
    """

    type_: str
    is_required: bool
    is_hidden: bool
    alias: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    default_value: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        is_required = self.is_required

        is_hidden = self.is_hidden

        alias: None | str | Unset
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        default_value = self.default_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "isRequired": is_required,
                "isHidden": is_hidden,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        is_required = d.pop("isRequired")

        is_hidden = d.pop("isHidden")

        def _parse_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        default_value = d.pop("defaultValue", UNSET)

        param = cls(
            type_=type_,
            is_required=is_required,
            is_hidden=is_hidden,
            alias=alias,
            description=description,
            default_value=default_value,
        )

        return param
