from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.override_discriminator import OverrideDiscriminator
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelRequestOverride")


@_attrs_define
class ModelRequestOverride:
    """
    Attributes:
        key (str):
        operation (OverrideDiscriminator):
        value (Union[Unset, Any]):
    """

    key: str
    operation: OverrideDiscriminator
    value: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        operation = self.operation.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "operation": operation,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        operation = OverrideDiscriminator(d.pop("operation"))

        value = d.pop("value", UNSET)

        model_request_override = cls(
            key=key,
            operation=operation,
            value=value,
        )

        return model_request_override
