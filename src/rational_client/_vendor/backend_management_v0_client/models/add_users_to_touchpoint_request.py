from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddUsersToTouchpointRequest")


@_attrs_define
class AddUsersToTouchpointRequest:
    """
    Attributes:
        user_ids (list[UUID]):
    """

    user_ids: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        user_ids = []
        for user_ids_item_data in self.user_ids:
            user_ids_item = str(user_ids_item_data)
            user_ids.append(user_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userIds": user_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = []
        _user_ids = d.pop("userIds")
        for user_ids_item_data in _user_ids:
            user_ids_item = UUID(user_ids_item_data)

            user_ids.append(user_ids_item)

        add_users_to_touchpoint_request = cls(
            user_ids=user_ids,
        )

        return add_users_to_touchpoint_request
