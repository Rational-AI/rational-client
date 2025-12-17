from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider import Provider


T = TypeVar("T", bound="McpServerParam")


@_attrs_define
class McpServerParam:
    """
    Attributes:
        provider (Provider):
        is_required (bool):
        is_hidden (bool):
        title (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        default_value (Union[Unset, Any]):
    """

    provider: "Provider"
    is_required: bool
    is_hidden: bool
    title: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    default_value: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider.to_dict()

        is_required = self.is_required

        is_hidden = self.is_hidden

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

        default_value = self.default_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
                "isRequired": is_required,
                "isHidden": is_hidden,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider import Provider

        d = dict(src_dict)
        provider = Provider.from_dict(d.pop("provider"))

        is_required = d.pop("isRequired")

        is_hidden = d.pop("isHidden")

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

        default_value = d.pop("defaultValue", UNSET)

        mcp_server_param = cls(
            provider=provider,
            is_required=is_required,
            is_hidden=is_hidden,
            title=title,
            description=description,
            default_value=default_value,
        )

        return mcp_server_param
