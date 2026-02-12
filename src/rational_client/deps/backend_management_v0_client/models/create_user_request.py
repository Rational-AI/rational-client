from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_configuration import ContextConfiguration
    from ..models.create_user_request_context_type_0 import CreateUserRequestContextType0


T = TypeVar("T", bound="CreateUserRequest")


@_attrs_define
class CreateUserRequest:
    """
    Attributes:
        is_admin (bool):
        family_name (str):
        given_name (str):
        authentication_id (None | str | Unset):
        email (None | str | Unset):
        is_enabled (bool | None | Unset):
        context (CreateUserRequestContextType0 | None | Unset):
        context_configuration (ContextConfiguration | Unset):
    """

    is_admin: bool
    family_name: str
    given_name: str
    authentication_id: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    is_enabled: bool | None | Unset = UNSET
    context: CreateUserRequestContextType0 | None | Unset = UNSET
    context_configuration: ContextConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_user_request_context_type_0 import CreateUserRequestContextType0

        is_admin = self.is_admin

        family_name = self.family_name

        given_name = self.given_name

        authentication_id: None | str | Unset
        if isinstance(self.authentication_id, Unset):
            authentication_id = UNSET
        else:
            authentication_id = self.authentication_id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        is_enabled: bool | None | Unset
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, CreateUserRequestContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        context_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context_configuration, Unset):
            context_configuration = self.context_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isAdmin": is_admin,
                "familyName": family_name,
                "givenName": given_name,
            }
        )
        if authentication_id is not UNSET:
            field_dict["authenticationId"] = authentication_id
        if email is not UNSET:
            field_dict["email"] = email
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if context is not UNSET:
            field_dict["context"] = context
        if context_configuration is not UNSET:
            field_dict["contextConfiguration"] = context_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_configuration import ContextConfiguration
        from ..models.create_user_request_context_type_0 import CreateUserRequestContextType0

        d = dict(src_dict)
        is_admin = d.pop("isAdmin")

        family_name = d.pop("familyName")

        given_name = d.pop("givenName")

        def _parse_authentication_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authentication_id = _parse_authentication_id(d.pop("authenticationId", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_is_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        def _parse_context(data: object) -> CreateUserRequestContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = CreateUserRequestContextType0.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateUserRequestContextType0 | None | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

        _context_configuration = d.pop("contextConfiguration", UNSET)
        context_configuration: ContextConfiguration | Unset
        if isinstance(_context_configuration, Unset):
            context_configuration = UNSET
        else:
            context_configuration = ContextConfiguration.from_dict(_context_configuration)

        create_user_request = cls(
            is_admin=is_admin,
            family_name=family_name,
            given_name=given_name,
            authentication_id=authentication_id,
            email=email,
            is_enabled=is_enabled,
            context=context,
            context_configuration=context_configuration,
        )

        return create_user_request
