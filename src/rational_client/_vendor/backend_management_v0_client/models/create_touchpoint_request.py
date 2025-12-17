from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sentiment_configuration_dto import SentimentConfigurationDto
    from ..models.title_configuration_dto import TitleConfigurationDto
    from ..models.topic_configuration_dto import TopicConfigurationDto


T = TypeVar("T", bound="CreateTouchpointRequest")


@_attrs_define
class CreateTouchpointRequest:
    """
    Attributes:
        name (str):
        description (str):
        default_model_id (UUID):
        model_ids (list[UUID]):
        channel_id (UUID):
        source_ids (list[UUID]):
        icon (Union[None, Unset, str]):
        model_prompt (Union[None, Unset, str]):
        is_enabled (Union[None, Unset, bool]):
        allow_anonymous (Union[None, Unset, bool]):
        override_title_configuration (Union[Unset, TitleConfigurationDto]):
        override_topic_configuration (Union[Unset, TopicConfigurationDto]):
        override_sentiment_configuration (Union[Unset, SentimentConfigurationDto]):
        enable_questions (Union[None, Unset, bool]):
        questions (Union[None, Unset, list[str]]):
    """

    name: str
    description: str
    default_model_id: UUID
    model_ids: list[UUID]
    channel_id: UUID
    source_ids: list[UUID]
    icon: Union[None, Unset, str] = UNSET
    model_prompt: Union[None, Unset, str] = UNSET
    is_enabled: Union[None, Unset, bool] = UNSET
    allow_anonymous: Union[None, Unset, bool] = UNSET
    override_title_configuration: Union[Unset, "TitleConfigurationDto"] = UNSET
    override_topic_configuration: Union[Unset, "TopicConfigurationDto"] = UNSET
    override_sentiment_configuration: Union[Unset, "SentimentConfigurationDto"] = UNSET
    enable_questions: Union[None, Unset, bool] = UNSET
    questions: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        default_model_id = str(self.default_model_id)

        model_ids = []
        for model_ids_item_data in self.model_ids:
            model_ids_item = str(model_ids_item_data)
            model_ids.append(model_ids_item)

        channel_id = str(self.channel_id)

        source_ids = []
        for source_ids_item_data in self.source_ids:
            source_ids_item = str(source_ids_item_data)
            source_ids.append(source_ids_item)

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

        is_enabled: Union[None, Unset, bool]
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        allow_anonymous: Union[None, Unset, bool]
        if isinstance(self.allow_anonymous, Unset):
            allow_anonymous = UNSET
        else:
            allow_anonymous = self.allow_anonymous

        override_title_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_title_configuration, Unset):
            override_title_configuration = self.override_title_configuration.to_dict()

        override_topic_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_topic_configuration, Unset):
            override_topic_configuration = self.override_topic_configuration.to_dict()

        override_sentiment_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.override_sentiment_configuration, Unset):
            override_sentiment_configuration = self.override_sentiment_configuration.to_dict()

        enable_questions: Union[None, Unset, bool]
        if isinstance(self.enable_questions, Unset):
            enable_questions = UNSET
        else:
            enable_questions = self.enable_questions

        questions: Union[None, Unset, list[str]]
        if isinstance(self.questions, Unset):
            questions = UNSET
        elif isinstance(self.questions, list):
            questions = self.questions

        else:
            questions = self.questions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "description": description,
                "defaultModelId": default_model_id,
                "modelIds": model_ids,
                "channelId": channel_id,
                "sourceIds": source_ids,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if model_prompt is not UNSET:
            field_dict["modelPrompt"] = model_prompt
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if allow_anonymous is not UNSET:
            field_dict["allowAnonymous"] = allow_anonymous
        if override_title_configuration is not UNSET:
            field_dict["overrideTitleConfiguration"] = override_title_configuration
        if override_topic_configuration is not UNSET:
            field_dict["overrideTopicConfiguration"] = override_topic_configuration
        if override_sentiment_configuration is not UNSET:
            field_dict["overrideSentimentConfiguration"] = override_sentiment_configuration
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
        name = d.pop("name")

        description = d.pop("description")

        default_model_id = UUID(d.pop("defaultModelId"))

        model_ids = []
        _model_ids = d.pop("modelIds")
        for model_ids_item_data in _model_ids:
            model_ids_item = UUID(model_ids_item_data)

            model_ids.append(model_ids_item)

        channel_id = UUID(d.pop("channelId"))

        source_ids = []
        _source_ids = d.pop("sourceIds")
        for source_ids_item_data in _source_ids:
            source_ids_item = UUID(source_ids_item_data)

            source_ids.append(source_ids_item)

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

        def _parse_is_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        def _parse_allow_anonymous(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_anonymous = _parse_allow_anonymous(d.pop("allowAnonymous", UNSET))

        _override_title_configuration = d.pop("overrideTitleConfiguration", UNSET)
        override_title_configuration: Union[Unset, TitleConfigurationDto]
        if isinstance(_override_title_configuration, Unset):
            override_title_configuration = UNSET
        else:
            override_title_configuration = TitleConfigurationDto.from_dict(_override_title_configuration)

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

        def _parse_enable_questions(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_questions = _parse_enable_questions(d.pop("enableQuestions", UNSET))

        def _parse_questions(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                questions_type_0 = cast(list[str], data)

                return questions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        questions = _parse_questions(d.pop("questions", UNSET))

        create_touchpoint_request = cls(
            name=name,
            description=description,
            default_model_id=default_model_id,
            model_ids=model_ids,
            channel_id=channel_id,
            source_ids=source_ids,
            icon=icon,
            model_prompt=model_prompt,
            is_enabled=is_enabled,
            allow_anonymous=allow_anonymous,
            override_title_configuration=override_title_configuration,
            override_topic_configuration=override_topic_configuration,
            override_sentiment_configuration=override_sentiment_configuration,
            enable_questions=enable_questions,
            questions=questions,
        )

        return create_touchpoint_request
