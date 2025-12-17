from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_mcp_server_configuration_request_configuration import (
        CreateMcpServerConfigurationRequestConfiguration,
    )


T = TypeVar("T", bound="CreateMcpServerConfigurationRequest")


@_attrs_define
class CreateMcpServerConfigurationRequest:
    """
    Attributes:
        name (str):
        is_default (bool):
        mcp_server_id (UUID):
        configuration (CreateMcpServerConfigurationRequestConfiguration):
        source_ids (list[UUID]):
    """

    name: str
    is_default: bool
    mcp_server_id: UUID
    configuration: "CreateMcpServerConfigurationRequestConfiguration"
    source_ids: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_default = self.is_default

        mcp_server_id = str(self.mcp_server_id)

        configuration = self.configuration.to_dict()

        source_ids = []
        for source_ids_item_data in self.source_ids:
            source_ids_item = str(source_ids_item_data)
            source_ids.append(source_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "isDefault": is_default,
                "mcpServerId": mcp_server_id,
                "configuration": configuration,
                "sourceIds": source_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_mcp_server_configuration_request_configuration import (
            CreateMcpServerConfigurationRequestConfiguration,
        )

        d = dict(src_dict)
        name = d.pop("name")

        is_default = d.pop("isDefault")

        mcp_server_id = UUID(d.pop("mcpServerId"))

        configuration = CreateMcpServerConfigurationRequestConfiguration.from_dict(d.pop("configuration"))

        source_ids = []
        _source_ids = d.pop("sourceIds")
        for source_ids_item_data in _source_ids:
            source_ids_item = UUID(source_ids_item_data)

            source_ids.append(source_ids_item)

        create_mcp_server_configuration_request = cls(
            name=name,
            is_default=is_default,
            mcp_server_id=mcp_server_id,
            configuration=configuration,
            source_ids=source_ids,
        )

        return create_mcp_server_configuration_request
