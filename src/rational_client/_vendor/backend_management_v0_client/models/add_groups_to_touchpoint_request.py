from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddGroupsToTouchpointRequest")


@_attrs_define
class AddGroupsToTouchpointRequest:
    """
    Attributes:
        group_ids (list[UUID]):
    """

    group_ids: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        group_ids = []
        for group_ids_item_data in self.group_ids:
            group_ids_item = str(group_ids_item_data)
            group_ids.append(group_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "groupIds": group_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_ids = []
        _group_ids = d.pop("groupIds")
        for group_ids_item_data in _group_ids:
            group_ids_item = UUID(group_ids_item_data)

            group_ids.append(group_ids_item)

        add_groups_to_touchpoint_request = cls(
            group_ids=group_ids,
        )

        return add_groups_to_touchpoint_request
