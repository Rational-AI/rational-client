from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.knowledge_stats_config_dto import KnowledgeStatsConfigDto
    from ..models.knowledge_stats_dto_categories import KnowledgeStatsDtoCategories
    from ..models.knowledge_stats_dto_labels import KnowledgeStatsDtoLabels
    from ..models.knowledge_stats_dto_relations import KnowledgeStatsDtoRelations
    from ..models.knowledge_stats_dto_tags import KnowledgeStatsDtoTags


T = TypeVar("T", bound="KnowledgeStatsDto")


@_attrs_define
class KnowledgeStatsDto:
    """
    Attributes:
        config (KnowledgeStatsConfigDto):
        categories (KnowledgeStatsDtoCategories):
        tags (KnowledgeStatsDtoTags):
        relations (KnowledgeStatsDtoRelations):
        labels (KnowledgeStatsDtoLabels):
    """

    config: KnowledgeStatsConfigDto
    categories: KnowledgeStatsDtoCategories
    tags: KnowledgeStatsDtoTags
    relations: KnowledgeStatsDtoRelations
    labels: KnowledgeStatsDtoLabels

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        categories = self.categories.to_dict()

        tags = self.tags.to_dict()

        relations = self.relations.to_dict()

        labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "categories": categories,
                "tags": tags,
                "relations": relations,
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_stats_config_dto import KnowledgeStatsConfigDto
        from ..models.knowledge_stats_dto_categories import KnowledgeStatsDtoCategories
        from ..models.knowledge_stats_dto_labels import KnowledgeStatsDtoLabels
        from ..models.knowledge_stats_dto_relations import KnowledgeStatsDtoRelations
        from ..models.knowledge_stats_dto_tags import KnowledgeStatsDtoTags

        d = dict(src_dict)
        config = KnowledgeStatsConfigDto.from_dict(d.pop("config"))

        categories = KnowledgeStatsDtoCategories.from_dict(d.pop("categories"))

        tags = KnowledgeStatsDtoTags.from_dict(d.pop("tags"))

        relations = KnowledgeStatsDtoRelations.from_dict(d.pop("relations"))

        labels = KnowledgeStatsDtoLabels.from_dict(d.pop("labels"))

        knowledge_stats_dto = cls(
            config=config,
            categories=categories,
            tags=tags,
            relations=relations,
            labels=labels,
        )

        return knowledge_stats_dto
