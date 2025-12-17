import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extension_channel_provider import ExtensionChannelProvider
    from ..models.extension_mcp_server_provider import ExtensionMcpServerProvider
    from ..models.mcp_server_dto import McpServerDto


T = TypeVar("T", bound="ExtensionDto")


@_attrs_define
class ExtensionDto:
    """
    Attributes:
        id (UUID):
        name (str):
        description (str):
        version (str):
        mcp_servers (list['McpServerDto']):
        channel_providers (list['ExtensionChannelProvider']):
        mcp_server_providers (list['ExtensionMcpServerProvider']):
        is_enabled (bool):
        installed (bool):
        number_of_channels (int):
        number_of_tools (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        extensions_registry_id (Union[None, Unset, str]):
        icon (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    description: str
    version: str
    mcp_servers: list["McpServerDto"]
    channel_providers: list["ExtensionChannelProvider"]
    mcp_server_providers: list["ExtensionMcpServerProvider"]
    is_enabled: bool
    installed: bool
    number_of_channels: int
    number_of_tools: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    extensions_registry_id: Union[None, Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        version = self.version

        mcp_servers = []
        for mcp_servers_item_data in self.mcp_servers:
            mcp_servers_item = mcp_servers_item_data.to_dict()
            mcp_servers.append(mcp_servers_item)

        channel_providers = []
        for channel_providers_item_data in self.channel_providers:
            channel_providers_item = channel_providers_item_data.to_dict()
            channel_providers.append(channel_providers_item)

        mcp_server_providers = []
        for mcp_server_providers_item_data in self.mcp_server_providers:
            mcp_server_providers_item = mcp_server_providers_item_data.to_dict()
            mcp_server_providers.append(mcp_server_providers_item)

        is_enabled = self.is_enabled

        installed = self.installed

        number_of_channels = self.number_of_channels

        number_of_tools = self.number_of_tools

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        extensions_registry_id: Union[None, Unset, str]
        if isinstance(self.extensions_registry_id, Unset):
            extensions_registry_id = UNSET
        else:
            extensions_registry_id = self.extensions_registry_id

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "version": version,
                "mcpServers": mcp_servers,
                "channelProviders": channel_providers,
                "mcpServerProviders": mcp_server_providers,
                "isEnabled": is_enabled,
                "installed": installed,
                "numberOfChannels": number_of_channels,
                "numberOfTools": number_of_tools,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if extensions_registry_id is not UNSET:
            field_dict["extensionsRegistryId"] = extensions_registry_id
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extension_channel_provider import ExtensionChannelProvider
        from ..models.extension_mcp_server_provider import ExtensionMcpServerProvider
        from ..models.mcp_server_dto import McpServerDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        version = d.pop("version")

        mcp_servers = []
        _mcp_servers = d.pop("mcpServers")
        for mcp_servers_item_data in _mcp_servers:
            mcp_servers_item = McpServerDto.from_dict(mcp_servers_item_data)

            mcp_servers.append(mcp_servers_item)

        channel_providers = []
        _channel_providers = d.pop("channelProviders")
        for channel_providers_item_data in _channel_providers:
            channel_providers_item = ExtensionChannelProvider.from_dict(channel_providers_item_data)

            channel_providers.append(channel_providers_item)

        mcp_server_providers = []
        _mcp_server_providers = d.pop("mcpServerProviders")
        for mcp_server_providers_item_data in _mcp_server_providers:
            mcp_server_providers_item = ExtensionMcpServerProvider.from_dict(mcp_server_providers_item_data)

            mcp_server_providers.append(mcp_server_providers_item)

        is_enabled = d.pop("isEnabled")

        installed = d.pop("installed")

        number_of_channels = d.pop("numberOfChannels")

        number_of_tools = d.pop("numberOfTools")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_extensions_registry_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extensions_registry_id = _parse_extensions_registry_id(d.pop("extensionsRegistryId", UNSET))

        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))

        extension_dto = cls(
            id=id,
            name=name,
            description=description,
            version=version,
            mcp_servers=mcp_servers,
            channel_providers=channel_providers,
            mcp_server_providers=mcp_server_providers,
            is_enabled=is_enabled,
            installed=installed,
            number_of_channels=number_of_channels,
            number_of_tools=number_of_tools,
            created_at=created_at,
            updated_at=updated_at,
            extensions_registry_id=extensions_registry_id,
            icon=icon,
        )

        return extension_dto
