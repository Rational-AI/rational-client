from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchedDocument")


@_attrs_define
class MatchedDocument:
    """
    Attributes:
        text (str):
        phase (str):
        resource_id (str | Unset):
        annotation_id (str | Unset):
        similarity_score (float | Unset):
    """

    text: str
    phase: str
    resource_id: str | Unset = UNSET
    annotation_id: str | Unset = UNSET
    similarity_score: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        phase = self.phase

        resource_id = self.resource_id

        annotation_id = self.annotation_id

        similarity_score = self.similarity_score

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
                "phase": phase,
            }
        )
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if annotation_id is not UNSET:
            field_dict["annotation_id"] = annotation_id
        if similarity_score is not UNSET:
            field_dict["similarity_score"] = similarity_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        phase = d.pop("phase")

        resource_id = d.pop("resource_id", UNSET)

        annotation_id = d.pop("annotation_id", UNSET)

        similarity_score = d.pop("similarity_score", UNSET)

        matched_document = cls(
            text=text,
            phase=phase,
            resource_id=resource_id,
            annotation_id=annotation_id,
            similarity_score=similarity_score,
        )

        return matched_document
