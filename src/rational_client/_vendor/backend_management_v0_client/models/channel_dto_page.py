from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.channel_dto import ChannelDto


T = TypeVar("T", bound="ChannelDtoPage")


@_attrs_define
class ChannelDtoPage:
    """
    Attributes:
        offset (int):
        limit (int):
        count (int):
        items (list['ChannelDto']):
    """

    offset: int
    limit: int
    count: int
    items: list["ChannelDto"]

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
        from ..models.channel_dto import ChannelDto

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        count = d.pop("count")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ChannelDto.from_dict(items_item_data)

            items.append(items_item)

        channel_dto_page = cls(
            offset=offset,
            limit=limit,
            count=count,
            items=items,
        )

        return channel_dto_page
