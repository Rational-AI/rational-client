from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        alias (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        default_value (Union[Unset, Any]):
    """

    type_: str
    is_required: bool
    is_hidden: bool
    alias: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    default_value: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        is_required = self.is_required

        is_hidden = self.is_hidden

        alias: Union[None, Unset, str]
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        description: Union[None, Unset, str]
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

        def _parse_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
