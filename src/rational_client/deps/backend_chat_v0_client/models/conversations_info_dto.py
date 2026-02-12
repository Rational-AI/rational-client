from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.conversations_info_dto_sentiments import ConversationsInfoDtoSentiments
    from ..models.conversations_info_dto_topics import ConversationsInfoDtoTopics


T = TypeVar("T", bound="ConversationsInfoDto")


@_attrs_define
class ConversationsInfoDto:
    """
    Attributes:
        topics (ConversationsInfoDtoTopics):
        sentiments (ConversationsInfoDtoSentiments):
    """

    topics: ConversationsInfoDtoTopics
    sentiments: ConversationsInfoDtoSentiments

    def to_dict(self) -> dict[str, Any]:
        topics = self.topics.to_dict()

        sentiments = self.sentiments.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "topics": topics,
                "sentiments": sentiments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversations_info_dto_sentiments import ConversationsInfoDtoSentiments
        from ..models.conversations_info_dto_topics import ConversationsInfoDtoTopics

        d = dict(src_dict)
        topics = ConversationsInfoDtoTopics.from_dict(d.pop("topics"))

        sentiments = ConversationsInfoDtoSentiments.from_dict(d.pop("sentiments"))

        conversations_info_dto = cls(
            topics=topics,
            sentiments=sentiments,
        )

        return conversations_info_dto
