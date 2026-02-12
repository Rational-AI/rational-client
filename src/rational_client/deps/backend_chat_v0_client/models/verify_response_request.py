from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyResponseRequest")


@_attrs_define
class VerifyResponseRequest:
    """
    Attributes:
        text (str):
        message_id (None | Unset | UUID):
        knowledge_id (None | Unset | UUID):
    """

    text: str
    message_id: None | Unset | UUID = UNSET
    knowledge_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        elif isinstance(self.message_id, UUID):
            message_id = str(self.message_id)
        else:
            message_id = self.message_id

        knowledge_id: None | str | Unset
        if isinstance(self.knowledge_id, Unset):
            knowledge_id = UNSET
        elif isinstance(self.knowledge_id, UUID):
            knowledge_id = str(self.knowledge_id)
        else:
            knowledge_id = self.knowledge_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
            }
        )
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if knowledge_id is not UNSET:
            field_dict["knowledgeId"] = knowledge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        def _parse_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                message_id_type_0 = UUID(data)

                return message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        message_id = _parse_message_id(d.pop("messageId", UNSET))

        def _parse_knowledge_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                knowledge_id_type_0 = UUID(data)

                return knowledge_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        knowledge_id = _parse_knowledge_id(d.pop("knowledgeId", UNSET))

        verify_response_request = cls(
            text=text,
            message_id=message_id,
            knowledge_id=knowledge_id,
        )

        return verify_response_request
