from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
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
        model_identifier (None | str | Unset):
        overrides (list[ModelRequestOverride] | None | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        purpose (ModelPurpose | Unset):
        pricing (ModelPricingDto | Unset):
        max_context_length (int | None | Unset):
        max_output_tokens (int | None | Unset):
        supports_function_calling (bool | None | Unset):
        supports_vision (bool | None | Unset):
        capabilities (list[str] | None | Unset):
        is_deprecated (bool | None | Unset):
    """

    proxy_id: UUID
    provider_model_identifier: str
    model_identifier: None | str | Unset = UNSET
    overrides: list[ModelRequestOverride] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    purpose: ModelPurpose | Unset = UNSET
    pricing: ModelPricingDto | Unset = UNSET
    max_context_length: int | None | Unset = UNSET
    max_output_tokens: int | None | Unset = UNSET
    supports_function_calling: bool | None | Unset = UNSET
    supports_vision: bool | None | Unset = UNSET
    capabilities: list[str] | None | Unset = UNSET
    is_deprecated: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        proxy_id = str(self.proxy_id)

        provider_model_identifier = self.provider_model_identifier

        model_identifier: None | str | Unset
        if isinstance(self.model_identifier, Unset):
            model_identifier = UNSET
        else:
            model_identifier = self.model_identifier

        overrides: list[dict[str, Any]] | None | Unset
        if isinstance(self.overrides, Unset):
            overrides = UNSET
        elif isinstance(self.overrides, list):
            overrides = []
            for overrides_type_0_item_data in self.overrides:
                overrides_type_0_item = overrides_type_0_item_data.to_dict()
                overrides.append(overrides_type_0_item)

        else:
            overrides = self.overrides

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        max_context_length: int | None | Unset
        if isinstance(self.max_context_length, Unset):
            max_context_length = UNSET
        else:
            max_context_length = self.max_context_length

        max_output_tokens: int | None | Unset
        if isinstance(self.max_output_tokens, Unset):
            max_output_tokens = UNSET
        else:
            max_output_tokens = self.max_output_tokens

        supports_function_calling: bool | None | Unset
        if isinstance(self.supports_function_calling, Unset):
            supports_function_calling = UNSET
        else:
            supports_function_calling = self.supports_function_calling

        supports_vision: bool | None | Unset
        if isinstance(self.supports_vision, Unset):
            supports_vision = UNSET
        else:
            supports_vision = self.supports_vision

        capabilities: list[str] | None | Unset
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, list):
            capabilities = self.capabilities

        else:
            capabilities = self.capabilities

        is_deprecated: bool | None | Unset
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

        def _parse_model_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_identifier = _parse_model_identifier(d.pop("modelIdentifier", UNSET))

        def _parse_overrides(data: object) -> list[ModelRequestOverride] | None | Unset:
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
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ModelRequestOverride] | None | Unset, data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _purpose = d.pop("purpose", UNSET)
        purpose: ModelPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = ModelPurpose(_purpose)

        _pricing = d.pop("pricing", UNSET)
        pricing: ModelPricingDto | Unset
        if isinstance(_pricing, Unset):
            pricing = UNSET
        else:
            pricing = ModelPricingDto.from_dict(_pricing)

        def _parse_max_context_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_context_length = _parse_max_context_length(d.pop("maxContextLength", UNSET))

        def _parse_max_output_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_output_tokens = _parse_max_output_tokens(d.pop("maxOutputTokens", UNSET))

        def _parse_supports_function_calling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_function_calling = _parse_supports_function_calling(d.pop("supportsFunctionCalling", UNSET))

        def _parse_supports_vision(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        supports_vision = _parse_supports_vision(d.pop("supportsVision", UNSET))

        def _parse_capabilities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                capabilities_type_0 = cast(list[str], data)

                return capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        capabilities = _parse_capabilities(d.pop("capabilities", UNSET))

        def _parse_is_deprecated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

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
