from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelPricingDto")


@_attrs_define
class ModelPricingDto:
    """
    Attributes:
        enabled (bool):
        cost_per_request (Union[None, Unset, float]):
        cost_per_second (Union[None, Unset, float]):
        cost_per_input_token (Union[None, Unset, float]):
        cost_per_output_token (Union[None, Unset, float]):
    """

    enabled: bool
    cost_per_request: Union[None, Unset, float] = UNSET
    cost_per_second: Union[None, Unset, float] = UNSET
    cost_per_input_token: Union[None, Unset, float] = UNSET
    cost_per_output_token: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        cost_per_request: Union[None, Unset, float]
        if isinstance(self.cost_per_request, Unset):
            cost_per_request = UNSET
        else:
            cost_per_request = self.cost_per_request

        cost_per_second: Union[None, Unset, float]
        if isinstance(self.cost_per_second, Unset):
            cost_per_second = UNSET
        else:
            cost_per_second = self.cost_per_second

        cost_per_input_token: Union[None, Unset, float]
        if isinstance(self.cost_per_input_token, Unset):
            cost_per_input_token = UNSET
        else:
            cost_per_input_token = self.cost_per_input_token

        cost_per_output_token: Union[None, Unset, float]
        if isinstance(self.cost_per_output_token, Unset):
            cost_per_output_token = UNSET
        else:
            cost_per_output_token = self.cost_per_output_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if cost_per_request is not UNSET:
            field_dict["costPerRequest"] = cost_per_request
        if cost_per_second is not UNSET:
            field_dict["costPerSecond"] = cost_per_second
        if cost_per_input_token is not UNSET:
            field_dict["costPerInputToken"] = cost_per_input_token
        if cost_per_output_token is not UNSET:
            field_dict["costPerOutputToken"] = cost_per_output_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_cost_per_request(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_per_request = _parse_cost_per_request(d.pop("costPerRequest", UNSET))

        def _parse_cost_per_second(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_per_second = _parse_cost_per_second(d.pop("costPerSecond", UNSET))

        def _parse_cost_per_input_token(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_per_input_token = _parse_cost_per_input_token(d.pop("costPerInputToken", UNSET))

        def _parse_cost_per_output_token(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_per_output_token = _parse_cost_per_output_token(d.pop("costPerOutputToken", UNSET))

        model_pricing_dto = cls(
            enabled=enabled,
            cost_per_request=cost_per_request,
            cost_per_second=cost_per_second,
            cost_per_input_token=cost_per_input_token,
            cost_per_output_token=cost_per_output_token,
        )

        return model_pricing_dto
