from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.chunker_type import ChunkerType
from ..models.keyword_extraction_method import KeywordExtractionMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.color_config import ColorConfig
    from ..models.knowledge_source_config_update import KnowledgeSourceConfigUpdate
    from ..models.processing_rule_config import ProcessingRuleConfig


T = TypeVar("T", bound="UpdateKnowledgeRequest")


@_attrs_define
class UpdateKnowledgeRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        processing_rule (Union[Unset, ProcessingRuleConfig]):
        knowledge_sources (Union[Unset, list['KnowledgeSourceConfigUpdate']]):
        allow_ai_search (Union[Unset, bool]):
        allow_keywords_extraction (Union[Unset, bool]):
        keyword_extraction_method (Union[Unset, KeywordExtractionMethod]):
        keyword_extraction_custom_prompt (Union[None, Unset, str]):
        keyword_extraction_max_keywords (Union[None, Unset, int]):
        enabled (Union[Unset, bool]):
        chunker (Union[Unset, ChunkerType]):
        chunker_options (Union[Unset, Any]):
        embedding_model_id (Union[None, UUID, Unset]):
        category_config (Union[Unset, ColorConfig]):
        tag_config (Union[Unset, ColorConfig]):
        relation_config (Union[Unset, ColorConfig]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    processing_rule: Union[Unset, "ProcessingRuleConfig"] = UNSET
    knowledge_sources: Union[Unset, list["KnowledgeSourceConfigUpdate"]] = UNSET
    allow_ai_search: Union[Unset, bool] = UNSET
    allow_keywords_extraction: Union[Unset, bool] = UNSET
    keyword_extraction_method: Union[Unset, KeywordExtractionMethod] = UNSET
    keyword_extraction_custom_prompt: Union[None, Unset, str] = UNSET
    keyword_extraction_max_keywords: Union[None, Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    chunker: Union[Unset, ChunkerType] = UNSET
    chunker_options: Union[Unset, Any] = UNSET
    embedding_model_id: Union[None, UUID, Unset] = UNSET
    category_config: Union[Unset, "ColorConfig"] = UNSET
    tag_config: Union[Unset, "ColorConfig"] = UNSET
    relation_config: Union[Unset, "ColorConfig"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        processing_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.processing_rule, Unset):
            processing_rule = self.processing_rule.to_dict()

        knowledge_sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.knowledge_sources, Unset):
            knowledge_sources = []
            for knowledge_sources_item_data in self.knowledge_sources:
                knowledge_sources_item = knowledge_sources_item_data.to_dict()
                knowledge_sources.append(knowledge_sources_item)

        allow_ai_search = self.allow_ai_search

        allow_keywords_extraction = self.allow_keywords_extraction

        keyword_extraction_method: Union[Unset, str] = UNSET
        if not isinstance(self.keyword_extraction_method, Unset):
            keyword_extraction_method = self.keyword_extraction_method.value

        keyword_extraction_custom_prompt: Union[None, Unset, str]
        if isinstance(self.keyword_extraction_custom_prompt, Unset):
            keyword_extraction_custom_prompt = UNSET
        else:
            keyword_extraction_custom_prompt = self.keyword_extraction_custom_prompt

        keyword_extraction_max_keywords: Union[None, Unset, int]
        if isinstance(self.keyword_extraction_max_keywords, Unset):
            keyword_extraction_max_keywords = UNSET
        else:
            keyword_extraction_max_keywords = self.keyword_extraction_max_keywords

        enabled = self.enabled

        chunker: Union[Unset, str] = UNSET
        if not isinstance(self.chunker, Unset):
            chunker = self.chunker.value

        chunker_options = self.chunker_options

        embedding_model_id: Union[None, Unset, str]
        if isinstance(self.embedding_model_id, Unset):
            embedding_model_id = UNSET
        elif isinstance(self.embedding_model_id, UUID):
            embedding_model_id = str(self.embedding_model_id)
        else:
            embedding_model_id = self.embedding_model_id

        category_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category_config, Unset):
            category_config = self.category_config.to_dict()

        tag_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tag_config, Unset):
            tag_config = self.tag_config.to_dict()

        relation_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.relation_config, Unset):
            relation_config = self.relation_config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if chunker is not UNSET:
            field_dict["chunker"] = chunker
        if chunker_options is not UNSET:
            field_dict["chunkerOptions"] = chunker_options
        if embedding_model_id is not UNSET:
            field_dict["embeddingModelId"] = embedding_model_id
        if category_config is not UNSET:
            field_dict["categoryConfig"] = category_config
        if tag_config is not UNSET:
            field_dict["tagConfig"] = tag_config
        if relation_config is not UNSET:
            field_dict["relationConfig"] = relation_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_config import ColorConfig
        from ..models.knowledge_source_config_update import KnowledgeSourceConfigUpdate
        from ..models.processing_rule_config import ProcessingRuleConfig

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _processing_rule = d.pop("processingRule", UNSET)
        processing_rule: Union[Unset, ProcessingRuleConfig]
        if isinstance(_processing_rule, Unset):
            processing_rule = UNSET
        else:
            processing_rule = ProcessingRuleConfig.from_dict(_processing_rule)

        knowledge_sources = []
        _knowledge_sources = d.pop("knowledgeSources", UNSET)
        for knowledge_sources_item_data in _knowledge_sources or []:
            knowledge_sources_item = KnowledgeSourceConfigUpdate.from_dict(knowledge_sources_item_data)

            knowledge_sources.append(knowledge_sources_item)

        allow_ai_search = d.pop("allowAiSearch", UNSET)

        allow_keywords_extraction = d.pop("allowKeywordsExtraction", UNSET)

        _keyword_extraction_method = d.pop("keywordExtractionMethod", UNSET)
        keyword_extraction_method: Union[Unset, KeywordExtractionMethod]
        if isinstance(_keyword_extraction_method, Unset):
            keyword_extraction_method = UNSET
        else:
            keyword_extraction_method = KeywordExtractionMethod(_keyword_extraction_method)

        def _parse_keyword_extraction_custom_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        keyword_extraction_custom_prompt = _parse_keyword_extraction_custom_prompt(
            d.pop("keywordExtractionCustomPrompt", UNSET)
        )

        def _parse_keyword_extraction_max_keywords(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        keyword_extraction_max_keywords = _parse_keyword_extraction_max_keywords(
            d.pop("keywordExtractionMaxKeywords", UNSET)
        )

        enabled = d.pop("enabled", UNSET)

        _chunker = d.pop("chunker", UNSET)
        chunker: Union[Unset, ChunkerType]
        if isinstance(_chunker, Unset):
            chunker = UNSET
        else:
            chunker = ChunkerType(_chunker)

        chunker_options = d.pop("chunkerOptions", UNSET)

        def _parse_embedding_model_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                embedding_model_id_type_0 = UUID(data)

                return embedding_model_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        embedding_model_id = _parse_embedding_model_id(d.pop("embeddingModelId", UNSET))

        _category_config = d.pop("categoryConfig", UNSET)
        category_config: Union[Unset, ColorConfig]
        if isinstance(_category_config, Unset):
            category_config = UNSET
        else:
            category_config = ColorConfig.from_dict(_category_config)

        _tag_config = d.pop("tagConfig", UNSET)
        tag_config: Union[Unset, ColorConfig]
        if isinstance(_tag_config, Unset):
            tag_config = UNSET
        else:
            tag_config = ColorConfig.from_dict(_tag_config)

        _relation_config = d.pop("relationConfig", UNSET)
        relation_config: Union[Unset, ColorConfig]
        if isinstance(_relation_config, Unset):
            relation_config = UNSET
        else:
            relation_config = ColorConfig.from_dict(_relation_config)

        update_knowledge_request = cls(
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
            chunker=chunker,
            chunker_options=chunker_options,
            embedding_model_id=embedding_model_id,
            category_config=category_config,
            tag_config=tag_config,
            relation_config=relation_config,
        )

        return update_knowledge_request
