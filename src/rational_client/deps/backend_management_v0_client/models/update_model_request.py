from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_default_parameters import ModelDefaultParameters
    from ..models.model_pricing_dto import ModelPricingDto
    from ..models.model_request_override import ModelRequestOverride


T = TypeVar("T", bound="UpdateModelRequest")


@_attrs_define
class UpdateModelRequest:
    """
    Attributes:
        name (str | Unset):
        description (None | str | Unset):
        model_identifier (str | Unset):
        overrides (list[ModelRequestOverride] | Unset):
        pricing (ModelPricingDto | Unset):
        default_parameters (ModelDefaultParameters | Unset):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    model_identifier: str | Unset = UNSET
    overrides: list[ModelRequestOverride] | Unset = UNSET
    pricing: ModelPricingDto | Unset = UNSET
    default_parameters: ModelDefaultParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        model_identifier = self.model_identifier

        overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = []
            for overrides_item_data in self.overrides:
                overrides_item = overrides_item_data.to_dict()
                overrides.append(overrides_item)

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        default_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_parameters, Unset):
            default_parameters = self.default_parameters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if model_identifier is not UNSET:
            field_dict["modelIdentifier"] = model_identifier
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if default_parameters is not UNSET:
            field_dict["defaultParameters"] = default_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_default_parameters import ModelDefaultParameters
        from ..models.model_pricing_dto import ModelPricingDto
        from ..models.model_request_override import ModelRequestOverride

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        model_identifier = d.pop("modelIdentifier", UNSET)

        _overrides = d.pop("overrides", UNSET)
        overrides: list[ModelRequestOverride] | Unset = UNSET
        if _overrides is not UNSET:
            overrides = []
            for overrides_item_data in _overrides:
                overrides_item = ModelRequestOverride.from_dict(overrides_item_data)

                overrides.append(overrides_item)

        _pricing = d.pop("pricing", UNSET)
        pricing: ModelPricingDto | Unset
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = ModelPricingDto.from_dict(_pricing)

        _default_parameters = d.pop("defaultParameters", UNSET)
        default_parameters: ModelDefaultParameters | Unset
        if isinstance(_default_parameters, Unset):
            default_parameters = UNSET
        else:
            default_parameters = ModelDefaultParameters.from_dict(_default_parameters)

        update_model_request = cls(
            name=name,
            description=description,
            model_identifier=model_identifier,
            overrides=overrides,
            pricing=pricing,
            default_parameters=default_parameters,
        )

        return update_model_request
