import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.deployment_status import DeploymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knative_condition import KnativeCondition


T = TypeVar("T", bound="ModelDeploymentStatusResponse")


@_attrs_define
class ModelDeploymentStatusResponse:
    """
    Attributes:
        name (str):
        id (UUID):
        status (DeploymentStatus):
        is_service_ready (bool):
        is_model_scaled_to_zero (bool):
        has_active_pods (bool):
        is_fully_deployed (bool):
        is_deploying (bool):
        has_failed (bool):
        deployment_id (Union[None, Unset, str]):
        service_url (Union[None, Unset, str]):
        conditions (Union[None, Unset, list['KnativeCondition']]):
        error_message (Union[None, Unset, str]):
        last_updated_at (Union[None, Unset, datetime.datetime]):
        active_revision (Union[None, Unset, str]):
    """

    name: str
    id: UUID
    status: DeploymentStatus
    is_service_ready: bool
    is_model_scaled_to_zero: bool
    has_active_pods: bool
    is_fully_deployed: bool
    is_deploying: bool
    has_failed: bool
    deployment_id: Union[None, Unset, str] = UNSET
    service_url: Union[None, Unset, str] = UNSET
    conditions: Union[None, Unset, list["KnativeCondition"]] = UNSET
    error_message: Union[None, Unset, str] = UNSET
    last_updated_at: Union[None, Unset, datetime.datetime] = UNSET
    active_revision: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        status = self.status.value

        is_service_ready = self.is_service_ready

        is_model_scaled_to_zero = self.is_model_scaled_to_zero

        has_active_pods = self.has_active_pods

        is_fully_deployed = self.is_fully_deployed

        is_deploying = self.is_deploying

        has_failed = self.has_failed

        deployment_id: Union[None, Unset, str]
        if isinstance(self.deployment_id, Unset):
            deployment_id = UNSET
        else:
            deployment_id = self.deployment_id

        service_url: Union[None, Unset, str]
        if isinstance(self.service_url, Unset):
            service_url = UNSET
        else:
            service_url = self.service_url

        conditions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        error_message: Union[None, Unset, str]
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        last_updated_at: Union[None, Unset, str]
        if isinstance(self.last_updated_at, Unset):
            last_updated_at = UNSET
        elif isinstance(self.last_updated_at, datetime.datetime):
            last_updated_at = self.last_updated_at.isoformat()
        else:
            last_updated_at = self.last_updated_at

        active_revision: Union[None, Unset, str]
        if isinstance(self.active_revision, Unset):
            active_revision = UNSET
        else:
            active_revision = self.active_revision

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "id": id,
                "status": status,
                "isServiceReady": is_service_ready,
                "isModelScaledToZero": is_model_scaled_to_zero,
                "hasActivePods": has_active_pods,
                "isFullyDeployed": is_fully_deployed,
                "isDeploying": is_deploying,
                "hasFailed": has_failed,
            }
        )
        if deployment_id is not UNSET:
            field_dict["deploymentId"] = deployment_id
        if service_url is not UNSET:
            field_dict["serviceUrl"] = service_url
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if active_revision is not UNSET:
            field_dict["activeRevision"] = active_revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knative_condition import KnativeCondition

        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        status = DeploymentStatus(d.pop("status"))

        is_service_ready = d.pop("isServiceReady")

        is_model_scaled_to_zero = d.pop("isModelScaledToZero")

        has_active_pods = d.pop("hasActivePods")

        is_fully_deployed = d.pop("isFullyDeployed")

        is_deploying = d.pop("isDeploying")

        has_failed = d.pop("hasFailed")

        def _parse_deployment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deployment_id = _parse_deployment_id(d.pop("deploymentId", UNSET))

        def _parse_service_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_url = _parse_service_url(d.pop("serviceUrl", UNSET))

        def _parse_conditions(data: object) -> Union[None, Unset, list["KnativeCondition"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = KnativeCondition.from_dict(conditions_type_0_item_data)

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["KnativeCondition"]], data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_last_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_at_type_0 = isoparse(data)

                return last_updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_updated_at = _parse_last_updated_at(d.pop("lastUpdatedAt", UNSET))

        def _parse_active_revision(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        active_revision = _parse_active_revision(d.pop("activeRevision", UNSET))

        model_deployment_status_response = cls(
            name=name,
            id=id,
            status=status,
            is_service_ready=is_service_ready,
            is_model_scaled_to_zero=is_model_scaled_to_zero,
            has_active_pods=has_active_pods,
            is_fully_deployed=is_fully_deployed,
            is_deploying=is_deploying,
            has_failed=has_failed,
            deployment_id=deployment_id,
            service_url=service_url,
            conditions=conditions,
            error_message=error_message,
            last_updated_at=last_updated_at,
            active_revision=active_revision,
        )

        return model_deployment_status_response
