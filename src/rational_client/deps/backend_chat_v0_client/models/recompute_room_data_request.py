from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecomputeRoomDataRequest")


@_attrs_define
class RecomputeRoomDataRequest:
    """
    Attributes:
        title (bool | None | Unset):
        topic (bool | None | Unset):
        sentiment (bool | None | Unset):
        wait_for_completion (bool | None | Unset):
    """

    title: bool | None | Unset = UNSET
    topic: bool | None | Unset = UNSET
    sentiment: bool | None | Unset = UNSET
    wait_for_completion: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: bool | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        topic: bool | None | Unset
        if isinstance(self.topic, Unset):
            topic = UNSET
        else:
            topic = self.topic

        sentiment: bool | None | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        wait_for_completion: bool | None | Unset
        if isinstance(self.wait_for_completion, Unset):
            wait_for_completion = UNSET
        else:
            wait_for_completion = self.wait_for_completion

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if topic is not UNSET:
            field_dict["topic"] = topic
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if wait_for_completion is not UNSET:
            field_dict["waitForCompletion"] = wait_for_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_topic(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        topic = _parse_topic(d.pop("topic", UNSET))

        def _parse_sentiment(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        def _parse_wait_for_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        wait_for_completion = _parse_wait_for_completion(d.pop("waitForCompletion", UNSET))

        recompute_room_data_request = cls(
            title=title,
            topic=topic,
            sentiment=sentiment,
            wait_for_completion=wait_for_completion,
        )

        return recompute_room_data_request
