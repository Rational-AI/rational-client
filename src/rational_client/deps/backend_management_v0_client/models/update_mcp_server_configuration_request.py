from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_mcp_server_configuration_request_configuration import (
        UpdateMcpServerConfigurationRequestConfiguration,
    )


T = TypeVar("T", bound="UpdateMcpServerConfigurationRequest")


@_attrs_define
class UpdateMcpServerConfigurationRequest:
    """
    Attributes:
        name (str | Unset):
        configuration (UpdateMcpServerConfigurationRequestConfiguration | Unset):
        source_ids (list[UUID] | Unset):
    """

    name: str | Unset = UNSET
    configuration: UpdateMcpServerConfigurationRequestConfiguration | Unset = UNSET
    source_ids: list[UUID] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        source_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = []
            for source_ids_item_data in self.source_ids:
                source_ids_item = str(source_ids_item_data)
                source_ids.append(source_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if source_ids is not UNSET:
            field_dict["sourceIds"] = source_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_mcp_server_configuration_request_configuration import (
            UpdateMcpServerConfigurationRequestConfiguration,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: UpdateMcpServerConfigurationRequestConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UpdateMcpServerConfigurationRequestConfiguration.from_dict(_configuration)

        _source_ids = d.pop("sourceIds", UNSET)
        source_ids: list[UUID] | Unset = UNSET
        if _source_ids is not UNSET:
            source_ids = []
            for source_ids_item_data in _source_ids:
                source_ids_item = UUID(source_ids_item_data)

                source_ids.append(source_ids_item)

        update_mcp_server_configuration_request = cls(
            name=name,
            configuration=configuration,
            source_ids=source_ids,
        )

        return update_mcp_server_configuration_request
