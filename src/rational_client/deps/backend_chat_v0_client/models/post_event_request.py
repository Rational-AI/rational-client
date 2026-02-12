from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_type import EventType
from ..models.sender_type import SenderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_event_request_context_msg_type_0 import PostEventRequestContextMsgType0


T = TypeVar("T", bound="PostEventRequest")


@_attrs_define
class PostEventRequest:
    """
    Attributes:
        type_ (EventType):
        content (Any):
        sender_type (SenderType):
        client_msg (Any | Unset):
        agent_msg (Any | Unset):
        context_msg (None | PostEventRequestContextMsgType0 | Unset):
    """

    type_: EventType
    content: Any
    sender_type: SenderType
    client_msg: Any | Unset = UNSET
    agent_msg: Any | Unset = UNSET
    context_msg: None | PostEventRequestContextMsgType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_event_request_context_msg_type_0 import PostEventRequestContextMsgType0

        type_ = self.type_.value

        content = self.content

        sender_type = self.sender_type.value

        client_msg = self.client_msg

        agent_msg = self.agent_msg

        context_msg: dict[str, Any] | None | Unset
        if isinstance(self.context_msg, Unset):
            context_msg = UNSET
        elif isinstance(self.context_msg, PostEventRequestContextMsgType0):
            context_msg = self.context_msg.to_dict()
        else:
            context_msg = self.context_msg

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "content": content,
                "senderType": sender_type,
            }
        )
        if client_msg is not UNSET:
            field_dict["clientMsg"] = client_msg
        if agent_msg is not UNSET:
            field_dict["agentMsg"] = agent_msg
        if context_msg is not UNSET:
            field_dict["contextMsg"] = context_msg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_event_request_context_msg_type_0 import PostEventRequestContextMsgType0

        d = dict(src_dict)
        type_ = EventType(d.pop("type"))

        content = d.pop("content")

        sender_type = SenderType(d.pop("senderType"))

        client_msg = d.pop("clientMsg", UNSET)

        agent_msg = d.pop("agentMsg", UNSET)

        def _parse_context_msg(data: object) -> None | PostEventRequestContextMsgType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_msg_type_0 = PostEventRequestContextMsgType0.from_dict(data)

                return context_msg_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostEventRequestContextMsgType0 | Unset, data)

        context_msg = _parse_context_msg(d.pop("contextMsg", UNSET))

        post_event_request = cls(
            type_=type_,
            content=content,
            sender_type=sender_type,
            client_msg=client_msg,
            agent_msg=agent_msg,
            context_msg=context_msg,
        )

        return post_event_request
