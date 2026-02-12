from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.temporal_workflow_status import TemporalWorkflowStatus
from ..models.temporal_workflow_type import TemporalWorkflowType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateKnowledgeSyncJobRequest")


@_attrs_define
class CreateKnowledgeSyncJobRequest:
    """
    Attributes:
        temporal_workflow_id (str):
        temporal_run_id (str):
        workflow_type (TemporalWorkflowType):
        workflow_status (TemporalWorkflowStatus | Unset):
        last_error (None | str | Unset):
        tries (int | None | Unset):
    """

    temporal_workflow_id: str
    temporal_run_id: str
    workflow_type: TemporalWorkflowType
    workflow_status: TemporalWorkflowStatus | Unset = UNSET
    last_error: None | str | Unset = UNSET
    tries: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        temporal_workflow_id = self.temporal_workflow_id

        temporal_run_id = self.temporal_run_id

        workflow_type = self.workflow_type.value

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "temporalWorkflowId": temporal_workflow_id,
                "temporalRunId": temporal_run_id,
                "workflowType": workflow_type,
            }
        )
        if workflow_status is not UNSET:
            field_dict["workflowStatus"] = workflow_status
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if tries is not UNSET:
            field_dict["tries"] = tries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        temporal_workflow_id = d.pop("temporalWorkflowId")

        temporal_run_id = d.pop("temporalRunId")

        workflow_type = TemporalWorkflowType(d.pop("workflowType"))

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

        create_knowledge_sync_job_request = cls(
            temporal_workflow_id=temporal_workflow_id,
            temporal_run_id=temporal_run_id,
            workflow_type=workflow_type,
            workflow_status=workflow_status,
            last_error=last_error,
            tries=tries,
        )

        return create_knowledge_sync_job_request
