from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.color_config_colors import ColorConfigColors


T = TypeVar("T", bound="ColorConfig")


@_attrs_define
class ColorConfig:
    """
    Attributes:
        default (str):
        colors (ColorConfigColors):
    """

    default: str
    colors: ColorConfigColors

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        colors = self.colors.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default": default,
                "colors": colors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_config_colors import ColorConfigColors

        d = dict(src_dict)
        default = d.pop("default")

        colors = ColorConfigColors.from_dict(d.pop("colors"))

        color_config = cls(
            default=default,
            colors=colors,
        )

        return color_config
