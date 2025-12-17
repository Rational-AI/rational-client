from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDefaultParameters")


@_attrs_define
class ModelDefaultParameters:
    """
    Attributes:
        ro_pe_frequency_base (float):
        ro_pe_frequency_scale (float):
        context_length (Union[None, Unset, int]):
        gpu_offload (Union[None, Unset, int]):
        cpu_thread_pool_size (Union[None, Unset, int]):
        evaluation_batch_size (Union[None, Unset, int]):
        seed (Union[None, Unset, int]):
        temperature (Union[None, Unset, float]):
        response_length (Union[None, Unset, float]):
        limit_response_length (Union[None, Unset, bool]):
        top_p (Union[None, Unset, float]):
        top_k (Union[None, Unset, float]):
        min_p (Union[None, Unset, float]):
        repetition_penalty (Union[None, Unset, float]):
    """

    ro_pe_frequency_base: float
    ro_pe_frequency_scale: float
    context_length: Union[None, Unset, int] = UNSET
    gpu_offload: Union[None, Unset, int] = UNSET
    cpu_thread_pool_size: Union[None, Unset, int] = UNSET
    evaluation_batch_size: Union[None, Unset, int] = UNSET
    seed: Union[None, Unset, int] = UNSET
    temperature: Union[None, Unset, float] = UNSET
    response_length: Union[None, Unset, float] = UNSET
    limit_response_length: Union[None, Unset, bool] = UNSET
    top_p: Union[None, Unset, float] = UNSET
    top_k: Union[None, Unset, float] = UNSET
    min_p: Union[None, Unset, float] = UNSET
    repetition_penalty: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ro_pe_frequency_base = self.ro_pe_frequency_base

        ro_pe_frequency_scale = self.ro_pe_frequency_scale

        context_length: Union[None, Unset, int]
        if isinstance(self.context_length, Unset):
            context_length = UNSET
        else:
            context_length = self.context_length

        gpu_offload: Union[None, Unset, int]
        if isinstance(self.gpu_offload, Unset):
            gpu_offload = UNSET
        else:
            gpu_offload = self.gpu_offload

        cpu_thread_pool_size: Union[None, Unset, int]
        if isinstance(self.cpu_thread_pool_size, Unset):
            cpu_thread_pool_size = UNSET
        else:
            cpu_thread_pool_size = self.cpu_thread_pool_size

        evaluation_batch_size: Union[None, Unset, int]
        if isinstance(self.evaluation_batch_size, Unset):
            evaluation_batch_size = UNSET
        else:
            evaluation_batch_size = self.evaluation_batch_size

        seed: Union[None, Unset, int]
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        response_length: Union[None, Unset, float]
        if isinstance(self.response_length, Unset):
            response_length = UNSET
        else:
            response_length = self.response_length

        limit_response_length: Union[None, Unset, bool]
        if isinstance(self.limit_response_length, Unset):
            limit_response_length = UNSET
        else:
            limit_response_length = self.limit_response_length

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

        def _parse_context_length(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        context_length = _parse_context_length(d.pop("contextLength", UNSET))

        def _parse_gpu_offload(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        gpu_offload = _parse_gpu_offload(d.pop("gpuOffload", UNSET))

        def _parse_cpu_thread_pool_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_thread_pool_size = _parse_cpu_thread_pool_size(d.pop("cpuThreadPoolSize", UNSET))

        def _parse_evaluation_batch_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        evaluation_batch_size = _parse_evaluation_batch_size(d.pop("evaluationBatchSize", UNSET))

        def _parse_seed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_response_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        response_length = _parse_response_length(d.pop("responseLength", UNSET))

        def _parse_limit_response_length(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        limit_response_length = _parse_limit_response_length(d.pop("limitResponseLength", UNSET))

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
