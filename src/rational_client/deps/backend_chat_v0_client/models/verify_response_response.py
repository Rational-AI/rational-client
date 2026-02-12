from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sentence_verification import SentenceVerification
    from ..models.verification_summary import VerificationSummary


T = TypeVar("T", bound="VerifyResponseResponse")


@_attrs_define
class VerifyResponseResponse:
    """
    Attributes:
        verifications (list[SentenceVerification]):
        summary (VerificationSummary):
        room_id (str | Unset):
        extraction_mode (str | Unset):
    """

    verifications: list[SentenceVerification]
    summary: VerificationSummary
    room_id: str | Unset = UNSET
    extraction_mode: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        verifications = []
        for verifications_item_data in self.verifications:
            verifications_item = verifications_item_data.to_dict()
            verifications.append(verifications_item)

        summary = self.summary.to_dict()

        room_id = self.room_id

        extraction_mode = self.extraction_mode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "verifications": verifications,
                "summary": summary,
            }
        )
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if extraction_mode is not UNSET:
            field_dict["extraction_mode"] = extraction_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentence_verification import SentenceVerification
        from ..models.verification_summary import VerificationSummary

        d = dict(src_dict)
        verifications = []
        _verifications = d.pop("verifications")
        for verifications_item_data in _verifications:
            verifications_item = SentenceVerification.from_dict(verifications_item_data)

            verifications.append(verifications_item)

        summary = VerificationSummary.from_dict(d.pop("summary"))

        room_id = d.pop("room_id", UNSET)

        extraction_mode = d.pop("extraction_mode", UNSET)

        verify_response_response = cls(
            verifications=verifications,
            summary=summary,
            room_id=room_id,
            extraction_mode=extraction_mode,
        )

        return verify_response_response
