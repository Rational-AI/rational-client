from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.model_purpose import ModelPurpose
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_pricing_dto import ModelPricingDto
    from ..models.model_request_override import ModelRequestOverride


T = TypeVar("T", bound="CreateModelRequest")


@_attrs_define
class CreateModelRequest:
    """
    Attributes:
        proxy_id (UUID):
        provider_model_identifier (str):
        model_identifier (Union[None, Unset, str]):
        overrides (Union[None, Unset, list['ModelRequestOverride']]):
        name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        purpose (Union[Unset, ModelPurpose]):
        pricing (Union[Unset, ModelPricingDto]):
        max_context_length (Union[None, Unset, int]):
        max_output_tokens (Union[None, Unset, int]):
        supports_function_calling (Union[None, Unset, bool]):
        supports_vision (Union[None, Unset, bool]):
        capabilities (Union[None, Unset, list[str]]):
        is_deprecated (Union[None, Unset, bool]):
    """

    proxy_id: UUID
    provider_model_identifier: str
    model_identifier: Union[None, Unset, str] = UNSET
    overrides: Union[None, Unset, list["ModelRequestOverride"]] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    purpose: Union[Unset, ModelPurpose] = UNSET
    pricing: Union[Unset, "ModelPricingDto"] = UNSET
    max_context_length: Union[None, Unset, int] = UNSET
    max_output_tokens: Union[None, Unset, int] = UNSET
    supports_function_calling: Union[None, Unset, bool] = UNSET
    supports_vision: Union[None, Unset, bool] = UNSET
    capabilities: Union[None, Unset, list[str]] = UNSET
    is_deprecated: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        proxy_id = str(self.proxy_id)

        provider_model_identifier = self.provider_model_identifier

        model_identifier: Union[None, Unset, str]
        if isinstance(self.model_identifier, Unset):
            model_identifier = UNSET
        else:
            model_identifier = self.model_identifier

        overrides: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.overrides, Unset):
            overrides = UNSET
        elif isinstance(self.overrides, list):
            overrides = []
            for overrides_type_0_item_data in self.overrides:
                overrides_type_0_item = overrides_type_0_item_data.to_dict()
                overrides.append(overrides_type_0_item)

        else:
            overrides = self.overrides

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        purpose: Union[Unset, str] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        pricing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        max_context_length: Union[None, Unset, int]
        if isinstance(self.max_context_length, Unset):
            max_context_length = UNSET
        else:
            max_context_length = self.max_context_length

        max_output_tokens: Union[None, Unset, int]
        if isinstance(self.max_output_tokens, Unset):
            max_output_tokens = UNSET
        else:
            max_output_tokens = self.max_output_tokens

        supports_function_calling: Union[None, Unset, bool]
        if isinstance(self.supports_function_calling, Unset):
            supports_function_calling = UNSET
        else:
            supports_function_calling = self.supports_function_calling

        supports_vision: Union[None, Unset, bool]
        if isinstance(self.supports_vision, Unset):
            supports_vision = UNSET
        else:
            supports_vision = self.supports_vision

        capabilities: Union[None, Unset, list[str]]
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, list):
            capabilities = self.capabilities

        else:
            capabilities = self.capabilities

        is_deprecated: Union[None, Unset, bool]
        if isinstance(self.is_deprecated, Unset):
            is_deprecated = UNSET
        else:
            is_deprecated = self.is_deprecated

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "proxyId": proxy_id,
                "providerModelIdentifier": provider_model_identifier,
            }
        )
        if model_identifier is not UNSET:
            field_dict["modelIdentifier"] = model_identifier
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if max_context_length is not UNSET:
            field_dict["maxContextLength"] = max_context_length
        if max_output_tokens is not UNSET:
            field_dict["maxOutputTokens"] = max_output_tokens
        if supports_function_calling is not UNSET:
            field_dict["supportsFunctionCalling"] = supports_function_calling
        if supports_vision is not UNSET:
            field_dict["supportsVision"] = supports_vision
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if is_deprecated is not UNSET:
            field_dict["isDeprecated"] = is_deprecated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_pricing_dto import ModelPricingDto
        from ..models.model_request_override import ModelRequestOverride

        d = dict(src_dict)
        proxy_id = UUID(d.pop("proxyId"))

        provider_model_identifier = d.pop("providerModelIdentifier")

        def _parse_model_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_identifier = _parse_model_identifier(d.pop("modelIdentifier", UNSET))

        def _parse_overrides(data: object) -> Union[None, Unset, list["ModelRequestOverride"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                overrides_type_0 = []
                _overrides_type_0 = data
                for overrides_type_0_item_data in _overrides_type_0:
                    overrides_type_0_item = ModelRequestOverride.from_dict(overrides_type_0_item_data)

                    overrides_type_0.append(overrides_type_0_item)

                return overrides_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ModelRequestOverride"]], data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, ModelPurpose]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = ModelPurpose(_purpose)

        _pricing = d.pop("pricing", UNSET)
        pricing: Union[Unset, ModelPricingDto]
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = ModelPricingDto.from_dict(_pricing)

        def _parse_max_context_length(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_context_length = _parse_max_context_length(d.pop("maxContextLength", UNSET))

        def _parse_max_output_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_output_tokens = _parse_max_output_tokens(d.pop("maxOutputTokens", UNSET))

        def _parse_supports_function_calling(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        supports_function_calling = _parse_supports_function_calling(d.pop("supportsFunctionCalling", UNSET))

        def _parse_supports_vision(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        supports_vision = _parse_supports_vision(d.pop("supportsVision", UNSET))

        def _parse_capabilities(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                capabilities_type_0 = cast(list[str], data)

                return capabilities_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        capabilities = _parse_capabilities(d.pop("capabilities", UNSET))

        def _parse_is_deprecated(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_deprecated = _parse_is_deprecated(d.pop("isDeprecated", UNSET))

        create_model_request = cls(
            proxy_id=proxy_id,
            provider_model_identifier=provider_model_identifier,
            model_identifier=model_identifier,
            overrides=overrides,
            name=name,
            description=description,
            purpose=purpose,
            pricing=pricing,
            max_context_length=max_context_length,
            max_output_tokens=max_output_tokens,
            supports_function_calling=supports_function_calling,
            supports_vision=supports_vision,
            capabilities=capabilities,
            is_deprecated=is_deprecated,
        )

        return create_model_request
