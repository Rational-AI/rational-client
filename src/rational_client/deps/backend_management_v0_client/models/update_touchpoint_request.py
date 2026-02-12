from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_verification_configuration import ResponseVerificationConfiguration
    from ..models.sentiment_configuration_dto import SentimentConfigurationDto
    from ..models.title_configuration_dto import TitleConfigurationDto
    from ..models.topic_configuration_dto import TopicConfigurationDto


T = TypeVar("T", bound="UpdateTouchpointRequest")


@_attrs_define
class UpdateTouchpointRequest:
    """
    Attributes:
        name (str | Unset):
        description (str | Unset):
        icon (None | str | Unset):
        model_prompt (None | str | Unset):
        default_model_id (UUID | Unset):
        model_ids (list[UUID] | Unset):
        channel_id (UUID | Unset):
        source_ids (list[UUID] | Unset):
        is_enabled (bool | Unset):
        allow_anonymous (bool | Unset):
        override_topic_configuration (TopicConfigurationDto | Unset):
        override_sentiment_configuration (SentimentConfigurationDto | Unset):
        override_title_configuration (TitleConfigurationDto | Unset):
        response_verification (ResponseVerificationConfiguration | Unset):
        enable_questions (bool | Unset):
        questions (list[str] | Unset):
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    icon: None | str | Unset = UNSET
    model_prompt: None | str | Unset = UNSET
    default_model_id: UUID | Unset = UNSET
    model_ids: list[UUID] | Unset = UNSET
    channel_id: UUID | Unset = UNSET
    source_ids: list[UUID] | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    allow_anonymous: bool | Unset = UNSET
    override_topic_configuration: TopicConfigurationDto | Unset = UNSET
    override_sentiment_configuration: SentimentConfigurationDto | Unset = UNSET
    override_title_configuration: TitleConfigurationDto | Unset = UNSET
    response_verification: ResponseVerificationConfiguration | Unset = UNSET
    enable_questions: bool | Unset = UNSET
    questions: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        model_prompt: None | str | Unset
        if isinstance(self.model_prompt, Unset):
            model_prompt = UNSET
        else:
            model_prompt = self.model_prompt

        default_model_id: str | Unset = UNSET
        if not isinstance(self.default_model_id, Unset):
            default_model_id = str(self.default_model_id)

        model_ids: list[str] | Unset = UNSET
        if not isinstance(self.model_ids, Unset):
            model_ids = []
            for model_ids_item_data in self.model_ids:
                model_ids_item = str(model_ids_item_data)
                model_ids.append(model_ids_item)

        channel_id: str | Unset = UNSET
        if not isinstance(self.channel_id, Unset):
            channel_id = str(self.channel_id)

        source_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = []
            for source_ids_item_data in self.source_ids:
                source_ids_item = str(source_ids_item_data)
                source_ids.append(source_ids_item)

        is_enabled = self.is_enabled

        allow_anonymous = self.allow_anonymous

        override_topic_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_topic_configuration, Unset):
            override_topic_configuration = self.override_topic_configuration.to_dict()

        override_sentiment_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_sentiment_configuration, Unset):
            override_sentiment_configuration = self.override_sentiment_configuration.to_dict()

        override_title_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_title_configuration, Unset):
            override_title_configuration = self.override_title_configuration.to_dict()

        response_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_verification, Unset):
            response_verification = self.response_verification.to_dict()

        enable_questions = self.enable_questions

        questions: list[str] | Unset = UNSET
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
        if response_verification is not UNSET:
            field_dict["responseVerification"] = response_verification
        if enable_questions is not UNSET:
            field_dict["enableQuestions"] = enable_questions
        if questions is not UNSET:
            field_dict["questions"] = questions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_verification_configuration import ResponseVerificationConfiguration
        from ..models.sentiment_configuration_dto import SentimentConfigurationDto
        from ..models.title_configuration_dto import TitleConfigurationDto
        from ..models.topic_configuration_dto import TopicConfigurationDto

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_model_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_prompt = _parse_model_prompt(d.pop("modelPrompt", UNSET))

        _default_model_id = d.pop("defaultModelId", UNSET)
        default_model_id: UUID | Unset
        if isinstance(_default_model_id, Unset):
            default_model_id = UNSET
        else:
            default_model_id = UUID(_default_model_id)

        _model_ids = d.pop("modelIds", UNSET)
        model_ids: list[UUID] | Unset = UNSET
        if _model_ids is not UNSET:
            model_ids = []
            for model_ids_item_data in _model_ids:
                model_ids_item = UUID(model_ids_item_data)

                model_ids.append(model_ids_item)

        _channel_id = d.pop("channelId", UNSET)
        channel_id: UUID | Unset
        if isinstance(_channel_id, Unset):
            channel_id = UNSET
        else:
            channel_id = UUID(_channel_id)

        _source_ids = d.pop("sourceIds", UNSET)
        source_ids: list[UUID] | Unset = UNSET
        if _source_ids is not UNSET:
            source_ids = []
            for source_ids_item_data in _source_ids:
                source_ids_item = UUID(source_ids_item_data)

                source_ids.append(source_ids_item)

        is_enabled = d.pop("isEnabled", UNSET)

        allow_anonymous = d.pop("allowAnonymous", UNSET)

        _override_topic_configuration = d.pop("overrideTopicConfiguration", UNSET)
        override_topic_configuration: TopicConfigurationDto | Unset
        if isinstance(_override_topic_configuration, Unset):
            override_topic_configuration = UNSET
        else:
            override_topic_configuration = TopicConfigurationDto.from_dict(_override_topic_configuration)

        _override_sentiment_configuration = d.pop("overrideSentimentConfiguration", UNSET)
        override_sentiment_configuration: SentimentConfigurationDto | Unset
        if isinstance(_override_sentiment_configuration, Unset):
            override_sentiment_configuration = UNSET
        else:
            override_sentiment_configuration = SentimentConfigurationDto.from_dict(_override_sentiment_configuration)

        _override_title_configuration = d.pop("overrideTitleConfiguration", UNSET)
        override_title_configuration: TitleConfigurationDto | Unset
        if isinstance(_override_title_configuration, Unset):
            override_title_configuration = UNSET
        else:
            override_title_configuration = TitleConfigurationDto.from_dict(_override_title_configuration)

        _response_verification = d.pop("responseVerification", UNSET)
        response_verification: ResponseVerificationConfiguration | Unset
        if isinstance(_response_verification, Unset):
            response_verification = UNSET
        else:
            response_verification = ResponseVerificationConfiguration.from_dict(_response_verification)

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
            response_verification=response_verification,
            enable_questions=enable_questions,
            questions=questions,
        )

        return update_touchpoint_request
