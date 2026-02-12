from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.event_status import EventStatus
from ..models.event_type import EventType
from ..models.sender_type import SenderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        room_id (UUID):
        sender_type (SenderType):
        type_ (EventType):
        status (EventStatus):
        content (Any):
        client_msg (Any):
        status_details (None | str | Unset):
        agent_msg (Any | Unset):
        metadata (Any | Unset):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    room_id: UUID
    sender_type: SenderType
    type_: EventType
    status: EventStatus
    content: Any
    client_msg: Any
    status_details: None | str | Unset = UNSET
    agent_msg: Any | Unset = UNSET
    metadata: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        room_id = str(self.room_id)

        sender_type = self.sender_type.value

        type_ = self.type_.value

        status = self.status.value

        content = self.content

        client_msg = self.client_msg

        status_details: None | str | Unset
        if isinstance(self.status_details, Unset):
            status_details = UNSET
        else:
            status_details = self.status_details

        agent_msg = self.agent_msg

        metadata = self.metadata

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "roomId": room_id,
                "senderType": sender_type,
                "type": type_,
                "status": status,
                "content": content,
                "clientMsg": client_msg,
            }
        )
        if status_details is not UNSET:
            field_dict["statusDetails"] = status_details
        if agent_msg is not UNSET:
            field_dict["agentMsg"] = agent_msg
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        room_id = UUID(d.pop("roomId"))

        sender_type = SenderType(d.pop("senderType"))

        type_ = EventType(d.pop("type"))

        status = EventStatus(d.pop("status"))

        content = d.pop("content")

        client_msg = d.pop("clientMsg")

        def _parse_status_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_details = _parse_status_details(d.pop("statusDetails", UNSET))

        agent_msg = d.pop("agentMsg", UNSET)

        metadata = d.pop("metadata", UNSET)

        event = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            room_id=room_id,
            sender_type=sender_type,
            type_=type_,
            status=status,
            content=content,
            client_msg=client_msg,
            status_details=status_details,
            agent_msg=agent_msg,
            metadata=metadata,
        )

        return event
