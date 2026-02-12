from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateRequest")


@_attrs_define
class UpdateRequest:
    """
    Attributes:
        enable (bool):
    """

    enable: bool

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enable": enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable")

        update_request = cls(
            enable=enable,
        )

        return update_request
