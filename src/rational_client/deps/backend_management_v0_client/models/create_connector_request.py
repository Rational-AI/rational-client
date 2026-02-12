from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.connector_type import ConnectorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateConnectorRequest")


@_attrs_define
class CreateConnectorRequest:
    """
    Attributes:
        name (str):
        type_ (ConnectorType):
        description (None | str | Unset):
        data (Any | Unset):
    """

    name: str
    type_: ConnectorType
    description: None | str | Unset = UNSET
    data: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ConnectorType(d.pop("type"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        data = d.pop("data", UNSET)

        create_connector_request = cls(
            name=name,
            type_=type_,
            description=description,
            data=data,
        )

        return create_connector_request
