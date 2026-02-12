from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SentimentLabel")


@_attrs_define
class SentimentLabel:
    """
    Attributes:
        sentiment (str):
        color (str):
    """

    sentiment: str
    color: str

    def to_dict(self) -> dict[str, Any]:
        sentiment = self.sentiment

        color = self.color

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sentiment": sentiment,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sentiment = d.pop("sentiment")

        color = d.pop("color")

        sentiment_label = cls(
            sentiment=sentiment,
            color=color,
        )

        return sentiment_label
