from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.annotation_dto import AnnotationDto
    from ..models.rational_resource_dto import RationalResourceDto


T = TypeVar("T", bound="SearchResultDto")


@_attrs_define
class SearchResultDto:
    """
    Attributes:
        annotation (AnnotationDto):
        rational_resource (RationalResourceDto):
        score (float):
    """

    annotation: AnnotationDto
    rational_resource: RationalResourceDto
    score: float

    def to_dict(self) -> dict[str, Any]:
        annotation = self.annotation.to_dict()

        rational_resource = self.rational_resource.to_dict()

        score = self.score

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "annotation": annotation,
                "rationalResource": rational_resource,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_dto import AnnotationDto
        from ..models.rational_resource_dto import RationalResourceDto

        d = dict(src_dict)
        annotation = AnnotationDto.from_dict(d.pop("annotation"))

        rational_resource = RationalResourceDto.from_dict(d.pop("rationalResource"))

        score = d.pop("score")

        search_result_dto = cls(
            annotation=annotation,
            rational_resource=rational_resource,
            score=score,
        )

        return search_result_dto
