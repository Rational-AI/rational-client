from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolConfigurationParam")


@_attrs_define
class ToolConfigurationParam:
    """
    Attributes:
        name (str):
        auto (bool):
        value (Union[Unset, Any]):
    """

    name: str
    auto: bool
    value: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        auto = self.auto

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "auto": auto,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        auto = d.pop("auto")

        value = d.pop("value", UNSET)

        tool_configuration_param = cls(
            name=name,
            auto=auto,
            value=value,
        )

        return tool_configuration_param
