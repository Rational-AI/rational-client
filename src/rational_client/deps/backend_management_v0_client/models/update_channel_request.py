from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.channel_mode import ChannelMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_channel_request_configuration import UpdateChannelRequestConfiguration


T = TypeVar("T", bound="UpdateChannelRequest")


@_attrs_define
class UpdateChannelRequest:
    """
    Attributes:
        name (str):
        channel_mode (ChannelMode):
        configuration (UpdateChannelRequestConfiguration):
        description (None | str | Unset):
        icon (None | str | Unset):
    """

    name: str
    channel_mode: ChannelMode
    configuration: UpdateChannelRequestConfiguration
    description: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        channel_mode = self.channel_mode.value

        configuration = self.configuration.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "channelMode": channel_mode,
                "configuration": configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_channel_request_configuration import UpdateChannelRequestConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        channel_mode = ChannelMode(d.pop("channelMode"))

        configuration = UpdateChannelRequestConfiguration.from_dict(d.pop("configuration"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        update_channel_request = cls(
            name=name,
            channel_mode=channel_mode,
            configuration=configuration,
            description=description,
            icon=icon,
        )

        return update_channel_request
