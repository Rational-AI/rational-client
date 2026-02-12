from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_verification import ClaimVerification


T = TypeVar("T", bound="SentenceVerification")


@_attrs_define
class SentenceVerification:
    """
    Attributes:
        classification (str):
        claims (list[ClaimVerification]):
        sentence_text (str | Unset):
    """

    classification: str
    claims: list[ClaimVerification]
    sentence_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        classification = self.classification

        claims = []
        for claims_item_data in self.claims:
            claims_item = claims_item_data.to_dict()
            claims.append(claims_item)

        sentence_text = self.sentence_text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "classification": classification,
                "claims": claims,
            }
        )
        if sentence_text is not UNSET:
            field_dict["sentence_text"] = sentence_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_verification import ClaimVerification

        d = dict(src_dict)
        classification = d.pop("classification")

        claims = []
        _claims = d.pop("claims")
        for claims_item_data in _claims:
            claims_item = ClaimVerification.from_dict(claims_item_data)

            claims.append(claims_item)

        sentence_text = d.pop("sentence_text", UNSET)

        sentence_verification = cls(
            classification=classification,
            claims=claims,
            sentence_text=sentence_text,
        )

        return sentence_verification
