from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseVerificationConfiguration")


@_attrs_define
class ResponseVerificationConfiguration:
    """
    Attributes:
        enabled (bool):
        extract_claims_first (bool | None | Unset):
        verification_method (None | str | Unset):
        llm_edge_threshold (float | None | Unset):
        max_rag_events (int | None | Unset):
        top_n_matches (int | None | Unset):
        supported_threshold (float | None | Unset):
        uncertain_threshold (float | None | Unset):
        model_name (None | str | Unset):
    """

    enabled: bool
    extract_claims_first: bool | None | Unset = UNSET
    verification_method: None | str | Unset = UNSET
    llm_edge_threshold: float | None | Unset = UNSET
    max_rag_events: int | None | Unset = UNSET
    top_n_matches: int | None | Unset = UNSET
    supported_threshold: float | None | Unset = UNSET
    uncertain_threshold: float | None | Unset = UNSET
    model_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        extract_claims_first: bool | None | Unset
        if isinstance(self.extract_claims_first, Unset):
            extract_claims_first = UNSET
        else:
            extract_claims_first = self.extract_claims_first

        verification_method: None | str | Unset
        if isinstance(self.verification_method, Unset):
            verification_method = UNSET
        else:
            verification_method = self.verification_method

        llm_edge_threshold: float | None | Unset
        if isinstance(self.llm_edge_threshold, Unset):
            llm_edge_threshold = UNSET
        else:
            llm_edge_threshold = self.llm_edge_threshold

        max_rag_events: int | None | Unset
        if isinstance(self.max_rag_events, Unset):
            max_rag_events = UNSET
        else:
            max_rag_events = self.max_rag_events

        top_n_matches: int | None | Unset
        if isinstance(self.top_n_matches, Unset):
            top_n_matches = UNSET
        else:
            top_n_matches = self.top_n_matches

        supported_threshold: float | None | Unset
        if isinstance(self.supported_threshold, Unset):
            supported_threshold = UNSET
        else:
            supported_threshold = self.supported_threshold

        uncertain_threshold: float | None | Unset
        if isinstance(self.uncertain_threshold, Unset):
            uncertain_threshold = UNSET
        else:
            uncertain_threshold = self.uncertain_threshold

        model_name: None | str | Unset
        if isinstance(self.model_name, Unset):
            model_name = UNSET
        else:
            model_name = self.model_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if extract_claims_first is not UNSET:
            field_dict["extractClaimsFirst"] = extract_claims_first
        if verification_method is not UNSET:
            field_dict["verificationMethod"] = verification_method
        if llm_edge_threshold is not UNSET:
            field_dict["llmEdgeThreshold"] = llm_edge_threshold
        if max_rag_events is not UNSET:
            field_dict["maxRagEvents"] = max_rag_events
        if top_n_matches is not UNSET:
            field_dict["topNMatches"] = top_n_matches
        if supported_threshold is not UNSET:
            field_dict["supportedThreshold"] = supported_threshold
        if uncertain_threshold is not UNSET:
            field_dict["uncertainThreshold"] = uncertain_threshold
        if model_name is not UNSET:
            field_dict["modelName"] = model_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_extract_claims_first(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        extract_claims_first = _parse_extract_claims_first(d.pop("extractClaimsFirst", UNSET))

        def _parse_verification_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verification_method = _parse_verification_method(d.pop("verificationMethod", UNSET))

        def _parse_llm_edge_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        llm_edge_threshold = _parse_llm_edge_threshold(d.pop("llmEdgeThreshold", UNSET))

        def _parse_max_rag_events(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_rag_events = _parse_max_rag_events(d.pop("maxRagEvents", UNSET))

        def _parse_top_n_matches(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        top_n_matches = _parse_top_n_matches(d.pop("topNMatches", UNSET))

        def _parse_supported_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        supported_threshold = _parse_supported_threshold(d.pop("supportedThreshold", UNSET))

        def _parse_uncertain_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        uncertain_threshold = _parse_uncertain_threshold(d.pop("uncertainThreshold", UNSET))

        def _parse_model_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_name = _parse_model_name(d.pop("modelName", UNSET))

        response_verification_configuration = cls(
            enabled=enabled,
            extract_claims_first=extract_claims_first,
            verification_method=verification_method,
            llm_edge_threshold=llm_edge_threshold,
            max_rag_events=max_rag_events,
            top_n_matches=top_n_matches,
            supported_threshold=supported_threshold,
            uncertain_threshold=uncertain_threshold,
            model_name=model_name,
        )

        return response_verification_configuration
