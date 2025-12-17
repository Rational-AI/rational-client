import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.connector_type import ConnectorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectorDto")


@_attrs_define
class ConnectorDto:
    """
    Attributes:
        id (UUID):
        name (str):
        type_ (ConnectorType):
        models_count (int):
        sources_count (int):
        tools_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (Union[None, Unset, str]):
        data (Union[Unset, Any]):
    """

    id: UUID
    name: str
    type_: ConnectorType
    models_count: int
    sources_count: int
    tools_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[None, Unset, str] = UNSET
    data: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        models_count = self.models_count

        sources_count = self.sources_count

        tools_count = self.tools_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "modelsCount": models_count,
                "sourcesCount": sources_count,
                "toolsCount": tools_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
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
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = ConnectorType(d.pop("type"))

        models_count = d.pop("modelsCount")

        sources_count = d.pop("sourcesCount")

        tools_count = d.pop("toolsCount")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        data = d.pop("data", UNSET)

        connector_dto = cls(
            id=id,
            name=name,
            type_=type_,
            models_count=models_count,
            sources_count=sources_count,
            tools_count=tools_count,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            data=data,
        )

        return connector_dto
