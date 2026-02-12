from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matched_document import MatchedDocument


T = TypeVar("T", bound="ClaimVerification")


@_attrs_define
class ClaimVerification:
    """
    Attributes:
        claim (str):
        matches (list[MatchedDocument]):
        highest_similarity (float | Unset):
    """

    claim: str
    matches: list[MatchedDocument]
    highest_similarity: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        claim = self.claim

        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)

        highest_similarity = self.highest_similarity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "claim": claim,
                "matches": matches,
            }
        )
        if highest_similarity is not UNSET:
            field_dict["highest_similarity"] = highest_similarity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matched_document import MatchedDocument

        d = dict(src_dict)
        claim = d.pop("claim")

        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:
            matches_item = MatchedDocument.from_dict(matches_item_data)

            matches.append(matches_item)

        highest_similarity = d.pop("highest_similarity", UNSET)

        claim_verification = cls(
            claim=claim,
            matches=matches,
            highest_similarity=highest_similarity,
        )

        return claim_verification
