from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentParameters")


@_attrs_define
class DeploymentParameters:
    """
    Attributes:
        force_deployment (bool):
        temperature (float | None | Unset):
        top_p (float | None | Unset):
        top_k (float | None | Unset):
        min_p (float | None | Unset):
        repetition_penalty (float | None | Unset):
        max_output_tokens (int | None | Unset):
        deployment_tier (None | str | Unset):
        finetuning_id (None | Unset | UUID):
        adapter_name (None | str | Unset):
        adapter_scale (float | None | Unset):
    """

    force_deployment: bool
    temperature: float | None | Unset = UNSET
    top_p: float | None | Unset = UNSET
    top_k: float | None | Unset = UNSET
    min_p: float | None | Unset = UNSET
    repetition_penalty: float | None | Unset = UNSET
    max_output_tokens: int | None | Unset = UNSET
    deployment_tier: None | str | Unset = UNSET
    finetuning_id: None | Unset | UUID = UNSET
    adapter_name: None | str | Unset = UNSET
    adapter_scale: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        force_deployment = self.force_deployment

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: float | None | Unset
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        top_k: float | None | Unset
        if isinstance(self.top_k, Unset):
            top_k = UNSET
        else:
            top_k = self.top_k

        min_p: float | None | Unset
        if isinstance(self.min_p, Unset):
            min_p = UNSET
        else:
            min_p = self.min_p

        repetition_penalty: float | None | Unset
        if isinstance(self.repetition_penalty, Unset):
            repetition_penalty = UNSET
        else:
            repetition_penalty = self.repetition_penalty

        max_output_tokens: int | None | Unset
        if isinstance(self.max_output_tokens, Unset):
            max_output_tokens = UNSET
        else:
            max_output_tokens = self.max_output_tokens

        deployment_tier: None | str | Unset
        if isinstance(self.deployment_tier, Unset):
            deployment_tier = UNSET
        else:
            deployment_tier = self.deployment_tier

        finetuning_id: None | str | Unset
        if isinstance(self.finetuning_id, Unset):
            finetuning_id = UNSET
        elif isinstance(self.finetuning_id, UUID):
            finetuning_id = str(self.finetuning_id)
        else:
            finetuning_id = self.finetuning_id

        adapter_name: None | str | Unset
        if isinstance(self.adapter_name, Unset):
            adapter_name = UNSET
        else:
            adapter_name = self.adapter_name

        adapter_scale: float | None | Unset
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

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_top_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_p = _parse_top_p(d.pop("topP", UNSET))

        def _parse_top_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_k = _parse_top_k(d.pop("topK", UNSET))

        def _parse_min_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_p = _parse_min_p(d.pop("minP", UNSET))

        def _parse_repetition_penalty(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        repetition_penalty = _parse_repetition_penalty(d.pop("repetitionPenalty", UNSET))

        def _parse_max_output_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_output_tokens = _parse_max_output_tokens(d.pop("maxOutputTokens", UNSET))

        def _parse_deployment_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deployment_tier = _parse_deployment_tier(d.pop("deploymentTier", UNSET))

        def _parse_finetuning_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finetuning_id_type_0 = UUID(data)

                return finetuning_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        finetuning_id = _parse_finetuning_id(d.pop("finetuningId", UNSET))

        def _parse_adapter_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adapter_name = _parse_adapter_name(d.pop("adapterName", UNSET))

        def _parse_adapter_scale(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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
