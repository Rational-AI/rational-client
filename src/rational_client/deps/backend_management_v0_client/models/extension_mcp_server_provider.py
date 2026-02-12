from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extension_mcp_server_provider_configuration_type_0 import ExtensionMcpServerProviderConfigurationType0
    from ..models.extension_mcp_server_provider_environment_type_0 import ExtensionMcpServerProviderEnvironmentType0


T = TypeVar("T", bound="ExtensionMcpServerProvider")


@_attrs_define
class ExtensionMcpServerProvider:
    """
    Attributes:
        name (str):
        path (str):
        command (str):
        arguments (list[str]):
        install_script (None | str | Unset):
        uninstall_script (None | str | Unset):
        before_call_script (None | str | Unset):
        after_call_script (None | str | Unset):
        allowed_sources (list[SourceType] | None | Unset):
        environment (ExtensionMcpServerProviderEnvironmentType0 | None | Unset):
        configuration (ExtensionMcpServerProviderConfigurationType0 | None | Unset):
    """

    name: str
    path: str
    command: str
    arguments: list[str]
    install_script: None | str | Unset = UNSET
    uninstall_script: None | str | Unset = UNSET
    before_call_script: None | str | Unset = UNSET
    after_call_script: None | str | Unset = UNSET
    allowed_sources: list[SourceType] | None | Unset = UNSET
    environment: ExtensionMcpServerProviderEnvironmentType0 | None | Unset = UNSET
    configuration: ExtensionMcpServerProviderConfigurationType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.extension_mcp_server_provider_configuration_type_0 import (
            ExtensionMcpServerProviderConfigurationType0,
        )
        from ..models.extension_mcp_server_provider_environment_type_0 import ExtensionMcpServerProviderEnvironmentType0

        name = self.name

        path = self.path

        command = self.command

        arguments = self.arguments

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

        after_call_script: None | str | Unset
        if isinstance(self.after_call_script, Unset):
            after_call_script = UNSET
        else:
            after_call_script = self.after_call_script

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

        environment: dict[str, Any] | None | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        elif isinstance(self.environment, ExtensionMcpServerProviderEnvironmentType0):
            environment = self.environment.to_dict()
        else:
            environment = self.environment

        configuration: dict[str, Any] | None | Unset
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, ExtensionMcpServerProviderConfigurationType0):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "path": path,
                "command": command,
                "arguments": arguments,
            }
        )
        if install_script is not UNSET:
            field_dict["installScript"] = install_script
        if uninstall_script is not UNSET:
            field_dict["uninstallScript"] = uninstall_script
        if before_call_script is not UNSET:
            field_dict["beforeCallScript"] = before_call_script
        if after_call_script is not UNSET:
            field_dict["afterCallScript"] = after_call_script
        if allowed_sources is not UNSET:
            field_dict["allowedSources"] = allowed_sources
        if environment is not UNSET:
            field_dict["environment"] = environment
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extension_mcp_server_provider_configuration_type_0 import (
            ExtensionMcpServerProviderConfigurationType0,
        )
        from ..models.extension_mcp_server_provider_environment_type_0 import ExtensionMcpServerProviderEnvironmentType0

        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        command = d.pop("command")

        arguments = cast(list[str], d.pop("arguments"))

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

        def _parse_after_call_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after_call_script = _parse_after_call_script(d.pop("afterCallScript", UNSET))

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

        def _parse_environment(data: object) -> ExtensionMcpServerProviderEnvironmentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environment_type_0 = ExtensionMcpServerProviderEnvironmentType0.from_dict(data)

                return environment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExtensionMcpServerProviderEnvironmentType0 | None | Unset, data)

        environment = _parse_environment(d.pop("environment", UNSET))

        def _parse_configuration(data: object) -> ExtensionMcpServerProviderConfigurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = ExtensionMcpServerProviderConfigurationType0.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExtensionMcpServerProviderConfigurationType0 | None | Unset, data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        extension_mcp_server_provider = cls(
            name=name,
            path=path,
            command=command,
            arguments=arguments,
            install_script=install_script,
            uninstall_script=uninstall_script,
            before_call_script=before_call_script,
            after_call_script=after_call_script,
            allowed_sources=allowed_sources,
            environment=environment,
            configuration=configuration,
        )

        return extension_mcp_server_provider
