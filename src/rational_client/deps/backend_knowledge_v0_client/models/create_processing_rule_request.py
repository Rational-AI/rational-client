from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateProcessingRuleRequest")


@_attrs_define
class CreateProcessingRuleRequest:
    """
    Attributes:
        name (str):
        code (str):
    """

    name: str
    code: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        create_processing_rule_request = cls(
            name=name,
            code=code,
        )

        return create_processing_rule_request
