from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="KnativeCondition")


@_attrs_define
class KnativeCondition:
    """
    Attributes:
        type_ (str):
        status (str):
        reason (str):
        message (str):
        last_transition_time (datetime.datetime):
    """

    type_: str
    status: str
    reason: str
    message: str
    last_transition_time: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        status = self.status

        reason = self.reason

        message = self.message

        last_transition_time = self.last_transition_time.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "status": status,
                "reason": reason,
                "message": message,
                "lastTransitionTime": last_transition_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        status = d.pop("status")

        reason = d.pop("reason")

        message = d.pop("message")

        last_transition_time = isoparse(d.pop("lastTransitionTime"))

        knative_condition = cls(
            type_=type_,
            status=status,
            reason=reason,
            message=message,
            last_transition_time=last_transition_time,
        )

        return knative_condition
