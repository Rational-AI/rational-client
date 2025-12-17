from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_mcp_server_tool_request_default_configuration import (
        UpdateMcpServerToolRequestDefaultConfiguration,
    )


T = TypeVar("T", bound="UpdateMcpServerToolRequest")


@_attrs_define
class UpdateMcpServerToolRequest:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        default_configuration (Union[Unset, UpdateMcpServerToolRequestDefaultConfiguration]):
    """

    enabled: Union[Unset, bool] = UNSET
    default_configuration: Union[Unset, "UpdateMcpServerToolRequestDefaultConfiguration"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        default_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_configuration, Unset):
            default_configuration = self.default_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if default_configuration is not UNSET:
            field_dict["defaultConfiguration"] = default_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_mcp_server_tool_request_default_configuration import (
            UpdateMcpServerToolRequestDefaultConfiguration,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _default_configuration = d.pop("defaultConfiguration", UNSET)
        default_configuration: Union[Unset, UpdateMcpServerToolRequestDefaultConfiguration]
        if isinstance(_default_configuration, Unset):
            default_configuration = UNSET
        else:
            default_configuration = UpdateMcpServerToolRequestDefaultConfiguration.from_dict(_default_configuration)

        update_mcp_server_tool_request = cls(
            enabled=enabled,
            default_configuration=default_configuration,
        )

        return update_mcp_server_tool_request
