from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.chunker_type import ChunkerType
from ..models.keyword_extraction_method import KeywordExtractionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.color_config import ColorConfig
    from ..models.knowledge_source_dto import KnowledgeSourceDto
    from ..models.model_dto import ModelDto
    from ..models.processing_rule_dto import ProcessingRuleDto


T = TypeVar("T", bound="KnowledgeDto")


@_attrs_define
class KnowledgeDto:
    """
    Attributes:
        id (UUID):
        name (str):
        description (str):
        chunker (ChunkerType):
        allow_ai_search (bool):
        enabled (bool):
        knowledge_sources (list[KnowledgeSourceDto]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        synced_resources_count (int):
        rational_resources_count (int):
        chunker_options (Any | Unset):
        embedding_model (ModelDto | Unset):
        allow_keywords_extraction (bool | None | Unset):
        keyword_extraction_method (KeywordExtractionMethod | Unset):
        keyword_extraction_custom_prompt (None | str | Unset):
        keyword_extraction_max_keywords (int | None | Unset):
        processing_rule (ProcessingRuleDto | Unset):
        touchpoint_id (None | Unset | UUID):
        processing_rule_options (Any | Unset):
        category_config (ColorConfig | Unset):
        tag_config (ColorConfig | Unset):
        relation_config (ColorConfig | Unset):
        label_config (ColorConfig | Unset):
    """

    id: UUID
    name: str
    description: str
    chunker: ChunkerType
    allow_ai_search: bool
    enabled: bool
    knowledge_sources: list[KnowledgeSourceDto]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    synced_resources_count: int
    rational_resources_count: int
    chunker_options: Any | Unset = UNSET
    embedding_model: ModelDto | Unset = UNSET
    allow_keywords_extraction: bool | None | Unset = UNSET
    keyword_extraction_method: KeywordExtractionMethod | Unset = UNSET
    keyword_extraction_custom_prompt: None | str | Unset = UNSET
    keyword_extraction_max_keywords: int | None | Unset = UNSET
    processing_rule: ProcessingRuleDto | Unset = UNSET
    touchpoint_id: None | Unset | UUID = UNSET
    processing_rule_options: Any | Unset = UNSET
    category_config: ColorConfig | Unset = UNSET
    tag_config: ColorConfig | Unset = UNSET
    relation_config: ColorConfig | Unset = UNSET
    label_config: ColorConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description = self.description

        chunker = self.chunker.value

        allow_ai_search = self.allow_ai_search

        enabled = self.enabled

        knowledge_sources = []
        for knowledge_sources_item_data in self.knowledge_sources:
            knowledge_sources_item = knowledge_sources_item_data.to_dict()
            knowledge_sources.append(knowledge_sources_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        synced_resources_count = self.synced_resources_count

        rational_resources_count = self.rational_resources_count

        chunker_options = self.chunker_options

        embedding_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedding_model, Unset):
            embedding_model = self.embedding_model.to_dict()

        allow_keywords_extraction: bool | None | Unset
        if isinstance(self.allow_keywords_extraction, Unset):
            allow_keywords_extraction = UNSET
        else:
            allow_keywords_extraction = self.allow_keywords_extraction

        keyword_extraction_method: str | Unset = UNSET
        if not isinstance(self.keyword_extraction_method, Unset):
            keyword_extraction_method = self.keyword_extraction_method.value

        keyword_extraction_custom_prompt: None | str | Unset
        if isinstance(self.keyword_extraction_custom_prompt, Unset):
            keyword_extraction_custom_prompt = UNSET
        else:
            keyword_extraction_custom_prompt = self.keyword_extraction_custom_prompt

        keyword_extraction_max_keywords: int | None | Unset
        if isinstance(self.keyword_extraction_max_keywords, Unset):
            keyword_extraction_max_keywords = UNSET
        else:
            keyword_extraction_max_keywords = self.keyword_extraction_max_keywords

        processing_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.processing_rule, Unset):
            processing_rule = self.processing_rule.to_dict()

        touchpoint_id: None | str | Unset
        if isinstance(self.touchpoint_id, Unset):
            touchpoint_id = UNSET
        elif isinstance(self.touchpoint_id, UUID):
            touchpoint_id = str(self.touchpoint_id)
        else:
            touchpoint_id = self.touchpoint_id

        processing_rule_options = self.processing_rule_options

        category_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category_config, Unset):
            category_config = self.category_config.to_dict()

        tag_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_config, Unset):
            tag_config = self.tag_config.to_dict()

        relation_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation_config, Unset):
            relation_config = self.relation_config.to_dict()

        label_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_config, Unset):
            label_config = self.label_config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "chunker": chunker,
                "allowAiSearch": allow_ai_search,
                "enabled": enabled,
                "knowledgeSources": knowledge_sources,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "syncedResourcesCount": synced_resources_count,
                "rationalResourcesCount": rational_resources_count,
            }
        )
        if chunker_options is not UNSET:
            field_dict["chunkerOptions"] = chunker_options
        if embedding_model is not UNSET:
            field_dict["embeddingModel"] = embedding_model
        if allow_keywords_extraction is not UNSET:
            field_dict["allowKeywordsExtraction"] = allow_keywords_extraction
        if keyword_extraction_method is not UNSET:
            field_dict["keywordExtractionMethod"] = keyword_extraction_method
        if keyword_extraction_custom_prompt is not UNSET:
            field_dict["keywordExtractionCustomPrompt"] = keyword_extraction_custom_prompt
        if keyword_extraction_max_keywords is not UNSET:
            field_dict["keywordExtractionMaxKeywords"] = keyword_extraction_max_keywords
        if processing_rule is not UNSET:
            field_dict["processingRule"] = processing_rule
        if touchpoint_id is not UNSET:
            field_dict["touchpointId"] = touchpoint_id
        if processing_rule_options is not UNSET:
            field_dict["processingRuleOptions"] = processing_rule_options
        if category_config is not UNSET:
            field_dict["categoryConfig"] = category_config
        if tag_config is not UNSET:
            field_dict["tagConfig"] = tag_config
        if relation_config is not UNSET:
            field_dict["relationConfig"] = relation_config
        if label_config is not UNSET:
            field_dict["labelConfig"] = label_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_config import ColorConfig
        from ..models.knowledge_source_dto import KnowledgeSourceDto
        from ..models.model_dto import ModelDto
        from ..models.processing_rule_dto import ProcessingRuleDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        description = d.pop("description")

        chunker = ChunkerType(d.pop("chunker"))

        allow_ai_search = d.pop("allowAiSearch")

        enabled = d.pop("enabled")

        knowledge_sources = []
        _knowledge_sources = d.pop("knowledgeSources")
        for knowledge_sources_item_data in _knowledge_sources:
            knowledge_sources_item = KnowledgeSourceDto.from_dict(knowledge_sources_item_data)

            knowledge_sources.append(knowledge_sources_item)

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        synced_resources_count = d.pop("syncedResourcesCount")

        rational_resources_count = d.pop("rationalResourcesCount")

        chunker_options = d.pop("chunkerOptions", UNSET)

        _embedding_model = d.pop("embeddingModel", UNSET)
        embedding_model: ModelDto | Unset
        if isinstance(_embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = ModelDto.from_dict(_embedding_model)

        def _parse_allow_keywords_extraction(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_keywords_extraction = _parse_allow_keywords_extraction(d.pop("allowKeywordsExtraction", UNSET))

        _keyword_extraction_method = d.pop("keywordExtractionMethod", UNSET)
        keyword_extraction_method: KeywordExtractionMethod | Unset
        if isinstance(_keyword_extraction_method, Unset):
            keyword_extraction_method = UNSET
        else:
            keyword_extraction_method = KeywordExtractionMethod(_keyword_extraction_method)

        def _parse_keyword_extraction_custom_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keyword_extraction_custom_prompt = _parse_keyword_extraction_custom_prompt(
            d.pop("keywordExtractionCustomPrompt", UNSET)
        )

        def _parse_keyword_extraction_max_keywords(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        keyword_extraction_max_keywords = _parse_keyword_extraction_max_keywords(
            d.pop("keywordExtractionMaxKeywords", UNSET)
        )

        _processing_rule = d.pop("processingRule", UNSET)
        processing_rule: ProcessingRuleDto | Unset
        if isinstance(_processing_rule, Unset):
            processing_rule = UNSET
        else:
            processing_rule = ProcessingRuleDto.from_dict(_processing_rule)

        def _parse_touchpoint_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                touchpoint_id_type_0 = UUID(data)

                return touchpoint_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        touchpoint_id = _parse_touchpoint_id(d.pop("touchpointId", UNSET))

        processing_rule_options = d.pop("processingRuleOptions", UNSET)

        _category_config = d.pop("categoryConfig", UNSET)
        category_config: ColorConfig | Unset
        if isinstance(_category_config, Unset):
            category_config = UNSET
        else:
            category_config = ColorConfig.from_dict(_category_config)

        _tag_config = d.pop("tagConfig", UNSET)
        tag_config: ColorConfig | Unset
        if isinstance(_tag_config, Unset):
            tag_config = UNSET
        else:
            tag_config = ColorConfig.from_dict(_tag_config)

        _relation_config = d.pop("relationConfig", UNSET)
        relation_config: ColorConfig | Unset
        if isinstance(_relation_config, Unset):
            relation_config = UNSET
        else:
            relation_config = ColorConfig.from_dict(_relation_config)

        _label_config = d.pop("labelConfig", UNSET)
        label_config: ColorConfig | Unset
        if isinstance(_label_config, Unset):
            label_config = UNSET
        else:
            label_config = ColorConfig.from_dict(_label_config)

        knowledge_dto = cls(
            id=id,
            name=name,
            description=description,
            chunker=chunker,
            allow_ai_search=allow_ai_search,
            enabled=enabled,
            knowledge_sources=knowledge_sources,
            created_at=created_at,
            updated_at=updated_at,
            synced_resources_count=synced_resources_count,
            rational_resources_count=rational_resources_count,
            chunker_options=chunker_options,
            embedding_model=embedding_model,
            allow_keywords_extraction=allow_keywords_extraction,
            keyword_extraction_method=keyword_extraction_method,
            keyword_extraction_custom_prompt=keyword_extraction_custom_prompt,
            keyword_extraction_max_keywords=keyword_extraction_max_keywords,
            processing_rule=processing_rule,
            touchpoint_id=touchpoint_id,
            processing_rule_options=processing_rule_options,
            category_config=category_config,
            tag_config=tag_config,
            relation_config=relation_config,
            label_config=label_config,
        )

        return knowledge_dto
