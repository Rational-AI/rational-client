from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.chunker_type import ChunkerType
from ..models.keyword_extraction_method import KeywordExtractionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.color_config import ColorConfig
    from ..models.knowledge_source_config import KnowledgeSourceConfig
    from ..models.processing_rule_config import ProcessingRuleConfig


T = TypeVar("T", bound="CreateKnowledgeRequest")


@_attrs_define
class CreateKnowledgeRequest:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        processing_rule (ProcessingRuleConfig | Unset):
        knowledge_sources (list[KnowledgeSourceConfig] | None | Unset):
        allow_ai_search (bool | None | Unset):
        allow_keywords_extraction (bool | None | Unset):
        keyword_extraction_method (KeywordExtractionMethod | Unset):
        keyword_extraction_custom_prompt (None | str | Unset):
        keyword_extraction_max_keywords (int | None | Unset):
        enabled (bool | None | Unset):
        embedding_model_id (None | Unset | UUID):
        chunker (ChunkerType | Unset):
        chunker_options (Any | Unset):
        category_config (ColorConfig | Unset):
        tag_config (ColorConfig | Unset):
        relation_config (ColorConfig | Unset):
        label_config (ColorConfig | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    processing_rule: ProcessingRuleConfig | Unset = UNSET
    knowledge_sources: list[KnowledgeSourceConfig] | None | Unset = UNSET
    allow_ai_search: bool | None | Unset = UNSET
    allow_keywords_extraction: bool | None | Unset = UNSET
    keyword_extraction_method: KeywordExtractionMethod | Unset = UNSET
    keyword_extraction_custom_prompt: None | str | Unset = UNSET
    keyword_extraction_max_keywords: int | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    embedding_model_id: None | Unset | UUID = UNSET
    chunker: ChunkerType | Unset = UNSET
    chunker_options: Any | Unset = UNSET
    category_config: ColorConfig | Unset = UNSET
    tag_config: ColorConfig | Unset = UNSET
    relation_config: ColorConfig | Unset = UNSET
    label_config: ColorConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        processing_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.processing_rule, Unset):
            processing_rule = self.processing_rule.to_dict()

        knowledge_sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.knowledge_sources, Unset):
            knowledge_sources = UNSET
        elif isinstance(self.knowledge_sources, list):
            knowledge_sources = []
            for knowledge_sources_type_0_item_data in self.knowledge_sources:
                knowledge_sources_type_0_item = knowledge_sources_type_0_item_data.to_dict()
                knowledge_sources.append(knowledge_sources_type_0_item)

        else:
            knowledge_sources = self.knowledge_sources

        allow_ai_search: bool | None | Unset
        if isinstance(self.allow_ai_search, Unset):
            allow_ai_search = UNSET
        else:
            allow_ai_search = self.allow_ai_search

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

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        embedding_model_id: None | str | Unset
        if isinstance(self.embedding_model_id, Unset):
            embedding_model_id = UNSET
        elif isinstance(self.embedding_model_id, UUID):
            embedding_model_id = str(self.embedding_model_id)
        else:
            embedding_model_id = self.embedding_model_id

        chunker: str | Unset = UNSET
        if not isinstance(self.chunker, Unset):
            chunker = self.chunker.value

        chunker_options = self.chunker_options

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
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if processing_rule is not UNSET:
            field_dict["processingRule"] = processing_rule
        if knowledge_sources is not UNSET:
            field_dict["knowledgeSources"] = knowledge_sources
        if allow_ai_search is not UNSET:
            field_dict["allowAiSearch"] = allow_ai_search
        if allow_keywords_extraction is not UNSET:
            field_dict["allowKeywordsExtraction"] = allow_keywords_extraction
        if keyword_extraction_method is not UNSET:
            field_dict["keywordExtractionMethod"] = keyword_extraction_method
        if keyword_extraction_custom_prompt is not UNSET:
            field_dict["keywordExtractionCustomPrompt"] = keyword_extraction_custom_prompt
        if keyword_extraction_max_keywords is not UNSET:
            field_dict["keywordExtractionMaxKeywords"] = keyword_extraction_max_keywords
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if embedding_model_id is not UNSET:
            field_dict["embeddingModelId"] = embedding_model_id
        if chunker is not UNSET:
            field_dict["chunker"] = chunker
        if chunker_options is not UNSET:
            field_dict["chunkerOptions"] = chunker_options
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
        from ..models.knowledge_source_config import KnowledgeSourceConfig
        from ..models.processing_rule_config import ProcessingRuleConfig

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _processing_rule = d.pop("processingRule", UNSET)
        processing_rule: ProcessingRuleConfig | Unset
        if isinstance(_processing_rule, Unset):
            processing_rule = UNSET
        else:
            processing_rule = ProcessingRuleConfig.from_dict(_processing_rule)

        def _parse_knowledge_sources(data: object) -> list[KnowledgeSourceConfig] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                knowledge_sources_type_0 = []
                _knowledge_sources_type_0 = data
                for knowledge_sources_type_0_item_data in _knowledge_sources_type_0:
                    knowledge_sources_type_0_item = KnowledgeSourceConfig.from_dict(knowledge_sources_type_0_item_data)

                    knowledge_sources_type_0.append(knowledge_sources_type_0_item)

                return knowledge_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[KnowledgeSourceConfig] | None | Unset, data)

        knowledge_sources = _parse_knowledge_sources(d.pop("knowledgeSources", UNSET))

        def _parse_allow_ai_search(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_ai_search = _parse_allow_ai_search(d.pop("allowAiSearch", UNSET))

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

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_embedding_model_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                embedding_model_id_type_0 = UUID(data)

                return embedding_model_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        embedding_model_id = _parse_embedding_model_id(d.pop("embeddingModelId", UNSET))

        _chunker = d.pop("chunker", UNSET)
        chunker: ChunkerType | Unset
        if isinstance(_chunker, Unset):
            chunker = UNSET
        else:
            chunker = ChunkerType(_chunker)

        chunker_options = d.pop("chunkerOptions", UNSET)

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

        create_knowledge_request = cls(
            name=name,
            description=description,
            processing_rule=processing_rule,
            knowledge_sources=knowledge_sources,
            allow_ai_search=allow_ai_search,
            allow_keywords_extraction=allow_keywords_extraction,
            keyword_extraction_method=keyword_extraction_method,
            keyword_extraction_custom_prompt=keyword_extraction_custom_prompt,
            keyword_extraction_max_keywords=keyword_extraction_max_keywords,
            enabled=enabled,
            embedding_model_id=embedding_model_id,
            chunker=chunker,
            chunker_options=chunker_options,
            category_config=category_config,
            tag_config=tag_config,
            relation_config=relation_config,
            label_config=label_config,
        )

        return create_knowledge_request
