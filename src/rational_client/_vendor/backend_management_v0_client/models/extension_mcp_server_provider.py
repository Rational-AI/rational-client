from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extension_mcp_server_provider_configuration_type_0 import ExtensionMcpServerProviderConfigurationType0


T = TypeVar("T", bound="ExtensionMcpServerProvider")


@_attrs_define
class ExtensionMcpServerProvider:
    """
    Attributes:
        name (str):
        path (str):
        command (str):
        arguments (list[str]):
        install_script (Union[None, Unset, str]):
        uninstall_script (Union[None, Unset, str]):
        before_call_script (Union[None, Unset, str]):
        after_call_script (Union[None, Unset, str]):
        allowed_sources (Union[None, Unset, list[SourceType]]):
        configuration (Union['ExtensionMcpServerProviderConfigurationType0', None, Unset]):
    """

    name: str
    path: str
    command: str
    arguments: list[str]
    install_script: Union[None, Unset, str] = UNSET
    uninstall_script: Union[None, Unset, str] = UNSET
    before_call_script: Union[None, Unset, str] = UNSET
    after_call_script: Union[None, Unset, str] = UNSET
    allowed_sources: Union[None, Unset, list[SourceType]] = UNSET
    configuration: Union["ExtensionMcpServerProviderConfigurationType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.extension_mcp_server_provider_configuration_type_0 import (
            ExtensionMcpServerProviderConfigurationType0,
        )

        name = self.name

        path = self.path

        command = self.command

        arguments = self.arguments

        install_script: Union[None, Unset, str]
        if isinstance(self.install_script, Unset):
            install_script = UNSET
        else:
            install_script = self.install_script

        uninstall_script: Union[None, Unset, str]
        if isinstance(self.uninstall_script, Unset):
            uninstall_script = UNSET
        else:
            uninstall_script = self.uninstall_script

        before_call_script: Union[None, Unset, str]
        if isinstance(self.before_call_script, Unset):
            before_call_script = UNSET
        else:
            before_call_script = self.before_call_script

        after_call_script: Union[None, Unset, str]
        if isinstance(self.after_call_script, Unset):
            after_call_script = UNSET
        else:
            after_call_script = self.after_call_script

        allowed_sources: Union[None, Unset, list[str]]
        if isinstance(self.allowed_sources, Unset):
            allowed_sources = UNSET
        elif isinstance(self.allowed_sources, list):
            allowed_sources = []
            for allowed_sources_type_0_item_data in self.allowed_sources:
                allowed_sources_type_0_item = allowed_sources_type_0_item_data.value
                allowed_sources.append(allowed_sources_type_0_item)

        else:
            allowed_sources = self.allowed_sources

        configuration: Union[None, Unset, dict[str, Any]]
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
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extension_mcp_server_provider_configuration_type_0 import (
            ExtensionMcpServerProviderConfigurationType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        command = d.pop("command")

        arguments = cast(list[str], d.pop("arguments"))

        def _parse_install_script(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        install_script = _parse_install_script(d.pop("installScript", UNSET))

        def _parse_uninstall_script(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uninstall_script = _parse_uninstall_script(d.pop("uninstallScript", UNSET))

        def _parse_before_call_script(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        before_call_script = _parse_before_call_script(d.pop("beforeCallScript", UNSET))

        def _parse_after_call_script(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        after_call_script = _parse_after_call_script(d.pop("afterCallScript", UNSET))

        def _parse_allowed_sources(data: object) -> Union[None, Unset, list[SourceType]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[SourceType]], data)

        allowed_sources = _parse_allowed_sources(d.pop("allowedSources", UNSET))

        def _parse_configuration(data: object) -> Union["ExtensionMcpServerProviderConfigurationType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = ExtensionMcpServerProviderConfigurationType0.from_dict(data)

                return configuration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ExtensionMcpServerProviderConfigurationType0", None, Unset], data)

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
            configuration=configuration,
        )

        return extension_mcp_server_provider
