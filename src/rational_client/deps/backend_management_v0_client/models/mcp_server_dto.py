from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_configuration_dto import McpServerConfigurationDto
    from ..models.mcp_server_dto_default_configuration_type_0 import McpServerDtoDefaultConfigurationType0


T = TypeVar("T", bound="McpServerDto")


@_attrs_define
class McpServerDto:
    """
    Attributes:
        id (UUID):
        name (str):
        command (str):
        arguments (list[str]):
        tools_count (int):
        mcp_server_configurations (list[McpServerConfigurationDto]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        install_script (None | str | Unset):
        uninstall_script (None | str | Unset):
        before_call_script (None | str | Unset):
        allowed_sources (list[SourceType] | None | Unset):
        after_call_script (None | str | Unset):
        default_configuration (McpServerDtoDefaultConfigurationType0 | None | Unset):
    """

    id: UUID
    name: str
    command: str
    arguments: list[str]
    tools_count: int
    mcp_server_configurations: list[McpServerConfigurationDto]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    install_script: None | str | Unset = UNSET
    uninstall_script: None | str | Unset = UNSET
    before_call_script: None | str | Unset = UNSET
    allowed_sources: list[SourceType] | None | Unset = UNSET
    after_call_script: None | str | Unset = UNSET
    default_configuration: McpServerDtoDefaultConfigurationType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_server_dto_default_configuration_type_0 import McpServerDtoDefaultConfigurationType0

        id = str(self.id)

        name = self.name

        command = self.command

        arguments = self.arguments

        tools_count = self.tools_count

        mcp_server_configurations = []
        for mcp_server_configurations_item_data in self.mcp_server_configurations:
            mcp_server_configurations_item = mcp_server_configurations_item_data.to_dict()
            mcp_server_configurations.append(mcp_server_configurations_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        install_script: None | str | Unset
        if isinstance(self.install_script, Unset):
            install_script = UNSET
        else:
            install_script = self.install_script

        uninstall_script: None | str | Unset
        if isinstance(self.uninstall_script, Unset):
            uninstall_script = UNSET
        else:
            uninstall_script = self.uninstall_script

        before_call_script: None | str | Unset
        if isinstance(self.before_call_script, Unset):
            before_call_script = UNSET
        else:
            before_call_script = self.before_call_script

        allowed_sources: list[str] | None | Unset
        if isinstance(self.allowed_sources, Unset):
            allowed_sources = UNSET
        elif isinstance(self.allowed_sources, list):
            allowed_sources = []
            for allowed_sources_type_0_item_data in self.allowed_sources:
                allowed_sources_type_0_item = allowed_sources_type_0_item_data.value
                allowed_sources.append(allowed_sources_type_0_item)

        else:
            allowed_sources = self.allowed_sources

        after_call_script: None | str | Unset
        if isinstance(self.after_call_script, Unset):
            after_call_script = UNSET
        else:
            after_call_script = self.after_call_script

        default_configuration: dict[str, Any] | None | Unset
        if isinstance(self.default_configuration, Unset):
            default_configuration = UNSET
        elif isinstance(self.default_configuration, McpServerDtoDefaultConfigurationType0):
            default_configuration = self.default_configuration.to_dict()
        else:
            default_configuration = self.default_configuration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "command": command,
                "arguments": arguments,
                "toolsCount": tools_count,
                "mcpServerConfigurations": mcp_server_configurations,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if install_script is not UNSET:
            field_dict["installScript"] = install_script
        if uninstall_script is not UNSET:
            field_dict["uninstallScript"] = uninstall_script
        if before_call_script is not UNSET:
            field_dict["beforeCallScript"] = before_call_script
        if allowed_sources is not UNSET:
            field_dict["allowedSources"] = allowed_sources
        if after_call_script is not UNSET:
            field_dict["afterCallScript"] = after_call_script
        if default_configuration is not UNSET:
            field_dict["defaultConfiguration"] = default_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_server_configuration_dto import McpServerConfigurationDto
        from ..models.mcp_server_dto_default_configuration_type_0 import McpServerDtoDefaultConfigurationType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        command = d.pop("command")

        arguments = cast(list[str], d.pop("arguments"))

        tools_count = d.pop("toolsCount")

        mcp_server_configurations = []
        _mcp_server_configurations = d.pop("mcpServerConfigurations")
        for mcp_server_configurations_item_data in _mcp_server_configurations:
            mcp_server_configurations_item = McpServerConfigurationDto.from_dict(mcp_server_configurations_item_data)

            mcp_server_configurations.append(mcp_server_configurations_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_install_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        install_script = _parse_install_script(d.pop("installScript", UNSET))

        def _parse_uninstall_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uninstall_script = _parse_uninstall_script(d.pop("uninstallScript", UNSET))

        def _parse_before_call_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        before_call_script = _parse_before_call_script(d.pop("beforeCallScript", UNSET))

        def _parse_allowed_sources(data: object) -> list[SourceType] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_sources_type_0 = []
                _allowed_sources_type_0 = data
                for allowed_sources_type_0_item_data in _allowed_sources_type_0:
                    allowed_sources_type_0_item = SourceType(allowed_sources_type_0_item_data)

                    allowed_sources_type_0.append(allowed_sources_type_0_item)

                return allowed_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SourceType] | None | Unset, data)

        allowed_sources = _parse_allowed_sources(d.pop("allowedSources", UNSET))

        def _parse_after_call_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after_call_script = _parse_after_call_script(d.pop("afterCallScript", UNSET))

        def _parse_default_configuration(data: object) -> McpServerDtoDefaultConfigurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_configuration_type_0 = McpServerDtoDefaultConfigurationType0.from_dict(data)

                return default_configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(McpServerDtoDefaultConfigurationType0 | None | Unset, data)

        default_configuration = _parse_default_configuration(d.pop("defaultConfiguration", UNSET))

        mcp_server_dto = cls(
            id=id,
            name=name,
            command=command,
            arguments=arguments,
            tools_count=tools_count,
            mcp_server_configurations=mcp_server_configurations,
            created_at=created_at,
            updated_at=updated_at,
            install_script=install_script,
            uninstall_script=uninstall_script,
            before_call_script=before_call_script,
            allowed_sources=allowed_sources,
            after_call_script=after_call_script,
            default_configuration=default_configuration,
        )

        return mcp_server_dto
