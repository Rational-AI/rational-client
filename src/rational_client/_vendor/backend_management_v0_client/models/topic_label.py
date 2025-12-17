from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TopicLabel")


@_attrs_define
class TopicLabel:
    """
    Attributes:
        topic (str):
    """

    topic: str

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "topic": topic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        topic = d.pop("topic")

        topic_label = cls(
            topic=topic,
        )

        return topic_label
