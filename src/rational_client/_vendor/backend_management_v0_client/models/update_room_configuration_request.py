from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sentiment_configuration_dto import SentimentConfigurationDto
    from ..models.title_configuration_dto import TitleConfigurationDto
    from ..models.topic_configuration_dto import TopicConfigurationDto


T = TypeVar("T", bound="UpdateRoomConfigurationRequest")


@_attrs_define
class UpdateRoomConfigurationRequest:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        request_json_response (Union[Unset, bool]):
        data (Union[Unset, Any]):
        default_conversational_model_id (Union[None, UUID, Unset]):
        title (Union[Unset, TitleConfigurationDto]):
        topic (Union[Unset, TopicConfigurationDto]):
        sentiment (Union[Unset, SentimentConfigurationDto]):
    """

    is_active: Union[Unset, bool] = UNSET
    request_json_response: Union[Unset, bool] = UNSET
    data: Union[Unset, Any] = UNSET
    default_conversational_model_id: Union[None, UUID, Unset] = UNSET
    title: Union[Unset, "TitleConfigurationDto"] = UNSET
    topic: Union[Unset, "TopicConfigurationDto"] = UNSET
    sentiment: Union[Unset, "SentimentConfigurationDto"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_active = self.is_active

        request_json_response = self.request_json_response

        data = self.data

        default_conversational_model_id: Union[None, Unset, str]
        if isinstance(self.default_conversational_model_id, Unset):
            default_conversational_model_id = UNSET
        elif isinstance(self.default_conversational_model_id, UUID):
            default_conversational_model_id = str(self.default_conversational_model_id)
        else:
            default_conversational_model_id = self.default_conversational_model_id

        title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        topic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topic, Unset):
            topic = self.topic.to_dict()

        sentiment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sentiment, Unset):
            sentiment = self.sentiment.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if request_json_response is not UNSET:
            field_dict["requestJsonResponse"] = request_json_response
        if data is not UNSET:
            field_dict["data"] = data
        if default_conversational_model_id is not UNSET:
            field_dict["defaultConversationalModelId"] = default_conversational_model_id
        if title is not UNSET:
            field_dict["title"] = title
        if topic is not UNSET:
            field_dict["topic"] = topic
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentiment_configuration_dto import SentimentConfigurationDto
        from ..models.title_configuration_dto import TitleConfigurationDto
        from ..models.topic_configuration_dto import TopicConfigurationDto

        d = dict(src_dict)
        is_active = d.pop("isActive", UNSET)

        request_json_response = d.pop("requestJsonResponse", UNSET)

        data = d.pop("data", UNSET)

        def _parse_default_conversational_model_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_conversational_model_id_type_0 = UUID(data)

                return default_conversational_model_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        default_conversational_model_id = _parse_default_conversational_model_id(
            d.pop("defaultConversationalModelId", UNSET)
        )

        _title = d.pop("title", UNSET)
        title: Union[Unset, TitleConfigurationDto]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = TitleConfigurationDto.from_dict(_title)

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

        update_room_configuration_request = cls(
            is_active=is_active,
            request_json_response=request_json_response,
            data=data,
            default_conversational_model_id=default_conversational_model_id,
            title=title,
            topic=topic,
            sentiment=sentiment,
        )

        return update_room_configuration_request
