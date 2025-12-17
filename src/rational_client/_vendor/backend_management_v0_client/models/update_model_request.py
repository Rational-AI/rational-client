from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        model_identifier (Union[Unset, str]):
        overrides (Union[Unset, list['ModelRequestOverride']]):
        pricing (Union[Unset, ModelPricingDto]):
        default_parameters (Union[Unset, ModelDefaultParameters]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    model_identifier: Union[Unset, str] = UNSET
    overrides: Union[Unset, list["ModelRequestOverride"]] = UNSET
    pricing: Union[Unset, "ModelPricingDto"] = UNSET
    default_parameters: Union[Unset, "ModelDefaultParameters"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        model_identifier = self.model_identifier

        overrides: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = []
            for overrides_item_data in self.overrides:
                overrides_item = overrides_item_data.to_dict()
                overrides.append(overrides_item)

        pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        default_parameters: Union[Unset, dict[str, Any]] = UNSET
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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        model_identifier = d.pop("modelIdentifier", UNSET)

        overrides = []
        _overrides = d.pop("overrides", UNSET)
        for overrides_item_data in _overrides or []:
            overrides_item = ModelRequestOverride.from_dict(overrides_item_data)

            overrides.append(overrides_item)

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, ModelPricingDto]
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = ModelPricingDto.from_dict(_pricing)

        _default_parameters = d.pop("defaultParameters", UNSET)
        default_parameters: Union[Unset, ModelDefaultParameters]
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
