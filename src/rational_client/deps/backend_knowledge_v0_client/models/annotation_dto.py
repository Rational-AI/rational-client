from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.annotation_type import AnnotationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selector import Selector


T = TypeVar("T", bound="AnnotationDto")


@_attrs_define
class AnnotationDto:
    """
    Attributes:
        id (UUID):
        annotation_type (AnnotationType):
        position (int):
        rational_resource_id (UUID):
        enabled (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        selector (Selector | Unset):
        title (None | str | Unset):
        content (None | str | Unset):
        note (None | str | Unset):
        label (None | str | Unset):
        data (Any | Unset):
        embedding (list[float] | None | Unset):
        keywords (list[str] | None | Unset):
        generated_resource_id (None | Unset | UUID):
    """

    id: UUID
    annotation_type: AnnotationType
    position: int
    rational_resource_id: UUID
    enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    selector: Selector | Unset = UNSET
    title: None | str | Unset = UNSET
    content: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    data: Any | Unset = UNSET
    embedding: list[float] | None | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    generated_resource_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        annotation_type = self.annotation_type.value

        position = self.position

        rational_resource_id = str(self.rational_resource_id)

        enabled = self.enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        content: None | str | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        data = self.data

        embedding: list[float] | None | Unset
        if isinstance(self.embedding, Unset):
            embedding = UNSET
        elif isinstance(self.embedding, list):
            embedding = self.embedding

        else:
            embedding = self.embedding

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        generated_resource_id: None | str | Unset
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
                "position": position,
                "rationalResourceId": rational_resource_id,
                "enabled": enabled,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if selector is not UNSET:
            field_dict["selector"] = selector
        if title is not UNSET:
            field_dict["title"] = title
        if content is not UNSET:
            field_dict["content"] = content
        if note is not UNSET:
            field_dict["note"] = note
        if label is not UNSET:
            field_dict["label"] = label
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
        from ..models.selector import Selector

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        annotation_type = AnnotationType(d.pop("annotationType"))

        position = d.pop("position")

        rational_resource_id = UUID(d.pop("rationalResourceId"))

        enabled = d.pop("enabled")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _selector = d.pop("selector", UNSET)
        selector: Selector | Unset
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = Selector.from_dict(_selector)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        data = d.pop("data", UNSET)

        def _parse_embedding(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                embedding_type_0 = cast(list[float], data)

                return embedding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        embedding = _parse_embedding(d.pop("embedding", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_generated_resource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                generated_resource_id_type_0 = UUID(data)

                return generated_resource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        generated_resource_id = _parse_generated_resource_id(d.pop("generatedResourceId", UNSET))

        annotation_dto = cls(
            id=id,
            annotation_type=annotation_type,
            position=position,
            rational_resource_id=rational_resource_id,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
            selector=selector,
            title=title,
            content=content,
            note=note,
            label=label,
            data=data,
            embedding=embedding,
            keywords=keywords,
            generated_resource_id=generated_resource_id,
        )

        return annotation_dto
