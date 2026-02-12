from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.selector import Selector


T = TypeVar("T", bound="UpdateAnnotationRequest")


@_attrs_define
class UpdateAnnotationRequest:
    """
    Attributes:
        content (str | Unset):
        note (None | str | Unset):
        selector (Selector | Unset):
        position (int | None | Unset):
        title (None | str | Unset):
        label (None | str | Unset):
        data (Any | Unset):
        embedding (list[float] | None | Unset):
        keywords (list[str] | None | Unset):
        generated_resource_id (None | Unset | UUID):
        enabled (bool | Unset):
    """

    content: str | Unset = UNSET
    note: None | str | Unset = UNSET
    selector: Selector | Unset = UNSET
    position: int | None | Unset = UNSET
    title: None | str | Unset = UNSET
    label: None | str | Unset = UNSET
    data: Any | Unset = UNSET
    embedding: list[float] | None | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    generated_resource_id: None | Unset | UUID = UNSET
    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

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

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if note is not UNSET:
            field_dict["note"] = note
        if selector is not UNSET:
            field_dict["selector"] = selector
        if position is not UNSET:
            field_dict["position"] = position
        if title is not UNSET:
            field_dict["title"] = title
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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selector import Selector

        d = dict(src_dict)
        content = d.pop("content", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        _selector = d.pop("selector", UNSET)
        selector: Selector | Unset
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = Selector.from_dict(_selector)

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        enabled = d.pop("enabled", UNSET)

        update_annotation_request = cls(
            content=content,
            note=note,
            selector=selector,
            position=position,
            title=title,
            label=label,
            data=data,
            embedding=embedding,
            keywords=keywords,
            generated_resource_id=generated_resource_id,
            enabled=enabled,
        )

        return update_annotation_request
