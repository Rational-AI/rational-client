from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
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
        name (Union[Unset, str]):
        configuration (Union[Unset, UpdateMcpServerConfigurationRequestConfiguration]):
        source_ids (Union[Unset, list[UUID]]):
    """

    name: Union[Unset, str] = UNSET
    configuration: Union[Unset, "UpdateMcpServerConfigurationRequestConfiguration"] = UNSET
    source_ids: Union[Unset, list[UUID]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        source_ids: Union[Unset, list[str]] = UNSET
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
        configuration: Union[Unset, UpdateMcpServerConfigurationRequestConfiguration]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UpdateMcpServerConfigurationRequestConfiguration.from_dict(_configuration)

        source_ids = []
        _source_ids = d.pop("sourceIds", UNSET)
        for source_ids_item_data in _source_ids or []:
            source_ids_item = UUID(source_ids_item_data)

            source_ids.append(source_ids_item)

        update_mcp_server_configuration_request = cls(
            name=name,
            configuration=configuration,
            source_ids=source_ids,
        )

        return update_mcp_server_configuration_request
