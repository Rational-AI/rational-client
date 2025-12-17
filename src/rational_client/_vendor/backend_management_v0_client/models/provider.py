from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Provider")


@_attrs_define
class Provider:
    """
    Attributes:
        kind (str):
    """

    kind: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        provider = cls(
            kind=kind,
        )

        return provider
