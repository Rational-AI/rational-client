import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupDto")


@_attrs_define
class GroupDto:
    """
    Attributes:
        id (UUID):
        name (str):
        allow_anonymous (bool):
        users_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    allow_anonymous: bool
    users_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        allow_anonymous = self.allow_anonymous

        users_count = self.users_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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
                "allowAnonymous": allow_anonymous,
                "usersCount": users_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        allow_anonymous = d.pop("allowAnonymous")

        users_count = d.pop("usersCount")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        group_dto = cls(
            id=id,
            name=name,
            allow_anonymous=allow_anonymous,
            users_count=users_count,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        return group_dto
