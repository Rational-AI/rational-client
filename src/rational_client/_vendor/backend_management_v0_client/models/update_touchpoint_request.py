from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sentiment_configuration_dto import SentimentConfigurationDto
    from ..models.title_configuration_dto import TitleConfigurationDto
    from ..models.topic_configuration_dto import TopicConfigurationDto


T = TypeVar("T", bound="UpdateTouchpointRequest")


@_attrs_define
class UpdateTouchpointRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        icon (Union[None, Unset, str]):
        model_prompt (Union[None, Unset, str]):
        default_model_id (Union[Unset, UUID]):
        model_ids (Union[Unset, list[UUID]]):
        channel_id (Union[Unset, UUID]):
        source_ids (Union[Unset, list[UUID]]):
        is_enabled (Union[Unset, bool]):
        allow_anonymous (Union[Unset, bool]):
        override_topic_configuration (Union[Unset, TopicConfigurationDto]):
        override_sentiment_configuration (Union[Unset, SentimentConfigurationDto]):
        override_title_configuration (Union[Unset, TitleConfigurationDto]):
        enable_questions (Union[Unset, bool]):
        questions (Union[Unset, list[str]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET
    model_prompt: Union[None, Unset, str] = UNSET
    default_model_id: Union[Unset, UUID] = UNSET
    model_ids: Union[Unset, list[UUID]] = UNSET
    channel_id: Union[Unset, UUID] = UNSET
    source_ids: Union[Unset, list[UUID]] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    allow_anonymous: Union[Unset, bool] = UNSET
    override_topic_configuration: Union[Unset, "TopicConfigurationDto"] = UNSET
    override_sentiment_configuration: Union[Unset, "SentimentConfigurationDto"] = UNSET
    override_title_configuration: Union[Unset, "TitleConfigurationDto"] = UNSET
    enable_questions: Union[Unset, bool] = UNSET
    questions: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        model_prompt: Union[None, Unset, str]
        if isinstance(self.model_prompt, Unset):
            model_prompt = UNSET
        else:
            model_prompt = self.model_prompt

        default_model_id: Union[Unset, str] = UNSET
        if not isinstance(self.default_model_id, Unset):
            default_model_id = str(self.default_model_id)

        model_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.model_ids, Unset):
            model_ids = []
            for model_ids_item_data in self.model_ids:
                model_ids_item = str(model_ids_item_data)
                model_ids.append(model_ids_item)

        channel_id: Union[Unset, str] = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        source_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = []
            for source_ids_item_data in self.source_ids:
                source_ids_item = str(source_ids_item_data)
                source_ids.append(source_ids_item)

        is_enabled = self.is_enabled

        allow_anonymous = self.allow_anonymous

        override_topic_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_topic_configuration, Unset):
            override_topic_configuration = self.override_topic_configuration.to_dict()

        override_sentiment_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_sentiment_configuration, Unset):
            override_sentiment_configuration = self.override_sentiment_configuration.to_dict()

        override_title_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_title_configuration, Unset):
            override_title_configuration = self.override_title_configuration.to_dict()

        enable_questions = self.enable_questions

        questions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.questions, Unset):
            questions = self.questions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if model_prompt is not UNSET:
            field_dict["modelPrompt"] = model_prompt
        if default_model_id is not UNSET:
            field_dict["defaultModelId"] = default_model_id
        if model_ids is not UNSET:
            field_dict["modelIds"] = model_ids
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if source_ids is not UNSET:
            field_dict["sourceIds"] = source_ids
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if allow_anonymous is not UNSET:
            field_dict["allowAnonymous"] = allow_anonymous
        if override_topic_configuration is not UNSET:
            field_dict["overrideTopicConfiguration"] = override_topic_configuration
        if override_sentiment_configuration is not UNSET:
            field_dict["overrideSentimentConfiguration"] = override_sentiment_configuration
        if override_title_configuration is not UNSET:
            field_dict["overrideTitleConfiguration"] = override_title_configuration
        if enable_questions is not UNSET:
            field_dict["enableQuestions"] = enable_questions
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentiment_configuration_dto import SentimentConfigurationDto
        from ..models.title_configuration_dto import TitleConfigurationDto
        from ..models.topic_configuration_dto import TopicConfigurationDto

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_model_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_prompt = _parse_model_prompt(d.pop("modelPrompt", UNSET))

        _default_model_id = d.pop("defaultModelId", UNSET)
        default_model_id: Union[Unset, UUID]
        if isinstance(_default_model_id, Unset):
            default_model_id = UNSET
        else:
            default_model_id = UUID(_default_model_id)

        model_ids = []
        _model_ids = d.pop("modelIds", UNSET)
        for model_ids_item_data in _model_ids or []:
            model_ids_item = UUID(model_ids_item_data)

            model_ids.append(model_ids_item)

        _channel_id = d.pop("channelId", UNSET)
        channel_id: Union[Unset, UUID]
        if isinstance(_channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)

        source_ids = []
        _source_ids = d.pop("sourceIds", UNSET)
        for source_ids_item_data in _source_ids or []:
            source_ids_item = UUID(source_ids_item_data)

            source_ids.append(source_ids_item)

        is_enabled = d.pop("isEnabled", UNSET)

        allow_anonymous = d.pop("allowAnonymous", UNSET)

        _override_topic_configuration = d.pop("overrideTopicConfiguration", UNSET)
        override_topic_configuration: Union[Unset, TopicConfigurationDto]
        if isinstance(_override_topic_configuration, Unset):
            override_topic_configuration = UNSET
        else:
            override_topic_configuration = TopicConfigurationDto.from_dict(_override_topic_configuration)

        _override_sentiment_configuration = d.pop("overrideSentimentConfiguration", UNSET)
        override_sentiment_configuration: Union[Unset, SentimentConfigurationDto]
        if isinstance(_override_sentiment_configuration, Unset):
            override_sentiment_configuration = UNSET
        else:
            override_sentiment_configuration = SentimentConfigurationDto.from_dict(_override_sentiment_configuration)

        _override_title_configuration = d.pop("overrideTitleConfiguration", UNSET)
        override_title_configuration: Union[Unset, TitleConfigurationDto]
        if isinstance(_override_title_configuration, Unset):
            override_title_configuration = UNSET
        else:
            override_title_configuration = TitleConfigurationDto.from_dict(_override_title_configuration)

        enable_questions = d.pop("enableQuestions", UNSET)

        questions = cast(list[str], d.pop("questions", UNSET))

        update_touchpoint_request = cls(
            name=name,
            description=description,
            icon=icon,
            model_prompt=model_prompt,
            default_model_id=default_model_id,
            model_ids=model_ids,
            channel_id=channel_id,
            source_ids=source_ids,
            is_enabled=is_enabled,
            allow_anonymous=allow_anonymous,
            override_topic_configuration=override_topic_configuration,
            override_sentiment_configuration=override_sentiment_configuration,
            override_title_configuration=override_title_configuration,
            enable_questions=enable_questions,
            questions=questions,
        )

        return update_touchpoint_request
