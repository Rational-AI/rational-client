import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.temporal_workflow_status import TemporalWorkflowStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKnowledgeSyncJobRequest")


@_attrs_define
class UpdateKnowledgeSyncJobRequest:
    """
    Attributes:
        workflow_status (Union[Unset, TemporalWorkflowStatus]):
        last_error (Union[None, Unset, str]):
        tries (Union[None, Unset, int]):
        completed_at (Union[None, Unset, datetime.datetime]):
    """

    workflow_status: Union[Unset, TemporalWorkflowStatus] = UNSET
    last_error: Union[None, Unset, str] = UNSET
    tries: Union[None, Unset, int] = UNSET
    completed_at: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        workflow_status: Union[Unset, str] = UNSET
        if not isinstance(self.workflow_status, Unset):
            workflow_status = self.workflow_status.value

        last_error: Union[None, Unset, str]
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        tries: Union[None, Unset, int]
        if isinstance(self.tries, Unset):
            tries = UNSET
        else:
            tries = self.tries

        completed_at: Union[None, Unset, str]
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
        workflow_status: Union[Unset, TemporalWorkflowStatus]
        if isinstance(_workflow_status, Unset):
            workflow_status = UNSET
        else:
            workflow_status = TemporalWorkflowStatus(_workflow_status)

        def _parse_last_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

        def _parse_tries(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tries = _parse_tries(d.pop("tries", UNSET))

        def _parse_completed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        update_knowledge_sync_job_request = cls(
            workflow_status=workflow_status,
            last_error=last_error,
            tries=tries,
            completed_at=completed_at,
        )

        return update_knowledge_sync_job_request
