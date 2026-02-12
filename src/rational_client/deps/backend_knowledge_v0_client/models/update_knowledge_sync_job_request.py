from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.temporal_workflow_status import TemporalWorkflowStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKnowledgeSyncJobRequest")


@_attrs_define
class UpdateKnowledgeSyncJobRequest:
    """
    Attributes:
        workflow_status (TemporalWorkflowStatus | Unset):
        last_error (None | str | Unset):
        tries (int | None | Unset):
        completed_at (datetime.datetime | None | Unset):
    """

    workflow_status: TemporalWorkflowStatus | Unset = UNSET
    last_error: None | str | Unset = UNSET
    tries: int | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workflow_status: str | Unset = UNSET
        if not isinstance(self.workflow_status, Unset):
            workflow_status = self.workflow_status.value

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        tries: int | None | Unset
        if isinstance(self.tries, Unset):
            tries = UNSET
        else:
            tries = self.tries

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if workflow_status is not UNSET:
            field_dict["workflowStatus"] = workflow_status
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if tries is not UNSET:
            field_dict["tries"] = tries
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _workflow_status = d.pop("workflowStatus", UNSET)
        workflow_status: TemporalWorkflowStatus | Unset
        if isinstance(_workflow_status, Unset):
            workflow_status = UNSET
        else:
            workflow_status = TemporalWorkflowStatus(_workflow_status)

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

        def _parse_tries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tries = _parse_tries(d.pop("tries", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        update_knowledge_sync_job_request = cls(
            workflow_status=workflow_status,
            last_error=last_error,
            tries=tries,
            completed_at=completed_at,
        )

        return update_knowledge_sync_job_request
