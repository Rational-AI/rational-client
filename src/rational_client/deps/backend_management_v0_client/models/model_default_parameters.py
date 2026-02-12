from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDefaultParameters")


@_attrs_define
class ModelDefaultParameters:
    """
    Attributes:
        ro_pe_frequency_base (float):
        ro_pe_frequency_scale (float):
        context_length (int | None | Unset):
        gpu_offload (int | None | Unset):
        cpu_thread_pool_size (int | None | Unset):
        evaluation_batch_size (int | None | Unset):
        seed (int | None | Unset):
        temperature (float | None | Unset):
        response_length (float | None | Unset):
        limit_response_length (bool | None | Unset):
        top_p (float | None | Unset):
        top_k (float | None | Unset):
        min_p (float | None | Unset):
        repetition_penalty (float | None | Unset):
    """

    ro_pe_frequency_base: float
    ro_pe_frequency_scale: float
    context_length: int | None | Unset = UNSET
    gpu_offload: int | None | Unset = UNSET
    cpu_thread_pool_size: int | None | Unset = UNSET
    evaluation_batch_size: int | None | Unset = UNSET
    seed: int | None | Unset = UNSET
    temperature: float | None | Unset = UNSET
    response_length: float | None | Unset = UNSET
    limit_response_length: bool | None | Unset = UNSET
    top_p: float | None | Unset = UNSET
    top_k: float | None | Unset = UNSET
    min_p: float | None | Unset = UNSET
    repetition_penalty: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ro_pe_frequency_base = self.ro_pe_frequency_base

        ro_pe_frequency_scale = self.ro_pe_frequency_scale

        context_length: int | None | Unset
        if isinstance(self.context_length, Unset):
            context_length = UNSET
        else:
            context_length = self.context_length

        gpu_offload: int | None | Unset
        if isinstance(self.gpu_offload, Unset):
            gpu_offload = UNSET
        else:
            gpu_offload = self.gpu_offload

        cpu_thread_pool_size: int | None | Unset
        if isinstance(self.cpu_thread_pool_size, Unset):
            cpu_thread_pool_size = UNSET
        else:
            cpu_thread_pool_size = self.cpu_thread_pool_size

        evaluation_batch_size: int | None | Unset
        if isinstance(self.evaluation_batch_size, Unset):
            evaluation_batch_size = UNSET
        else:
            evaluation_batch_size = self.evaluation_batch_size

        seed: int | None | Unset
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        response_length: float | None | Unset
        if isinstance(self.response_length, Unset):
            response_length = UNSET
        else:
            response_length = self.response_length

        limit_response_length: bool | None | Unset
        if isinstance(self.limit_response_length, Unset):
            limit_response_length = UNSET
        else:
            limit_response_length = self.limit_response_length

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "roPEFrequencyBase": ro_pe_frequency_base,
                "roPEFrequencyScale": ro_pe_frequency_scale,
            }
        )
        if context_length is not UNSET:
            field_dict["contextLength"] = context_length
        if gpu_offload is not UNSET:
            field_dict["gpuOffload"] = gpu_offload
        if cpu_thread_pool_size is not UNSET:
            field_dict["cpuThreadPoolSize"] = cpu_thread_pool_size
        if evaluation_batch_size is not UNSET:
            field_dict["evaluationBatchSize"] = evaluation_batch_size
        if seed is not UNSET:
            field_dict["seed"] = seed
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if response_length is not UNSET:
            field_dict["responseLength"] = response_length
        if limit_response_length is not UNSET:
            field_dict["limitResponseLength"] = limit_response_length
        if top_p is not UNSET:
            field_dict["topP"] = top_p
        if top_k is not UNSET:
            field_dict["topK"] = top_k
        if min_p is not UNSET:
            field_dict["minP"] = min_p
        if repetition_penalty is not UNSET:
            field_dict["repetitionPenalty"] = repetition_penalty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ro_pe_frequency_base = d.pop("roPEFrequencyBase")

        ro_pe_frequency_scale = d.pop("roPEFrequencyScale")

        def _parse_context_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        context_length = _parse_context_length(d.pop("contextLength", UNSET))

        def _parse_gpu_offload(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gpu_offload = _parse_gpu_offload(d.pop("gpuOffload", UNSET))

        def _parse_cpu_thread_pool_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_thread_pool_size = _parse_cpu_thread_pool_size(d.pop("cpuThreadPoolSize", UNSET))

        def _parse_evaluation_batch_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        evaluation_batch_size = _parse_evaluation_batch_size(d.pop("evaluationBatchSize", UNSET))

        def _parse_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_response_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        response_length = _parse_response_length(d.pop("responseLength", UNSET))

        def _parse_limit_response_length(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        limit_response_length = _parse_limit_response_length(d.pop("limitResponseLength", UNSET))

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

        model_default_parameters = cls(
            ro_pe_frequency_base=ro_pe_frequency_base,
            ro_pe_frequency_scale=ro_pe_frequency_scale,
            context_length=context_length,
            gpu_offload=gpu_offload,
            cpu_thread_pool_size=cpu_thread_pool_size,
            evaluation_batch_size=evaluation_batch_size,
            seed=seed,
            temperature=temperature,
            response_length=response_length,
            limit_response_length=limit_response_length,
            top_p=top_p,
            top_k=top_k,
            min_p=min_p,
            repetition_penalty=repetition_penalty,
        )

        return model_default_parameters
