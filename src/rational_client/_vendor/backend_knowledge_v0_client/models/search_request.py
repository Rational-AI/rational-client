from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        query_vector (list[float]):
        top_k (int):
        resource_ids (Union[None, Unset, list[UUID]]):
        annotation_ids (Union[None, Unset, list[UUID]]):
        keywords (Union[None, Unset, list[str]]):
    """

    query_vector: list[float]
    top_k: int
    resource_ids: Union[None, Unset, list[UUID]] = UNSET
    annotation_ids: Union[None, Unset, list[UUID]] = UNSET
    keywords: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_vector = self.query_vector

        top_k = self.top_k

        resource_ids: Union[None, Unset, list[str]]
        if isinstance(self.resource_ids, Unset):
            resource_ids = UNSET
        elif isinstance(self.resource_ids, list):
            resource_ids = []
            for resource_ids_type_0_item_data in self.resource_ids:
                resource_ids_type_0_item = str(resource_ids_type_0_item_data)
                resource_ids.append(resource_ids_type_0_item)

        else:
            resource_ids = self.resource_ids

        annotation_ids: Union[None, Unset, list[str]]
        if isinstance(self.annotation_ids, Unset):
            annotation_ids = UNSET
        elif isinstance(self.annotation_ids, list):
            annotation_ids = []
            for annotation_ids_type_0_item_data in self.annotation_ids:
                annotation_ids_type_0_item = str(annotation_ids_type_0_item_data)
                annotation_ids.append(annotation_ids_type_0_item)

        else:
            annotation_ids = self.annotation_ids

        keywords: Union[None, Unset, list[str]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "queryVector": query_vector,
                "topK": top_k,
            }
        )
        if resource_ids is not UNSET:
            field_dict["resourceIds"] = resource_ids
        if annotation_ids is not UNSET:
            field_dict["annotationIds"] = annotation_ids
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_vector = cast(list[float], d.pop("queryVector"))

        top_k = d.pop("topK")

        def _parse_resource_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resource_ids_type_0 = []
                _resource_ids_type_0 = data
                for resource_ids_type_0_item_data in _resource_ids_type_0:
                    resource_ids_type_0_item = UUID(resource_ids_type_0_item_data)

                    resource_ids_type_0.append(resource_ids_type_0_item)

                return resource_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        resource_ids = _parse_resource_ids(d.pop("resourceIds", UNSET))

        def _parse_annotation_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                annotation_ids_type_0 = []
                _annotation_ids_type_0 = data
                for annotation_ids_type_0_item_data in _annotation_ids_type_0:
                    annotation_ids_type_0_item = UUID(annotation_ids_type_0_item_data)

                    annotation_ids_type_0.append(annotation_ids_type_0_item)

                return annotation_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        annotation_ids = _parse_annotation_ids(d.pop("annotationIds", UNSET))

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

        search_request = cls(
            query_vector=query_vector,
            top_k=top_k,
            resource_ids=resource_ids,
            annotation_ids=annotation_ids,
            keywords=keywords,
        )

        return search_request
