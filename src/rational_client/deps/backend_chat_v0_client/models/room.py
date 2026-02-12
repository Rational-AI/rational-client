from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.assignee_type import AssigneeType
from ..models.room_status import RoomStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.room_agent_store import RoomAgentStore
    from ..models.room_user_store import RoomUserStore
    from ..models.user_details import UserDetails


T = TypeVar("T", bound="Room")


@_attrs_define
class Room:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        room_status (RoomStatus):
        is_starred (bool):
        user_details (UserDetails):
        assignee_type (AssigneeType):
        user_store (RoomUserStore):
        agent_store (RoomAgentStore):
        title (None | str | Unset):
        user_id (None | Unset | UUID):
        assignee_id (None | Unset | UUID):
        touchpoint_id (None | Unset | UUID):
        touchpoint_name (None | str | Unset):
        sentiment (None | str | Unset):
        topic (None | str | Unset):
        last_message_event (Event | Unset):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    room_status: RoomStatus
    is_starred: bool
    user_details: UserDetails
    assignee_type: AssigneeType
    user_store: RoomUserStore
    agent_store: RoomAgentStore
    title: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    assignee_id: None | Unset | UUID = UNSET
    touchpoint_id: None | Unset | UUID = UNSET
    touchpoint_name: None | str | Unset = UNSET
    sentiment: None | str | Unset = UNSET
    topic: None | str | Unset = UNSET
    last_message_event: Event | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        room_status = self.room_status.value

        is_starred = self.is_starred

        user_details = self.user_details.to_dict()

        assignee_type = self.assignee_type.value

        user_store = self.user_store.to_dict()

        agent_store = self.agent_store.to_dict()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        elif isinstance(self.assignee_id, UUID):
            assignee_id = str(self.assignee_id)
        else:
            assignee_id = self.assignee_id

        touchpoint_id: None | str | Unset
        if isinstance(self.touchpoint_id, Unset):
            touchpoint_id = UNSET
        elif isinstance(self.touchpoint_id, UUID):
            touchpoint_id = str(self.touchpoint_id)
        else:
            touchpoint_id = self.touchpoint_id

        touchpoint_name: None | str | Unset
        if isinstance(self.touchpoint_name, Unset):
            touchpoint_name = UNSET
        else:
            touchpoint_name = self.touchpoint_name

        sentiment: None | str | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        topic: None | str | Unset
        if isinstance(self.topic, Unset):
            topic = UNSET
        else:
            topic = self.topic

        last_message_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_message_event, Unset):
            last_message_event = self.last_message_event.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "roomStatus": room_status,
                "isStarred": is_starred,
                "userDetails": user_details,
                "assigneeType": assignee_type,
                "userStore": user_store,
                "agentStore": agent_store,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if assignee_id is not UNSET:
            field_dict["assigneeId"] = assignee_id
        if touchpoint_id is not UNSET:
            field_dict["touchpointId"] = touchpoint_id
        if touchpoint_name is not UNSET:
            field_dict["touchpointName"] = touchpoint_name
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if topic is not UNSET:
            field_dict["topic"] = topic
        if last_message_event is not UNSET:
            field_dict["lastMessageEvent"] = last_message_event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event import Event
        from ..models.room_agent_store import RoomAgentStore
        from ..models.room_user_store import RoomUserStore
        from ..models.user_details import UserDetails

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        room_status = RoomStatus(d.pop("roomStatus"))

        is_starred = d.pop("isStarred")

        user_details = UserDetails.from_dict(d.pop("userDetails"))

        assignee_type = AssigneeType(d.pop("assigneeType"))

        user_store = RoomUserStore.from_dict(d.pop("userStore"))

        agent_store = RoomAgentStore.from_dict(d.pop("agentStore"))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_assignee_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignee_id_type_0 = UUID(data)

                return assignee_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assignee_id = _parse_assignee_id(d.pop("assigneeId", UNSET))

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

        def _parse_touchpoint_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        touchpoint_name = _parse_touchpoint_name(d.pop("touchpointName", UNSET))

        def _parse_sentiment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        def _parse_topic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        topic = _parse_topic(d.pop("topic", UNSET))

        _last_message_event = d.pop("lastMessageEvent", UNSET)
        last_message_event: Event | Unset
        if isinstance(_last_message_event, Unset):
            last_message_event = UNSET
        else:
            last_message_event = Event.from_dict(_last_message_event)

        room = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            room_status=room_status,
            is_starred=is_starred,
            user_details=user_details,
            assignee_type=assignee_type,
            user_store=user_store,
            agent_store=agent_store,
            title=title,
            user_id=user_id,
            assignee_id=assignee_id,
            touchpoint_id=touchpoint_id,
            touchpoint_name=touchpoint_name,
            sentiment=sentiment,
            topic=topic,
            last_message_event=last_message_event,
        )

        return room
