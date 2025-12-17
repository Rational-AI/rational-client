import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_dto import ModelDto
    from ..models.sentiment_configuration_dto import SentimentConfigurationDto
    from ..models.title_configuration_dto import TitleConfigurationDto
    from ..models.topic_configuration_dto import TopicConfigurationDto


T = TypeVar("T", bound="RoomConfigurationDto")


@_attrs_define
class RoomConfigurationDto:
    """
    Attributes:
        id (UUID):
        is_active (bool):
        request_json_response (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        topic (Union[Unset, TopicConfigurationDto]):
        sentiment (Union[Unset, SentimentConfigurationDto]):
        title (Union[Unset, TitleConfigurationDto]):
        default_conversational_model (Union[Unset, ModelDto]):
        data (Union[Unset, Any]):
    """

    id: UUID
    is_active: bool
    request_json_response: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    topic: Union[Unset, "TopicConfigurationDto"] = UNSET
    sentiment: Union[Unset, "SentimentConfigurationDto"] = UNSET
    title: Union[Unset, "TitleConfigurationDto"] = UNSET
    default_conversational_model: Union[Unset, "ModelDto"] = UNSET
    data: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        is_active = self.is_active

        request_json_response = self.request_json_response

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        topic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topic, Unset):
            topic = self.topic.to_dict()

        sentiment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sentiment, Unset):
            sentiment = self.sentiment.to_dict()

        title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        default_conversational_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_conversational_model, Unset):
            default_conversational_model = self.default_conversational_model.to_dict()

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "isActive": is_active,
                "requestJsonResponse": request_json_response,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if topic is not UNSET:
            field_dict["topic"] = topic
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if title is not UNSET:
            field_dict["title"] = title
        if default_conversational_model is not UNSET:
            field_dict["defaultConversationalModel"] = default_conversational_model
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_dto import ModelDto
        from ..models.sentiment_configuration_dto import SentimentConfigurationDto
        from ..models.title_configuration_dto import TitleConfigurationDto
        from ..models.topic_configuration_dto import TopicConfigurationDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        is_active = d.pop("isActive")

        request_json_response = d.pop("requestJsonResponse")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _topic = d.pop("topic", UNSET)
        topic: Union[Unset, TopicConfigurationDto]
        if isinstance(_topic, Unset):
            topic = UNSET
        else:
            topic = TopicConfigurationDto.from_dict(_topic)

        _sentiment = d.pop("sentiment", UNSET)
        sentiment: Union[Unset, SentimentConfigurationDto]
        if isinstance(_sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = SentimentConfigurationDto.from_dict(_sentiment)

        _title = d.pop("title", UNSET)
        title: Union[Unset, TitleConfigurationDto]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = TitleConfigurationDto.from_dict(_title)

        _default_conversational_model = d.pop("defaultConversationalModel", UNSET)
        default_conversational_model: Union[Unset, ModelDto]
        if isinstance(_default_conversational_model, Unset):
            default_conversational_model = UNSET
        else:
            default_conversational_model = ModelDto.from_dict(_default_conversational_model)

        data = d.pop("data", UNSET)

        room_configuration_dto = cls(
            id=id,
            is_active=is_active,
            request_json_response=request_json_response,
            created_at=created_at,
            updated_at=updated_at,
            topic=topic,
            sentiment=sentiment,
            title=title,
            default_conversational_model=default_conversational_model,
            data=data,
        )

        return room_configuration_dto
