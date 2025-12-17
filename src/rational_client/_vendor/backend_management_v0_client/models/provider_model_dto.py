from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        context_length (Union[None, Unset, int]):
        max_tokens (Union[None, Unset, int]):
        input_cost_per_1_k (Union[None, Unset, float]):
        output_cost_per_1_k (Union[None, Unset, float]):
        input_token_cost (Union[None, Unset, float]):
        output_token_cost (Union[None, Unset, float]):
        is_fine_tunable (Union[None, Unset, bool]):
        is_deprecated (Union[None, Unset, bool]):
        capabilities (Union[None, Unset, list[str]]):
        source (Union[None, Unset, str]):
    """

    id: str
    name: str
    provider: str
    description: str
    context_length: Union[None, Unset, int] = UNSET
    max_tokens: Union[None, Unset, int] = UNSET
    input_cost_per_1_k: Union[None, Unset, float] = UNSET
    output_cost_per_1_k: Union[None, Unset, float] = UNSET
    input_token_cost: Union[None, Unset, float] = UNSET
    output_token_cost: Union[None, Unset, float] = UNSET
    is_fine_tunable: Union[None, Unset, bool] = UNSET
    is_deprecated: Union[None, Unset, bool] = UNSET
    capabilities: Union[None, Unset, list[str]] = UNSET
    source: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        provider = self.provider

        description = self.description

        context_length: Union[None, Unset, int]
        if isinstance(self.context_length, Unset):
            context_length = UNSET
        else:
            context_length = self.context_length

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        input_cost_per_1_k: Union[None, Unset, float]
        if isinstance(self.input_cost_per_1_k, Unset):
            input_cost_per_1_k = UNSET
        else:
            input_cost_per_1_k = self.input_cost_per_1_k

        output_cost_per_1_k: Union[None, Unset, float]
        if isinstance(self.output_cost_per_1_k, Unset):
            output_cost_per_1_k = UNSET
        else:
            output_cost_per_1_k = self.output_cost_per_1_k

        input_token_cost: Union[None, Unset, float]
        if isinstance(self.input_token_cost, Unset):
            input_token_cost = UNSET
        else:
            input_token_cost = self.input_token_cost

        output_token_cost: Union[None, Unset, float]
        if isinstance(self.output_token_cost, Unset):
            output_token_cost = UNSET
        else:
            output_token_cost = self.output_token_cost

        is_fine_tunable: Union[None, Unset, bool]
        if isinstance(self.is_fine_tunable, Unset):
            is_fine_tunable = UNSET
        else:
            is_fine_tunable = self.is_fine_tunable

        is_deprecated: Union[None, Unset, bool]
        if isinstance(self.is_deprecated, Unset):
            is_deprecated = UNSET
        else:
            is_deprecated = self.is_deprecated

        capabilities: Union[None, Unset, list[str]]
        if isinstance(self.capabilities, Unset):
            capabilities = UNSET
        elif isinstance(self.capabilities, list):
            capabilities = self.capabilities

        else:
            capabilities = self.capabilities

        source: Union[None, Unset, str]
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

        def _parse_context_length(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        context_length = _parse_context_length(d.pop("contextLength", UNSET))

        def _parse_max_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_tokens = _parse_max_tokens(d.pop("maxTokens", UNSET))

        def _parse_input_cost_per_1_k(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        input_cost_per_1_k = _parse_input_cost_per_1_k(d.pop("inputCostPer1k", UNSET))

        def _parse_output_cost_per_1_k(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        output_cost_per_1_k = _parse_output_cost_per_1_k(d.pop("outputCostPer1k", UNSET))

        def _parse_input_token_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        input_token_cost = _parse_input_token_cost(d.pop("inputTokenCost", UNSET))

        def _parse_output_token_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        output_token_cost = _parse_output_token_cost(d.pop("outputTokenCost", UNSET))

        def _parse_is_fine_tunable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_fine_tunable = _parse_is_fine_tunable(d.pop("isFineTunable", UNSET))

        def _parse_is_deprecated(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_deprecated = _parse_is_deprecated(d.pop("isDeprecated", UNSET))

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

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
