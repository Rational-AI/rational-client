from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="UserDtoPage")


@_attrs_define
class UserDtoPage:
    """
    Attributes:
        offset (int):
        limit (int):
        count (int):
        items (list[UserDto]):
    """

    offset: int
    limit: int
    count: int
    items: list[UserDto]

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        count = self.count

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
                "count": count,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_dto import UserDto

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        count = d.pop("count")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = UserDto.from_dict(items_item_data)

            items.append(items_item)

        user_dto_page = cls(
            offset=offset,
            limit=limit,
            count=count,
            items=items,
        )

        return user_dto_page
