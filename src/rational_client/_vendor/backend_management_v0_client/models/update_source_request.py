from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_source_request_configuration import UpdateSourceRequestConfiguration


T = TypeVar("T", bound="UpdateSourceRequest")


@_attrs_define
class UpdateSourceRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        icon_url (Union[None, Unset, str]):
        type_ (Union[Unset, SourceType]):
        configuration (Union[Unset, UpdateSourceRequestConfiguration]):
    """

    name: Union[Unset, str] = UNSET
    icon_url: Union[None, Unset, str] = UNSET
    type_: Union[Unset, SourceType] = UNSET
    configuration: Union[Unset, "UpdateSourceRequestConfiguration"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        icon_url: Union[None, Unset, str]
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_source_request_configuration import UpdateSourceRequestConfiguration

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_icon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SourceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SourceType(_type_)

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, UpdateSourceRequestConfiguration]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UpdateSourceRequestConfiguration.from_dict(_configuration)

        update_source_request = cls(
            name=name,
            icon_url=icon_url,
            type_=type_,
            configuration=configuration,
        )

        return update_source_request
