from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.temporal_workflow_status import TemporalWorkflowStatus
from ..models.temporal_workflow_type import TemporalWorkflowType
from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeSyncJobDto")


@_attrs_define
class KnowledgeSyncJobDto:
    """
    Attributes:
        id (UUID):
        knowledge_id (UUID):
        temporal_workflow_id (str):
        temporal_run_id (str):
        workflow_type (TemporalWorkflowType):
        workflow_status (TemporalWorkflowStatus):
        tries (int):
        rational_resource_ids (list[UUID]):
        created_at (datetime.datetime):
        last_error (None | str | Unset):
        completed_at (datetime.datetime | None | Unset):
    """

    id: UUID
    knowledge_id: UUID
    temporal_workflow_id: str
    temporal_run_id: str
    workflow_type: TemporalWorkflowType
    workflow_status: TemporalWorkflowStatus
    tries: int
    rational_resource_ids: list[UUID]
    created_at: datetime.datetime
    last_error: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        knowledge_id = str(self.knowledge_id)

        temporal_workflow_id = self.temporal_workflow_id

        temporal_run_id = self.temporal_run_id

        workflow_type = self.workflow_type.value

        workflow_status = self.workflow_status.value

        tries = self.tries

        rational_resource_ids = []
        for rational_resource_ids_item_data in self.rational_resource_ids:
            rational_resource_ids_item = str(rational_resource_ids_item_data)
            rational_resource_ids.append(rational_resource_ids_item)

        created_at = self.created_at.isoformat()

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "knowledgeId": knowledge_id,
                "temporalWorkflowId": temporal_workflow_id,
                "temporalRunId": temporal_run_id,
                "workflowType": workflow_type,
                "workflowStatus": workflow_status,
                "tries": tries,
                "rationalResourceIds": rational_resource_ids,
                "createdAt": created_at,
            }
        )
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        knowledge_id = UUID(d.pop("knowledgeId"))

        temporal_workflow_id = d.pop("temporalWorkflowId")

        temporal_run_id = d.pop("temporalRunId")

        workflow_type = TemporalWorkflowType(d.pop("workflowType"))

        workflow_status = TemporalWorkflowStatus(d.pop("workflowStatus"))

        tries = d.pop("tries")

        rational_resource_ids = []
        _rational_resource_ids = d.pop("rationalResourceIds")
        for rational_resource_ids_item_data in _rational_resource_ids:
            rational_resource_ids_item = UUID(rational_resource_ids_item_data)

            rational_resource_ids.append(rational_resource_ids_item)

        created_at = isoparse(d.pop("createdAt"))

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

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

        knowledge_sync_job_dto = cls(
            id=id,
            knowledge_id=knowledge_id,
            temporal_workflow_id=temporal_workflow_id,
            temporal_run_id=temporal_run_id,
            workflow_type=workflow_type,
            workflow_status=workflow_status,
            tries=tries,
            rational_resource_ids=rational_resource_ids,
            created_at=created_at,
            last_error=last_error,
            completed_at=completed_at,
        )

        return knowledge_sync_job_dto
