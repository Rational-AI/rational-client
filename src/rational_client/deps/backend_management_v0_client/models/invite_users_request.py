from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.invite_user_request import InviteUserRequest


T = TypeVar("T", bound="InviteUsersRequest")


@_attrs_define
class InviteUsersRequest:
    """
    Attributes:
        is_admin (bool):
        is_enabled (bool):
        invite_user_requests (list[InviteUserRequest]):
    """

    is_admin: bool
    is_enabled: bool
    invite_user_requests: list[InviteUserRequest]

    def to_dict(self) -> dict[str, Any]:
        is_admin = self.is_admin

        is_enabled = self.is_enabled

        invite_user_requests = []
        for invite_user_requests_item_data in self.invite_user_requests:
            invite_user_requests_item = invite_user_requests_item_data.to_dict()
            invite_user_requests.append(invite_user_requests_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isAdmin": is_admin,
                "isEnabled": is_enabled,
                "inviteUserRequests": invite_user_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_user_request import InviteUserRequest

        d = dict(src_dict)
        is_admin = d.pop("isAdmin")

        is_enabled = d.pop("isEnabled")

        invite_user_requests = []
        _invite_user_requests = d.pop("inviteUserRequests")
        for invite_user_requests_item_data in _invite_user_requests:
            invite_user_requests_item = InviteUserRequest.from_dict(invite_user_requests_item_data)

            invite_user_requests.append(invite_user_requests_item)

        invite_users_request = cls(
            is_admin=is_admin,
            is_enabled=is_enabled,
            invite_user_requests=invite_user_requests,
        )

        return invite_users_request
