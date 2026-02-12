from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_dto import ChannelDto
    from ..models.group_dto import GroupDto
    from ..models.model_dto import ModelDto
    from ..models.response_verification_configuration import ResponseVerificationConfiguration
    from ..models.sentiment_configuration_dto import SentimentConfigurationDto
    from ..models.title_configuration_dto import TitleConfigurationDto
    from ..models.topic_configuration_dto import TopicConfigurationDto
    from ..models.touchpoint_source_dto import TouchpointSourceDto
    from ..models.touchpoint_tool_dto import TouchpointToolDto
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="TouchpointDto")


@_attrs_define
class TouchpointDto:
    """
    Attributes:
        id (UUID):
        name (str):
        description (str):
        models (list[ModelDto]):
        channel (ChannelDto):
        is_enabled (bool):
        sources (list[TouchpointSourceDto]):
        users_permission (list[UserDto]):
        groups_permission (list[GroupDto]):
        allow_anonymous (bool):
        touchpoint_tools (list[TouchpointToolDto]):
        enable_questions (bool):
        questions (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        icon (None | str | Unset):
        default_model (ModelDto | Unset):
        model_prompt (None | str | Unset):
        override_title_configuration (TitleConfigurationDto | Unset):
        override_topic_configuration (TopicConfigurationDto | Unset):
        override_sentiment_configuration (SentimentConfigurationDto | Unset):
        response_verification (ResponseVerificationConfiguration | Unset):
    """

    id: UUID
    name: str
    description: str
    models: list[ModelDto]
    channel: ChannelDto
    is_enabled: bool
    sources: list[TouchpointSourceDto]
    users_permission: list[UserDto]
    groups_permission: list[GroupDto]
    allow_anonymous: bool
    touchpoint_tools: list[TouchpointToolDto]
    enable_questions: bool
    questions: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    icon: None | str | Unset = UNSET
    default_model: ModelDto | Unset = UNSET
    model_prompt: None | str | Unset = UNSET
    override_title_configuration: TitleConfigurationDto | Unset = UNSET
    override_topic_configuration: TopicConfigurationDto | Unset = UNSET
    override_sentiment_configuration: SentimentConfigurationDto | Unset = UNSET
    response_verification: ResponseVerificationConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        channel = self.channel.to_dict()

        is_enabled = self.is_enabled

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        users_permission = []
        for users_permission_item_data in self.users_permission:
            users_permission_item = users_permission_item_data.to_dict()
            users_permission.append(users_permission_item)

        groups_permission = []
        for groups_permission_item_data in self.groups_permission:
            groups_permission_item = groups_permission_item_data.to_dict()
            groups_permission.append(groups_permission_item)

        allow_anonymous = self.allow_anonymous

        touchpoint_tools = []
        for touchpoint_tools_item_data in self.touchpoint_tools:
            touchpoint_tools_item = touchpoint_tools_item_data.to_dict()
            touchpoint_tools.append(touchpoint_tools_item)

        enable_questions = self.enable_questions

        questions = self.questions

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        default_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_model, Unset):
            default_model = self.default_model.to_dict()

        model_prompt: None | str | Unset
        if isinstance(self.model_prompt, Unset):
            model_prompt = UNSET
        else:
            model_prompt = self.model_prompt

        override_title_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_title_configuration, Unset):
            override_title_configuration = self.override_title_configuration.to_dict()

        override_topic_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_topic_configuration, Unset):
            override_topic_configuration = self.override_topic_configuration.to_dict()

        override_sentiment_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_sentiment_configuration, Unset):
            override_sentiment_configuration = self.override_sentiment_configuration.to_dict()

        response_verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_verification, Unset):
            response_verification = self.response_verification.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "models": models,
                "channel": channel,
                "isEnabled": is_enabled,
                "sources": sources,
                "usersPermission": users_permission,
                "groupsPermission": groups_permission,
                "allowAnonymous": allow_anonymous,
                "touchpointTools": touchpoint_tools,
                "enableQuestions": enable_questions,
                "questions": questions,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if default_model is not UNSET:
            field_dict["defaultModel"] = default_model
        if model_prompt is not UNSET:
            field_dict["modelPrompt"] = model_prompt
        if override_title_configuration is not UNSET:
            field_dict["overrideTitleConfiguration"] = override_title_configuration
        if override_topic_configuration is not UNSET:
            field_dict["overrideTopicConfiguration"] = override_topic_configuration
        if override_sentiment_configuration is not UNSET:
            field_dict["overrideSentimentConfiguration"] = override_sentiment_configuration
        if response_verification is not UNSET:
            field_dict["responseVerification"] = response_verification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_dto import ChannelDto
        from ..models.group_dto import GroupDto
        from ..models.model_dto import ModelDto
        from ..models.response_verification_configuration import ResponseVerificationConfiguration
        from ..models.sentiment_configuration_dto import SentimentConfigurationDto
        from ..models.title_configuration_dto import TitleConfigurationDto
        from ..models.topic_configuration_dto import TopicConfigurationDto
        from ..models.touchpoint_source_dto import TouchpointSourceDto
        from ..models.touchpoint_tool_dto import TouchpointToolDto
        from ..models.user_dto import UserDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = ModelDto.from_dict(models_item_data)

            models.append(models_item)

        channel = ChannelDto.from_dict(d.pop("channel"))

        is_enabled = d.pop("isEnabled")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = TouchpointSourceDto.from_dict(sources_item_data)

            sources.append(sources_item)

        users_permission = []
        _users_permission = d.pop("usersPermission")
        for users_permission_item_data in _users_permission:
            users_permission_item = UserDto.from_dict(users_permission_item_data)

            users_permission.append(users_permission_item)

        groups_permission = []
        _groups_permission = d.pop("groupsPermission")
        for groups_permission_item_data in _groups_permission:
            groups_permission_item = GroupDto.from_dict(groups_permission_item_data)

            groups_permission.append(groups_permission_item)

        allow_anonymous = d.pop("allowAnonymous")

        touchpoint_tools = []
        _touchpoint_tools = d.pop("touchpointTools")
        for touchpoint_tools_item_data in _touchpoint_tools:
            touchpoint_tools_item = TouchpointToolDto.from_dict(touchpoint_tools_item_data)

            touchpoint_tools.append(touchpoint_tools_item)

        enable_questions = d.pop("enableQuestions")

        questions = cast(list[str], d.pop("questions"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        _default_model = d.pop("defaultModel", UNSET)
        default_model: ModelDto | Unset
        if isinstance(_default_model, Unset):
            default_model = UNSET
        else:
            default_model = ModelDto.from_dict(_default_model)

        def _parse_model_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_prompt = _parse_model_prompt(d.pop("modelPrompt", UNSET))

        _override_title_configuration = d.pop("overrideTitleConfiguration", UNSET)
        override_title_configuration: TitleConfigurationDto | Unset
        if isinstance(_override_title_configuration, Unset):
            override_title_configuration = UNSET
        else:
            override_title_configuration = TitleConfigurationDto.from_dict(_override_title_configuration)

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

        _response_verification = d.pop("responseVerification", UNSET)
        response_verification: ResponseVerificationConfiguration | Unset
        if isinstance(_response_verification, Unset):
            response_verification = UNSET
        else:
            response_verification = ResponseVerificationConfiguration.from_dict(_response_verification)

        touchpoint_dto = cls(
            id=id,
            name=name,
            description=description,
            models=models,
            channel=channel,
            is_enabled=is_enabled,
            sources=sources,
            users_permission=users_permission,
            groups_permission=groups_permission,
            allow_anonymous=allow_anonymous,
            touchpoint_tools=touchpoint_tools,
            enable_questions=enable_questions,
            questions=questions,
            created_at=created_at,
            updated_at=updated_at,
            icon=icon,
            default_model=default_model,
            model_prompt=model_prompt,
            override_title_configuration=override_title_configuration,
            override_topic_configuration=override_topic_configuration,
            override_sentiment_configuration=override_sentiment_configuration,
            response_verification=response_verification,
        )

        return touchpoint_dto
