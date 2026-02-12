from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.widget_input import WidgetInput


T = TypeVar("T", bound="Widget")


@_attrs_define
class Widget:
    """
    Attributes:
        tag_name (str):
        url (str):
        inputs (list[WidgetInput]):
    """

    tag_name: str
    url: str
    inputs: list[WidgetInput]

    def to_dict(self) -> dict[str, Any]:
        tag_name = self.tag_name

        url = self.url

        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tagName": tag_name,
                "url": url,
                "inputs": inputs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget_input import WidgetInput

        d = dict(src_dict)
        tag_name = d.pop("tagName")

        url = d.pop("url")

        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in _inputs:
            inputs_item = WidgetInput.from_dict(inputs_item_data)

            inputs.append(inputs_item)

        widget = cls(
            tag_name=tag_name,
            url=url,
            inputs=inputs,
        )

        return widget
