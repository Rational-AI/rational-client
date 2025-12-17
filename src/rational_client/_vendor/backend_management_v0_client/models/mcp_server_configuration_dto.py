import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_configuration_dto_configuration import McpServerConfigurationDtoConfiguration
    from ..models.mcp_server_tool_dto import McpServerToolDto
    from ..models.source_dto import SourceDto


T = TypeVar("T", bound="McpServerConfigurationDto")


@_attrs_define
class McpServerConfigurationDto:
    """
    Attributes:
        id (UUID):
        name (str):
        is_default (bool):
        mcp_server_id (UUID):
        mcp_server_name (str):
        configuration (McpServerConfigurationDtoConfiguration):
        sources (list['SourceDto']):
        tools (list['McpServerToolDto']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        mcp_server_extension_icon (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    is_default: bool
    mcp_server_id: UUID
    mcp_server_name: str
    configuration: "McpServerConfigurationDtoConfiguration"
    sources: list["SourceDto"]
    tools: list["McpServerToolDto"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    mcp_server_extension_icon: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        is_default = self.is_default

        mcp_server_id = str(self.mcp_server_id)

        mcp_server_name = self.mcp_server_name

        configuration = self.configuration.to_dict()

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        mcp_server_extension_icon: Union[None, Unset, str]
        if isinstance(self.mcp_server_extension_icon, Unset):
            mcp_server_extension_icon = UNSET
        else:
            mcp_server_extension_icon = self.mcp_server_extension_icon

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "isDefault": is_default,
                "mcpServerId": mcp_server_id,
                "mcpServerName": mcp_server_name,
                "configuration": configuration,
                "sources": sources,
                "tools": tools,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if mcp_server_extension_icon is not UNSET:
            field_dict["mcpServerExtensionIcon"] = mcp_server_extension_icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_server_configuration_dto_configuration import McpServerConfigurationDtoConfiguration
        from ..models.mcp_server_tool_dto import McpServerToolDto
        from ..models.source_dto import SourceDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        is_default = d.pop("isDefault")

        mcp_server_id = UUID(d.pop("mcpServerId"))

        mcp_server_name = d.pop("mcpServerName")

        configuration = McpServerConfigurationDtoConfiguration.from_dict(d.pop("configuration"))

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceDto.from_dict(sources_item_data)

            sources.append(sources_item)

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = McpServerToolDto.from_dict(tools_item_data)

            tools.append(tools_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_mcp_server_extension_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mcp_server_extension_icon = _parse_mcp_server_extension_icon(d.pop("mcpServerExtensionIcon", UNSET))

        mcp_server_configuration_dto = cls(
            id=id,
            name=name,
            is_default=is_default,
            mcp_server_id=mcp_server_id,
            mcp_server_name=mcp_server_name,
            configuration=configuration,
            sources=sources,
            tools=tools,
            created_at=created_at,
            updated_at=updated_at,
            mcp_server_extension_icon=mcp_server_extension_icon,
        )

        return mcp_server_configuration_dto
