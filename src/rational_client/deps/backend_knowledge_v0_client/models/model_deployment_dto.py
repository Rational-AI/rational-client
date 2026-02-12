from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.deployment_status import DeploymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_parameters import DeploymentParameters


T = TypeVar("T", bound="ModelDeploymentDto")


@_attrs_define
class ModelDeploymentDto:
    """
    Attributes:
        id (UUID):
        deployment_id (str):
        model_id (UUID):
        model_name (str):
        status (DeploymentStatus):
        gpu_count (int):
        created_at (datetime.datetime):
        service_url (None | str | Unset):
        last_used_at (datetime.datetime | None | Unset):
        error_message (None | str | Unset):
        parameters (DeploymentParameters | Unset):
        hugging_face_id (None | str | Unset):
    """

    id: UUID
    deployment_id: str
    model_id: UUID
    model_name: str
    status: DeploymentStatus
    gpu_count: int
    created_at: datetime.datetime
    service_url: None | str | Unset = UNSET
    last_used_at: datetime.datetime | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    parameters: DeploymentParameters | Unset = UNSET
    hugging_face_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deployment_id = self.deployment_id

        model_id = str(self.model_id)

        model_name = self.model_name

        status = self.status.value

        gpu_count = self.gpu_count

        created_at = self.created_at.isoformat()

        service_url: None | str | Unset
        if isinstance(self.service_url, Unset):
            service_url = UNSET
        else:
            service_url = self.service_url

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        hugging_face_id: None | str | Unset
        if isinstance(self.hugging_face_id, Unset):
            hugging_face_id = UNSET
        else:
            hugging_face_id = self.hugging_face_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "deploymentId": deployment_id,
                "modelId": model_id,
                "modelName": model_name,
                "status": status,
                "gpuCount": gpu_count,
                "createdAt": created_at,
            }
        )
        if service_url is not UNSET:
            field_dict["serviceUrl"] = service_url
        if last_used_at is not UNSET:
            field_dict["lastUsedAt"] = last_used_at
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if hugging_face_id is not UNSET:
            field_dict["huggingFaceId"] = hugging_face_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_parameters import DeploymentParameters

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deployment_id = d.pop("deploymentId")

        model_id = UUID(d.pop("modelId"))

        model_name = d.pop("modelName")

        status = DeploymentStatus(d.pop("status"))

        gpu_count = d.pop("gpuCount")

        created_at = isoparse(d.pop("createdAt"))

        def _parse_service_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_url = _parse_service_url(d.pop("serviceUrl", UNSET))

        def _parse_last_used_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = isoparse(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("lastUsedAt", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        _parameters = d.pop("parameters", UNSET)
        parameters: DeploymentParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = DeploymentParameters.from_dict(_parameters)

        def _parse_hugging_face_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hugging_face_id = _parse_hugging_face_id(d.pop("huggingFaceId", UNSET))

        model_deployment_dto = cls(
            id=id,
            deployment_id=deployment_id,
            model_id=model_id,
            model_name=model_name,
            status=status,
            gpu_count=gpu_count,
            created_at=created_at,
            service_url=service_url,
            last_used_at=last_used_at,
            error_message=error_message,
            parameters=parameters,
            hugging_face_id=hugging_face_id,
        )

        return model_deployment_dto
