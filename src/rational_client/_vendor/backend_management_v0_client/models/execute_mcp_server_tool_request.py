from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.execute_mcp_server_tool_request_input_arguments import ExecuteMcpServerToolRequestInputArguments


T = TypeVar("T", bound="ExecuteMcpServerToolRequest")


@_attrs_define
class ExecuteMcpServerToolRequest:
    """
    Attributes:
        input_arguments (ExecuteMcpServerToolRequestInputArguments):
    """

    input_arguments: "ExecuteMcpServerToolRequestInputArguments"

    def to_dict(self) -> dict[str, Any]:
        input_arguments = self.input_arguments.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "inputArguments": input_arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execute_mcp_server_tool_request_input_arguments import ExecuteMcpServerToolRequestInputArguments

        d = dict(src_dict)
        input_arguments = ExecuteMcpServerToolRequestInputArguments.from_dict(d.pop("inputArguments"))

        execute_mcp_server_tool_request = cls(
            input_arguments=input_arguments,
        )

        return execute_mcp_server_tool_request
