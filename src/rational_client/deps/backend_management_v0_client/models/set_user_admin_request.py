from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SetUserAdminRequest")


@_attrs_define
class SetUserAdminRequest:
    """
    Attributes:
        is_admin (bool):
    """

    is_admin: bool

    def to_dict(self) -> dict[str, Any]:
        is_admin = self.is_admin

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isAdmin": is_admin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_admin = d.pop("isAdmin")

        set_user_admin_request = cls(
            is_admin=is_admin,
        )

        return set_user_admin_request
