import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.annotation_type import AnnotationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnnotationDto")


@_attrs_define
class AnnotationDto:
    """
    Attributes:
        id (UUID):
        annotation_type (AnnotationType):
        rational_resource_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        data (Union[Unset, Any]):
        embedding (Union[None, Unset, list[float]]):
        keywords (Union[None, Unset, list[str]]):
        generated_resource_id (Union[None, UUID, Unset]):
    """

    id: UUID
    annotation_type: AnnotationType
    rational_resource_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    data: Union[Unset, Any] = UNSET
    embedding: Union[None, Unset, list[float]] = UNSET
    keywords: Union[None, Unset, list[str]] = UNSET
    generated_resource_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        annotation_type = self.annotation_type.value

        rational_resource_id = str(self.rational_resource_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        data = self.data

        embedding: Union[None, Unset, list[float]]
        if isinstance(self.embedding, Unset):
            embedding = UNSET
        elif isinstance(self.embedding, list):
            embedding = self.embedding

        else:
            embedding = self.embedding

        keywords: Union[None, Unset, list[str]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        generated_resource_id: Union[None, Unset, str]
        if isinstance(self.generated_resource_id, Unset):
            generated_resource_id = UNSET
        elif isinstance(self.generated_resource_id, UUID):
            generated_resource_id = str(self.generated_resource_id)
        else:
            generated_resource_id = self.generated_resource_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "annotationType": annotation_type,
                "rationalResourceId": rational_resource_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if embedding is not UNSET:
            field_dict["embedding"] = embedding
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if generated_resource_id is not UNSET:
            field_dict["generatedResourceId"] = generated_resource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        annotation_type = AnnotationType(d.pop("annotationType"))

        rational_resource_id = UUID(d.pop("rationalResourceId"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        data = d.pop("data", UNSET)

        def _parse_embedding(data: object) -> Union[None, Unset, list[float]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                embedding_type_0 = cast(list[float], data)

                return embedding_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[float]], data)

        embedding = _parse_embedding(d.pop("embedding", UNSET))

        def _parse_keywords(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_generated_resource_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_resource_id_type_0 = UUID(data)

                return generated_resource_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        generated_resource_id = _parse_generated_resource_id(d.pop("generatedResourceId", UNSET))

        annotation_dto = cls(
            id=id,
            annotation_type=annotation_type,
            rational_resource_id=rational_resource_id,
            created_at=created_at,
            updated_at=updated_at,
            data=data,
            embedding=embedding,
            keywords=keywords,
            generated_resource_id=generated_resource_id,
        )

        return annotation_dto
