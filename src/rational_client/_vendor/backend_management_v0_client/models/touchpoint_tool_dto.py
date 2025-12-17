import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_server_tool_dto import McpServerToolDto
    from ..models.tool_configuration_param import ToolConfigurationParam


T = TypeVar("T", bound="TouchpointToolDto")


@_attrs_define
class TouchpointToolDto:
    """
    Attributes:
        id (UUID):
        name (str):
        mcp_server_tool (McpServerToolDto):
        touchpoint_id (UUID):
        params (list['ToolConfigurationParam']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        title (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    mcp_server_tool: "McpServerToolDto"
    touchpoint_id: UUID
    params: list["ToolConfigurationParam"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    title: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        mcp_server_tool = self.mcp_server_tool.to_dict()

        touchpoint_id = str(self.touchpoint_id)

        params = []
        for params_item_data in self.params:
            params_item = params_item_data.to_dict()
            params.append(params_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "mcpServerTool": mcp_server_tool,
                "touchpointId": touchpoint_id,
                "params": params,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_server_tool_dto import McpServerToolDto
        from ..models.tool_configuration_param import ToolConfigurationParam

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        mcp_server_tool = McpServerToolDto.from_dict(d.pop("mcpServerTool"))

        touchpoint_id = UUID(d.pop("touchpointId"))

        params = []
        _params = d.pop("params")
        for params_item_data in _params:
            params_item = ToolConfigurationParam.from_dict(params_item_data)

            params.append(params_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        touchpoint_tool_dto = cls(
            id=id,
            name=name,
            mcp_server_tool=mcp_server_tool,
            touchpoint_id=touchpoint_id,
            params=params,
            created_at=created_at,
            updated_at=updated_at,
            title=title,
            description=description,
        )

        return touchpoint_tool_dto
