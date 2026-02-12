from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.channel_mode import ChannelMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_channel_request_configuration_type_0 import CreateChannelRequestConfigurationType0


T = TypeVar("T", bound="CreateChannelRequest")


@_attrs_define
class CreateChannelRequest:
    """
    Attributes:
        extension_id (UUID):
        name (str):
        extension_channel_provider_id (str):
        channel_mode (ChannelMode):
        icon (None | str | Unset):
        configuration (CreateChannelRequestConfigurationType0 | None | Unset):
    """

    extension_id: UUID
    name: str
    extension_channel_provider_id: str
    channel_mode: ChannelMode
    icon: None | str | Unset = UNSET
    configuration: CreateChannelRequestConfigurationType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_channel_request_configuration_type_0 import CreateChannelRequestConfigurationType0

        extension_id = str(self.extension_id)

        name = self.name

        extension_channel_provider_id = self.extension_channel_provider_id

        channel_mode = self.channel_mode.value

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        configuration: dict[str, Any] | None | Unset
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, CreateChannelRequestConfigurationType0):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "extensionId": extension_id,
                "name": name,
                "extensionChannelProviderId": extension_channel_provider_id,
                "channelMode": channel_mode,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_channel_request_configuration_type_0 import CreateChannelRequestConfigurationType0

        d = dict(src_dict)
        extension_id = UUID(d.pop("extensionId"))

        name = d.pop("name")

        extension_channel_provider_id = d.pop("extensionChannelProviderId")

        channel_mode = ChannelMode(d.pop("channelMode"))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_configuration(data: object) -> CreateChannelRequestConfigurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = CreateChannelRequestConfigurationType0.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateChannelRequestConfigurationType0 | None | Unset, data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        create_channel_request = cls(
            extension_id=extension_id,
            name=name,
            extension_channel_provider_id=extension_channel_provider_id,
            channel_mode=channel_mode,
            icon=icon,
            configuration=configuration,
        )

        return create_channel_request
