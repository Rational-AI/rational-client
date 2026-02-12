from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_configuration_param import ToolConfigurationParam


T = TypeVar("T", bound="CreateTouchpointToolRequest")


@_attrs_define
class CreateTouchpointToolRequest:
    """
    Attributes:
        mcp_server_tool_id (UUID):
        touchpoint_id (UUID):
        params (list[ToolConfigurationParam]):
        name (None | str | Unset):
        title (None | str | Unset):
        description (None | str | Unset):
    """

    mcp_server_tool_id: UUID
    touchpoint_id: UUID
    params: list[ToolConfigurationParam]
    name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mcp_server_tool_id = str(self.mcp_server_tool_id)

        touchpoint_id = str(self.touchpoint_id)

        params = []
        for params_item_data in self.params:
            params_item = params_item_data.to_dict()
            params.append(params_item)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mcpServerToolId": mcp_server_tool_id,
                "touchpointId": touchpoint_id,
                "params": params,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_configuration_param import ToolConfigurationParam

        d = dict(src_dict)
        mcp_server_tool_id = UUID(d.pop("mcpServerToolId"))

        touchpoint_id = UUID(d.pop("touchpointId"))

        params = []
        _params = d.pop("params")
        for params_item_data in _params:
            params_item = ToolConfigurationParam.from_dict(params_item_data)

            params.append(params_item)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        create_touchpoint_tool_request = cls(
            mcp_server_tool_id=mcp_server_tool_id,
            touchpoint_id=touchpoint_id,
            params=params,
            name=name,
            title=title,
            description=description,
        )

        return create_touchpoint_tool_request
