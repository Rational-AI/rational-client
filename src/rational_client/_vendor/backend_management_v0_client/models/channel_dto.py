from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.channel_mode import ChannelMode
from ..models.extension_channel_type import ExtensionChannelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_dto_configuration import ChannelDtoConfiguration


T = TypeVar("T", bound="ChannelDto")


@_attrs_define
class ChannelDto:
    """
    Attributes:
        id (UUID):
        name (str):
        extension_channel_provider_id (str):
        mode (ChannelMode):
        type_ (ExtensionChannelType):
        configuration (ChannelDtoConfiguration):
        description (Union[None, Unset, str]):
        icon (Union[None, Unset, str]):
        extension_id (Union[None, UUID, Unset]):
    """

    id: UUID
    name: str
    extension_channel_provider_id: str
    mode: ChannelMode
    type_: ExtensionChannelType
    configuration: "ChannelDtoConfiguration"
    description: Union[None, Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET
    extension_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        extension_channel_provider_id = self.extension_channel_provider_id

        mode = self.mode.value

        type_ = self.type_.value

        configuration = self.configuration.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        extension_id: Union[None, Unset, str]
        if isinstance(self.extension_id, Unset):
            extension_id = UNSET
        elif isinstance(self.extension_id, UUID):
            extension_id = str(self.extension_id)
        else:
            extension_id = self.extension_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "extensionChannelProviderId": extension_channel_provider_id,
                "mode": mode,
                "type": type_,
                "configuration": configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if extension_id is not UNSET:
            field_dict["extensionId"] = extension_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_dto_configuration import ChannelDtoConfiguration

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        extension_channel_provider_id = d.pop("extensionChannelProviderId")

        mode = ChannelMode(d.pop("mode"))

        type_ = ExtensionChannelType(d.pop("type"))

        configuration = ChannelDtoConfiguration.from_dict(d.pop("configuration"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))

        def _parse_extension_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                extension_id_type_0 = UUID(data)

                return extension_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        extension_id = _parse_extension_id(d.pop("extensionId", UNSET))

        channel_dto = cls(
            id=id,
            name=name,
            extension_channel_provider_id=extension_channel_provider_id,
            mode=mode,
            type_=type_,
            configuration=configuration,
            description=description,
            icon=icon,
            extension_id=extension_id,
        )

        return channel_dto
