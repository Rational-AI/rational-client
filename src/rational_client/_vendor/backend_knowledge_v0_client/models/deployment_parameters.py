from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentParameters")


@_attrs_define
class DeploymentParameters:
    """
    Attributes:
        force_deployment (bool):
        temperature (Union[None, Unset, float]):
        top_p (Union[None, Unset, float]):
        top_k (Union[None, Unset, float]):
        min_p (Union[None, Unset, float]):
        repetition_penalty (Union[None, Unset, float]):
        max_output_tokens (Union[None, Unset, int]):
        deployment_tier (Union[None, Unset, str]):
        finetuning_id (Union[None, UUID, Unset]):
        adapter_name (Union[None, Unset, str]):
        adapter_scale (Union[None, Unset, float]):
    """

    force_deployment: bool
    temperature: Union[None, Unset, float] = UNSET
    top_p: Union[None, Unset, float] = UNSET
    top_k: Union[None, Unset, float] = UNSET
    min_p: Union[None, Unset, float] = UNSET
    repetition_penalty: Union[None, Unset, float] = UNSET
    max_output_tokens: Union[None, Unset, int] = UNSET
    deployment_tier: Union[None, Unset, str] = UNSET
    finetuning_id: Union[None, UUID, Unset] = UNSET
    adapter_name: Union[None, Unset, str] = UNSET
    adapter_scale: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        force_deployment = self.force_deployment

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: Union[None, Unset, float]
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        top_k: Union[None, Unset, float]
        if isinstance(self.top_k, Unset):
            top_k = UNSET
        else:
            top_k = self.top_k

        min_p: Union[None, Unset, float]
        if isinstance(self.min_p, Unset):
            min_p = UNSET
        else:
            min_p = self.min_p

        repetition_penalty: Union[None, Unset, float]
        if isinstance(self.repetition_penalty, Unset):
            repetition_penalty = UNSET
        else:
            repetition_penalty = self.repetition_penalty

        max_output_tokens: Union[None, Unset, int]
        if isinstance(self.max_output_tokens, Unset):
            max_output_tokens = UNSET
        else:
            max_output_tokens = self.max_output_tokens

        deployment_tier: Union[None, Unset, str]
        if isinstance(self.deployment_tier, Unset):
            deployment_tier = UNSET
        else:
            deployment_tier = self.deployment_tier

        finetuning_id: Union[None, Unset, str]
        if isinstance(self.finetuning_id, Unset):
            finetuning_id = UNSET
        elif isinstance(self.finetuning_id, UUID):
            finetuning_id = str(self.finetuning_id)
        else:
            finetuning_id = self.finetuning_id

        adapter_name: Union[None, Unset, str]
        if isinstance(self.adapter_name, Unset):
            adapter_name = UNSET
        else:
            adapter_name = self.adapter_name

        adapter_scale: Union[None, Unset, float]
        if isinstance(self.adapter_scale, Unset):
            adapter_scale = UNSET
        else:
            adapter_scale = self.adapter_scale

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "forceDeployment": force_deployment,
            }
        )
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["topP"] = top_p
        if top_k is not UNSET:
            field_dict["topK"] = top_k
        if min_p is not UNSET:
            field_dict["minP"] = min_p
        if repetition_penalty is not UNSET:
            field_dict["repetitionPenalty"] = repetition_penalty
        if max_output_tokens is not UNSET:
            field_dict["maxOutputTokens"] = max_output_tokens
        if deployment_tier is not UNSET:
            field_dict["deploymentTier"] = deployment_tier
        if finetuning_id is not UNSET:
            field_dict["finetuningId"] = finetuning_id
        if adapter_name is not UNSET:
            field_dict["adapterName"] = adapter_name
        if adapter_scale is not UNSET:
            field_dict["adapterScale"] = adapter_scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        force_deployment = d.pop("forceDeployment")

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_top_p(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        top_p = _parse_top_p(d.pop("topP", UNSET))

        def _parse_top_k(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        top_k = _parse_top_k(d.pop("topK", UNSET))

        def _parse_min_p(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        min_p = _parse_min_p(d.pop("minP", UNSET))

        def _parse_repetition_penalty(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        repetition_penalty = _parse_repetition_penalty(d.pop("repetitionPenalty", UNSET))

        def _parse_max_output_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_output_tokens = _parse_max_output_tokens(d.pop("maxOutputTokens", UNSET))

        def _parse_deployment_tier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deployment_tier = _parse_deployment_tier(d.pop("deploymentTier", UNSET))

        def _parse_finetuning_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finetuning_id_type_0 = UUID(data)

                return finetuning_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        finetuning_id = _parse_finetuning_id(d.pop("finetuningId", UNSET))

        def _parse_adapter_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        adapter_name = _parse_adapter_name(d.pop("adapterName", UNSET))

        def _parse_adapter_scale(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        adapter_scale = _parse_adapter_scale(d.pop("adapterScale", UNSET))

        deployment_parameters = cls(
            force_deployment=force_deployment,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            min_p=min_p,
            repetition_penalty=repetition_penalty,
            max_output_tokens=max_output_tokens,
            deployment_tier=deployment_tier,
            finetuning_id=finetuning_id,
            adapter_name=adapter_name,
            adapter_scale=adapter_scale,
        )

        return deployment_parameters
