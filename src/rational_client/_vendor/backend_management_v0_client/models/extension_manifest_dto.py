from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extension_channel_provider import ExtensionChannelProvider
    from ..models.extension_manifest_dto_environment_type_0 import ExtensionManifestDtoEnvironmentType0
    from ..models.extension_mcp_server_provider import ExtensionMcpServerProvider
    from ..models.extension_registry_tool import ExtensionRegistryTool


T = TypeVar("T", bound="ExtensionManifestDto")


@_attrs_define
class ExtensionManifestDto:
    """
    Attributes:
        id (str):
        name_identifier (str):
        version (str):
        name (str):
        channel_providers (list['ExtensionChannelProvider']):
        tools (list['ExtensionRegistryTool']):
        number_of_tools (int):
        number_of_channels (int):
        number_of_sources (int):
        mcp_server_providers (list['ExtensionMcpServerProvider']):
        description (Union[None, Unset, str]):
        icon (Union[None, Unset, str]):
        content_type (Union[None, Unset, str]):
        environment (Union['ExtensionManifestDtoEnvironmentType0', None, Unset]):
    """

    id: str
    name_identifier: str
    version: str
    name: str
    channel_providers: list["ExtensionChannelProvider"]
    tools: list["ExtensionRegistryTool"]
    number_of_tools: int
    number_of_channels: int
    number_of_sources: int
    mcp_server_providers: list["ExtensionMcpServerProvider"]
    description: Union[None, Unset, str] = UNSET
    icon: Union[None, Unset, str] = UNSET
    content_type: Union[None, Unset, str] = UNSET
    environment: Union["ExtensionManifestDtoEnvironmentType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.extension_manifest_dto_environment_type_0 import ExtensionManifestDtoEnvironmentType0

        id = self.id

        name_identifier = self.name_identifier

        version = self.version

        name = self.name

        channel_providers = []
        for channel_providers_item_data in self.channel_providers:
            channel_providers_item = channel_providers_item_data.to_dict()
            channel_providers.append(channel_providers_item)

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        number_of_tools = self.number_of_tools

        number_of_channels = self.number_of_channels

        number_of_sources = self.number_of_sources

        mcp_server_providers = []
        for mcp_server_providers_item_data in self.mcp_server_providers:
            mcp_server_providers_item = mcp_server_providers_item_data.to_dict()
            mcp_server_providers.append(mcp_server_providers_item)

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

        content_type: Union[None, Unset, str]
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        environment: Union[None, Unset, dict[str, Any]]
        if isinstance(self.environment, Unset):
            environment = UNSET
        elif isinstance(self.environment, ExtensionManifestDtoEnvironmentType0):
            environment = self.environment.to_dict()
        else:
            environment = self.environment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "nameIdentifier": name_identifier,
                "version": version,
                "name": name,
                "channelProviders": channel_providers,
                "tools": tools,
                "numberOfTools": number_of_tools,
                "numberOfChannels": number_of_channels,
                "numberOfSources": number_of_sources,
                "mcpServerProviders": mcp_server_providers,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if environment is not UNSET:
            field_dict["environment"] = environment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extension_channel_provider import ExtensionChannelProvider
        from ..models.extension_manifest_dto_environment_type_0 import ExtensionManifestDtoEnvironmentType0
        from ..models.extension_mcp_server_provider import ExtensionMcpServerProvider
        from ..models.extension_registry_tool import ExtensionRegistryTool

        d = dict(src_dict)
        id = d.pop("id")

        name_identifier = d.pop("nameIdentifier")

        version = d.pop("version")

        name = d.pop("name")

        channel_providers = []
        _channel_providers = d.pop("channelProviders")
        for channel_providers_item_data in _channel_providers:
            channel_providers_item = ExtensionChannelProvider.from_dict(channel_providers_item_data)

            channel_providers.append(channel_providers_item)

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = ExtensionRegistryTool.from_dict(tools_item_data)

            tools.append(tools_item)

        number_of_tools = d.pop("numberOfTools")

        number_of_channels = d.pop("numberOfChannels")

        number_of_sources = d.pop("numberOfSources")

        mcp_server_providers = []
        _mcp_server_providers = d.pop("mcpServerProviders")
        for mcp_server_providers_item_data in _mcp_server_providers:
            mcp_server_providers_item = ExtensionMcpServerProvider.from_dict(mcp_server_providers_item_data)

            mcp_server_providers.append(mcp_server_providers_item)

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

        def _parse_content_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_type = _parse_content_type(d.pop("contentType", UNSET))

        def _parse_environment(data: object) -> Union["ExtensionManifestDtoEnvironmentType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_type_0 = ExtensionManifestDtoEnvironmentType0.from_dict(data)

                return environment_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ExtensionManifestDtoEnvironmentType0", None, Unset], data)

        environment = _parse_environment(d.pop("environment", UNSET))

        extension_manifest_dto = cls(
            id=id,
            name_identifier=name_identifier,
            version=version,
            name=name,
            channel_providers=channel_providers,
            tools=tools,
            number_of_tools=number_of_tools,
            number_of_channels=number_of_channels,
            number_of_sources=number_of_sources,
            mcp_server_providers=mcp_server_providers,
            description=description,
            icon=icon,
            content_type=content_type,
            environment=environment,
        )

        return extension_manifest_dto
