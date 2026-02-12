from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerificationSummary")


@_attrs_define
class VerificationSummary:
    """
    Attributes:
        total_sentences (int | Unset):
        total_claims (int | Unset):
        total_rag_documents (int | Unset):
        error (None | str | Unset):
    """

    total_sentences: int | Unset = UNSET
    total_claims: int | Unset = UNSET
    total_rag_documents: int | Unset = UNSET
    error: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_sentences = self.total_sentences

        total_claims = self.total_claims

        total_rag_documents = self.total_rag_documents

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_sentences is not UNSET:
            field_dict["total_sentences"] = total_sentences
        if total_claims is not UNSET:
            field_dict["total_claims"] = total_claims
        if total_rag_documents is not UNSET:
            field_dict["total_rag_documents"] = total_rag_documents
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_sentences = d.pop("total_sentences", UNSET)

        total_claims = d.pop("total_claims", UNSET)

        total_rag_documents = d.pop("total_rag_documents", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        verification_summary = cls(
            total_sentences=total_sentences,
            total_claims=total_claims,
            total_rag_documents=total_rag_documents,
            error=error,
        )

        return verification_summary
