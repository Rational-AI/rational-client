from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderModelDto")


@_attrs_define
class ProviderModelDto:
    """
    Attributes:
        id (str):
        name (str):
        provider (str):
        description (str):
        context_length (int | None | Unset):
        max_tokens (int | None | Unset):
        input_cost_per_1_k (float | None | Unset):
        output_cost_per_1_k (float | None | Unset):
        input_token_cost (float | None | Unset):
        output_token_cost (float | None | Unset):
        is_fine_tunable (bool | None | Unset):
        is_deprecated (bool | None | Unset):
        capabilities (list[str] | None | Unset):
        source (None | str | Unset):
    """

    id: str
    name: str
    provider: str
    description: str
    context_length: int | None | Unset = UNSET
    max_tokens: int | None | Unset = UNSET
    input_cost_per_1_k: float | None | Unset = UNSET
    output_cost_per_1_k: float | None | Unset = UNSET
    input_token_cost: float | None | Unset = UNSET
    output_token_cost: float | None | Unset = UNSET
    is_fine_tunable: bool | None | Unset = UNSET
    is_deprecated: bool | None | Unset = UNSET
    capabilities: list[str] | None | Unset = UNSET
    source: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        provider = self.provider

        description = self.description

        context_length: int | None | Unset
        if isinstance(self.context_length, Unset):
            context_length = UNSET
        else:
            context_length = self.context_length

        max_tokens: int | None | Unset
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        input_cost_per_1_k: float | None | Unset
        if isinstance(self.input_cost_per_1_k, Unset):
            input_cost_per_1_k = UNSET
        else:
            input_cost_per_1_k = self.input_cost_per_1_k

        output_cost_per_1_k: float | None | Unset
        if isinstance(self.output_cost_per_1_k, Unset):
            output_cost_per_1_k = UNSET
        else:
            output_cost_per_1_k = self.output_cost_per_1_k

        input_token_cost: float | None | Unset
        if isinstance(self.input_token_cost, Unset):
            input_token_cost = UNSET
        else:
            input_token_cost = self.input_token_cost

        output_token_cost: float | None | Unset
        if isinstance(self.output_token_cost, Unset):
            output_token_cost = UNSET
        else:
            output_token_cost = self.output_token_cost

        is_fine_tunable: bool | None | Unset
        if isinstance(self.is_fine_tunable, Unset):
            is_fine_tunable = UNSET
        else:
            is_fine_tunable = self.is_fine_tunable

        is_deprecated: bool | None | Unset
        if isinstance(self.is_deprecated, Unset):
            is_deprecated = UNSET
        else:
            is_deprecated = self.is_deprecated

        capabilities: list[str] | None | Unset
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, list):
            capabilities = self.capabilities

        else:
            capabilities = self.capabilities

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "provider": provider,
                "description": description,
            }
        )
        if context_length is not UNSET:
            field_dict["contextLength"] = context_length
        if max_tokens is not UNSET:
            field_dict["maxTokens"] = max_tokens
        if input_cost_per_1_k is not UNSET:
            field_dict["inputCostPer1k"] = input_cost_per_1_k
        if output_cost_per_1_k is not UNSET:
            field_dict["outputCostPer1k"] = output_cost_per_1_k
        if input_token_cost is not UNSET:
            field_dict["inputTokenCost"] = input_token_cost
        if output_token_cost is not UNSET:
            field_dict["outputTokenCost"] = output_token_cost
        if is_fine_tunable is not UNSET:
            field_dict["isFineTunable"] = is_fine_tunable
        if is_deprecated is not UNSET:
            field_dict["isDeprecated"] = is_deprecated
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        provider = d.pop("provider")

        description = d.pop("description")

        def _parse_context_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        context_length = _parse_context_length(d.pop("contextLength", UNSET))

        def _parse_max_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_tokens = _parse_max_tokens(d.pop("maxTokens", UNSET))

        def _parse_input_cost_per_1_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_cost_per_1_k = _parse_input_cost_per_1_k(d.pop("inputCostPer1k", UNSET))

        def _parse_output_cost_per_1_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_cost_per_1_k = _parse_output_cost_per_1_k(d.pop("outputCostPer1k", UNSET))

        def _parse_input_token_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        input_token_cost = _parse_input_token_cost(d.pop("inputTokenCost", UNSET))

        def _parse_output_token_cost(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        output_token_cost = _parse_output_token_cost(d.pop("outputTokenCost", UNSET))

        def _parse_is_fine_tunable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_fine_tunable = _parse_is_fine_tunable(d.pop("isFineTunable", UNSET))

        def _parse_is_deprecated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_deprecated = _parse_is_deprecated(d.pop("isDeprecated", UNSET))

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

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        provider_model_dto = cls(
            id=id,
            name=name,
            provider=provider,
            description=description,
            context_length=context_length,
            max_tokens=max_tokens,
            input_cost_per_1_k=input_cost_per_1_k,
            output_cost_per_1_k=output_cost_per_1_k,
            input_token_cost=input_token_cost,
            output_token_cost=output_token_cost,
            is_fine_tunable=is_fine_tunable,
            is_deprecated=is_deprecated,
            capabilities=capabilities,
            source=source,
        )

        return provider_model_dto
