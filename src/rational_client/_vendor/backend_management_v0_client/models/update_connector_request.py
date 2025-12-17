from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.connector_type import ConnectorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateConnectorRequest")


@_attrs_define
class UpdateConnectorRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        type_ (Union[Unset, ConnectorType]):
        data (Union[Unset, Any]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    type_: Union[Unset, ConnectorType] = UNSET
    data: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ConnectorType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConnectorType(_type_)

        data = d.pop("data", UNSET)

        update_connector_request = cls(
            name=name,
            description=description,
            type_=type_,
            data=data,
        )

        return update_connector_request
