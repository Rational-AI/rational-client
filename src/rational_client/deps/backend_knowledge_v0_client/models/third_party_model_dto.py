from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_purpose import ModelPurpose
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_pricing_dto import ModelPricingDto


T = TypeVar("T", bound="ThirdPartyModelDto")


@_attrs_define
class ThirdPartyModelDto:
    """
    Attributes:
        discriminator (str):
        id (UUID):
        name (str):
        model_identifier (str):
        purpose (ModelPurpose):
        pricing (ModelPricingDto):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        supports_function_calling (bool):
        supports_vision (bool):
        capabilities (list[str]):
        is_deprecated (bool):
        description (None | str | Unset):
        proxy_id (None | Unset | UUID):
        max_context_length (int | None | Unset):
        max_output_tokens (int | None | Unset):
    """

    discriminator: str
    id: UUID
    name: str
    model_identifier: str
    purpose: ModelPurpose
    pricing: ModelPricingDto
    created_at: datetime.datetime
    updated_at: datetime.datetime
    supports_function_calling: bool
    supports_vision: bool
    capabilities: list[str]
    is_deprecated: bool
    description: None | str | Unset = UNSET
    proxy_id: None | Unset | UUID = UNSET
    max_context_length: int | None | Unset = UNSET
    max_output_tokens: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discriminator = self.discriminator

        id = str(self.id)

        name = self.name

        model_identifier = self.model_identifier

        purpose = self.purpose.value

        pricing = self.pricing.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        supports_function_calling = self.supports_function_calling

        supports_vision = self.supports_vision

        capabilities = self.capabilities

        is_deprecated = self.is_deprecated

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        proxy_id: None | str | Unset
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        elif isinstance(self.proxy_id, UUID):
            proxy_id = str(self.proxy_id)
        else:
            proxy_id = self.proxy_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discriminator": discriminator,
                "id": id,
                "name": name,
                "modelIdentifier": model_identifier,
                "purpose": purpose,
                "pricing": pricing,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "supportsFunctionCalling": supports_function_calling,
                "supportsVision": supports_vision,
                "capabilities": capabilities,
                "isDeprecated": is_deprecated,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id
        if max_context_length is not UNSET:
            field_dict["maxContextLength"] = max_context_length
        if max_output_tokens is not UNSET:
            field_dict["maxOutputTokens"] = max_output_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_pricing_dto import ModelPricingDto

        d = dict(src_dict)
        discriminator = d.pop("discriminator")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        model_identifier = d.pop("modelIdentifier")

        purpose = ModelPurpose(d.pop("purpose"))

        pricing = ModelPricingDto.from_dict(d.pop("pricing"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        supports_function_calling = d.pop("supportsFunctionCalling")

        supports_vision = d.pop("supportsVision")

        capabilities = cast(list[str], d.pop("capabilities"))

        is_deprecated = d.pop("isDeprecated")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_proxy_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_id_type_0 = UUID(data)

                return proxy_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_id = _parse_proxy_id(d.pop("proxyId", UNSET))

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

        third_party_model_dto = cls(
            discriminator=discriminator,
            id=id,
            name=name,
            model_identifier=model_identifier,
            purpose=purpose,
            pricing=pricing,
            created_at=created_at,
            updated_at=updated_at,
            supports_function_calling=supports_function_calling,
            supports_vision=supports_vision,
            capabilities=capabilities,
            is_deprecated=is_deprecated,
            description=description,
            proxy_id=proxy_id,
            max_context_length=max_context_length,
            max_output_tokens=max_output_tokens,
        )

        third_party_model_dto.additional_properties = d
        return third_party_model_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
