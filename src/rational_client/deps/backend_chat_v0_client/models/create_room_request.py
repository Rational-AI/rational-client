from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRoomRequest")


@_attrs_define
class CreateRoomRequest:
    """
    Attributes:
        touchpoint_id (None | Unset | UUID):
        title (None | str | Unset):
        display_name (None | str | Unset):
        email_address (None | str | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
    """

    touchpoint_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    email_address: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        touchpoint_id: None | str | Unset
        if isinstance(self.touchpoint_id, Unset):
            touchpoint_id = UNSET
        elif isinstance(self.touchpoint_id, UUID):
            touchpoint_id = str(self.touchpoint_id)
        else:
            touchpoint_id = self.touchpoint_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if touchpoint_id is not UNSET:
            field_dict["touchpointId"] = touchpoint_id
        if title is not UNSET:
            field_dict["title"] = title
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_touchpoint_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                touchpoint_id_type_0 = UUID(data)

                return touchpoint_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        touchpoint_id = _parse_touchpoint_id(d.pop("touchpointId", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("displayName", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        create_room_request = cls(
            touchpoint_id=touchpoint_id,
            title=title,
            display_name=display_name,
            email_address=email_address,
            first_name=first_name,
            last_name=last_name,
        )

        return create_room_request
