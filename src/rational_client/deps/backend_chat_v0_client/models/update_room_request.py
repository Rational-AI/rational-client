from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.room_status import RoomStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRoomRequest")


@_attrs_define
class UpdateRoomRequest:
    """
    Attributes:
        title (None | str | Unset):
        room_status (RoomStatus | Unset):
        is_starred (bool | Unset):
    """

    title: None | str | Unset = UNSET
    room_status: RoomStatus | Unset = UNSET
    is_starred: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        room_status: str | Unset = UNSET
        if not isinstance(self.room_status, Unset):
            room_status = self.room_status.value

        is_starred = self.is_starred

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if room_status is not UNSET:
            field_dict["roomStatus"] = room_status
        if is_starred is not UNSET:
            field_dict["isStarred"] = is_starred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _room_status = d.pop("roomStatus", UNSET)
        room_status: RoomStatus | Unset
        if isinstance(_room_status, Unset):
            room_status = UNSET
        else:
            room_status = RoomStatus(_room_status)

        is_starred = d.pop("isStarred", UNSET)

        update_room_request = cls(
            title=title,
            room_status=room_status,
            is_starred=is_starred,
        )

        return update_room_request
