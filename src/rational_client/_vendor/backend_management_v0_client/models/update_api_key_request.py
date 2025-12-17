from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApiKeyRequest")


@_attrs_define
class UpdateApiKeyRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        update_api_key_request = cls(
            name=name,
            enabled=enabled,
        )

        return update_api_key_request
