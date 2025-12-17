from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateApiKeyRequest")


@_attrs_define
class CreateApiKeyRequest:
    """
    Attributes:
        name (str):
        enabled (Union[None, Unset, bool]):
    """

    name: str
    enabled: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled: Union[None, Unset, bool]
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        create_api_key_request = cls(
            name=name,
            enabled=enabled,
        )

        return create_api_key_request
