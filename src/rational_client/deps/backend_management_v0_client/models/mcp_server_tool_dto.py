from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_tool_dto_default_configuration import McpServerToolDtoDefaultConfiguration


T = TypeVar("T", bound="McpServerToolDto")


@_attrs_define
class McpServerToolDto:
    """
    Attributes:
        id (UUID):
        name (str):
        input_schema (Any):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        enabled (bool):
        mcp_server_configuration_id (UUID):
        mcp_server_configuration_name (str):
        mcp_server_name (str):
        default_configuration (McpServerToolDtoDefaultConfiguration):
        title (None | str | Unset):
        description (None | str | Unset):
        output_schema (Any | Unset):
        mcp_server_extension_icon (None | str | Unset):
    """

    id: UUID
    name: str
    input_schema: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    enabled: bool
    mcp_server_configuration_id: UUID
    mcp_server_configuration_name: str
    mcp_server_name: str
    default_configuration: McpServerToolDtoDefaultConfiguration
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    output_schema: Any | Unset = UNSET
    mcp_server_extension_icon: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        input_schema = self.input_schema

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        enabled = self.enabled

        mcp_server_configuration_id = str(self.mcp_server_configuration_id)

        mcp_server_configuration_name = self.mcp_server_configuration_name

        mcp_server_name = self.mcp_server_name

        default_configuration = self.default_configuration.to_dict()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        output_schema = self.output_schema

        mcp_server_extension_icon: None | str | Unset
        if isinstance(self.mcp_server_extension_icon, Unset):
            mcp_server_extension_icon = UNSET
        else:
            mcp_server_extension_icon = self.mcp_server_extension_icon

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "inputSchema": input_schema,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "enabled": enabled,
                "mcpServerConfigurationId": mcp_server_configuration_id,
                "mcpServerConfigurationName": mcp_server_configuration_name,
                "mcpServerName": mcp_server_name,
                "defaultConfiguration": default_configuration,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if output_schema is not UNSET:
            field_dict["outputSchema"] = output_schema
        if mcp_server_extension_icon is not UNSET:
            field_dict["mcpServerExtensionIcon"] = mcp_server_extension_icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_server_tool_dto_default_configuration import McpServerToolDtoDefaultConfiguration

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        input_schema = d.pop("inputSchema")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        enabled = d.pop("enabled")

        mcp_server_configuration_id = UUID(d.pop("mcpServerConfigurationId"))

        mcp_server_configuration_name = d.pop("mcpServerConfigurationName")

        mcp_server_name = d.pop("mcpServerName")

        default_configuration = McpServerToolDtoDefaultConfiguration.from_dict(d.pop("defaultConfiguration"))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        output_schema = d.pop("outputSchema", UNSET)

        def _parse_mcp_server_extension_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcp_server_extension_icon = _parse_mcp_server_extension_icon(d.pop("mcpServerExtensionIcon", UNSET))

        mcp_server_tool_dto = cls(
            id=id,
            name=name,
            input_schema=input_schema,
            created_at=created_at,
            updated_at=updated_at,
            enabled=enabled,
            mcp_server_configuration_id=mcp_server_configuration_id,
            mcp_server_configuration_name=mcp_server_configuration_name,
            mcp_server_name=mcp_server_name,
            default_configuration=default_configuration,
            title=title,
            description=description,
            output_schema=output_schema,
            mcp_server_extension_icon=mcp_server_extension_icon,
        )

        return mcp_server_tool_dto
