from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.knowledge_stats_dto_categories import KnowledgeStatsDtoCategories
    from ..models.knowledge_stats_dto_relations import KnowledgeStatsDtoRelations
    from ..models.knowledge_stats_dto_tags import KnowledgeStatsDtoTags


T = TypeVar("T", bound="KnowledgeStatsDto")


@_attrs_define
class KnowledgeStatsDto:
    """
    Attributes:
        categories (KnowledgeStatsDtoCategories):
        tags (KnowledgeStatsDtoTags):
        relations (KnowledgeStatsDtoRelations):
    """

    categories: "KnowledgeStatsDtoCategories"
    tags: "KnowledgeStatsDtoTags"
    relations: "KnowledgeStatsDtoRelations"

    def to_dict(self) -> dict[str, Any]:
        categories = self.categories.to_dict()

        tags = self.tags.to_dict()

        relations = self.relations.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "categories": categories,
                "tags": tags,
                "relations": relations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_stats_dto_categories import KnowledgeStatsDtoCategories
        from ..models.knowledge_stats_dto_relations import KnowledgeStatsDtoRelations
        from ..models.knowledge_stats_dto_tags import KnowledgeStatsDtoTags

        d = dict(src_dict)
        categories = KnowledgeStatsDtoCategories.from_dict(d.pop("categories"))

        tags = KnowledgeStatsDtoTags.from_dict(d.pop("tags"))

        relations = KnowledgeStatsDtoRelations.from_dict(d.pop("relations"))

        knowledge_stats_dto = cls(
            categories=categories,
            tags=tags,
            relations=relations,
        )

        return knowledge_stats_dto
