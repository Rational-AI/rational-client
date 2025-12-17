from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_configuration_param import ToolConfigurationParam


T = TypeVar("T", bound="UpdateTouchpointToolRequest")


@_attrs_define
class UpdateTouchpointToolRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        title (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        mcp_server_tool_id (Union[Unset, UUID]):
        params (Union[Unset, list['ToolConfigurationParam']]):
    """

    name: Union[Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    mcp_server_tool_id: Union[Unset, UUID] = UNSET
    params: Union[Unset, list["ToolConfigurationParam"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        mcp_server_tool_id: Union[Unset, str] = UNSET
        if not isinstance(self.mcp_server_tool_id, Unset):
            mcp_server_tool_id = str(self.mcp_server_tool_id)

        params: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.params, Unset):
            params = []
            for params_item_data in self.params:
                params_item = params_item_data.to_dict()
                params.append(params_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if mcp_server_tool_id is not UNSET:
            field_dict["mcpServerToolId"] = mcp_server_tool_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_configuration_param import ToolConfigurationParam

        d = dict(src_dict)
        name = d.pop("name", UNSET)

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

        _mcp_server_tool_id = d.pop("mcpServerToolId", UNSET)
        mcp_server_tool_id: Union[Unset, UUID]
        if isinstance(_mcp_server_tool_id, Unset):
            mcp_server_tool_id = UNSET
        else:
            mcp_server_tool_id = UUID(_mcp_server_tool_id)

        params = []
        _params = d.pop("params", UNSET)
        for params_item_data in _params or []:
            params_item = ToolConfigurationParam.from_dict(params_item_data)

            params.append(params_item)

        update_touchpoint_tool_request = cls(
            name=name,
            title=title,
            description=description,
            mcp_server_tool_id=mcp_server_tool_id,
            params=params,
        )

        return update_touchpoint_tool_request
