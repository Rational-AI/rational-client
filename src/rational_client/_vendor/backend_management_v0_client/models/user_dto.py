import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_configuration import ContextConfiguration
    from ..models.user_dto_context_type_0 import UserDtoContextType0
    from ..models.user_group_dto import UserGroupDto


T = TypeVar("T", bound="UserDto")


@_attrs_define
class UserDto:
    """
    Attributes:
        id (UUID):
        is_admin (bool):
        is_enabled (bool):
        rooms_count (int):
        groups (list['UserGroupDto']):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        authentication_id (Union[None, Unset, str]):
        family_name (Union[None, Unset, str]):
        given_name (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        context (Union['UserDtoContextType0', None, Unset]):
        context_configuration (Union[Unset, ContextConfiguration]):
    """

    id: UUID
    is_admin: bool
    is_enabled: bool
    rooms_count: int
    groups: list["UserGroupDto"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    authentication_id: Union[None, Unset, str] = UNSET
    family_name: Union[None, Unset, str] = UNSET
    given_name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    context: Union["UserDtoContextType0", None, Unset] = UNSET
    context_configuration: Union[Unset, "ContextConfiguration"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_dto_context_type_0 import UserDtoContextType0

        id = str(self.id)

        is_admin = self.is_admin

        is_enabled = self.is_enabled

        rooms_count = self.rooms_count

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        authentication_id: Union[None, Unset, str]
        if isinstance(self.authentication_id, Unset):
            authentication_id = UNSET
        else:
            authentication_id = self.authentication_id

        family_name: Union[None, Unset, str]
        if isinstance(self.family_name, Unset):
            family_name = UNSET
        else:
            family_name = self.family_name

        given_name: Union[None, Unset, str]
        if isinstance(self.given_name, Unset):
            given_name = UNSET
        else:
            given_name = self.given_name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        context: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, UserDtoContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        context_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_configuration, Unset):
            context_configuration = self.context_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "isAdmin": is_admin,
                "isEnabled": is_enabled,
                "roomsCount": rooms_count,
                "groups": groups,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if authentication_id is not UNSET:
            field_dict["authenticationId"] = authentication_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if email is not UNSET:
            field_dict["email"] = email
        if context is not UNSET:
            field_dict["context"] = context
        if context_configuration is not UNSET:
            field_dict["contextConfiguration"] = context_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_configuration import ContextConfiguration
        from ..models.user_dto_context_type_0 import UserDtoContextType0
        from ..models.user_group_dto import UserGroupDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        is_admin = d.pop("isAdmin")

        is_enabled = d.pop("isEnabled")

        rooms_count = d.pop("roomsCount")

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = UserGroupDto.from_dict(groups_item_data)

            groups.append(groups_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_authentication_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        authentication_id = _parse_authentication_id(d.pop("authenticationId", UNSET))

        def _parse_family_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        family_name = _parse_family_name(d.pop("familyName", UNSET))

        def _parse_given_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        given_name = _parse_given_name(d.pop("givenName", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_context(data: object) -> Union["UserDtoContextType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = UserDtoContextType0.from_dict(data)

                return context_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UserDtoContextType0", None, Unset], data)

        context = _parse_context(d.pop("context", UNSET))

        _context_configuration = d.pop("contextConfiguration", UNSET)
        context_configuration: Union[Unset, ContextConfiguration]
        if isinstance(_context_configuration, Unset):
            context_configuration = UNSET
        else:
            context_configuration = ContextConfiguration.from_dict(_context_configuration)

        user_dto = cls(
            id=id,
            is_admin=is_admin,
            is_enabled=is_enabled,
            rooms_count=rooms_count,
            groups=groups,
            created_at=created_at,
            updated_at=updated_at,
            authentication_id=authentication_id,
            family_name=family_name,
            given_name=given_name,
            email=email,
            context=context,
            context_configuration=context_configuration,
        )

        return user_dto
