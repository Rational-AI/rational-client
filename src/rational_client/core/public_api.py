import json
import logging
from itertools import batched
from typing import Any, cast
from uuid import UUID

from pydantic import BaseModel

from rational_client.core.utils import get_openai_client
from rational_client.deps.backend_knowledge_v0_client.api.annotation import (
    create_annotation,
    delete_annotation,
    get_annotation,
    list_annotations,
    update_annotation,
)
from rational_client.deps.backend_knowledge_v0_client.api.knowledge import (
    find_similar_annotations,
    find_similar_resources,
    get_knowledge,
)
from rational_client.deps.backend_knowledge_v0_client.api.rational_resource import (
    create_resource,
    delete_resource,
    get_resource,
    get_resource_by_name,
    list_resources,
    update_resource,
)
from rational_client.deps.backend_knowledge_v0_client.api.rational_resource_relation import (
    create_resource_relation,
    delete_resource_relation,
    list_resource_relations,
    update_resource_relation,
)
from rational_client.deps.backend_knowledge_v0_client.api.synced_resource import (
    delete_synced_resource,
    get_synced_resource,
    get_synced_resource_contents,
    list_synced_resources,
    update_synced_resource,
    upload_synced_resource,
)
from rational_client.deps.backend_knowledge_v0_client.models import (
    AnnotationDto,
    AnnotationDtoPage,
    AnnotationType,
    BboxSelector,
    CreateAnnotationRequest,
    CreateResourceRelationRequest,
    CreateResourceRequest,
    KeywordExtractionMethod,
    KnowledgeDto,
    ListResourceRelationsSortingItem,
    ListResourcesSortingItem,
    ListSyncedResourcesSortingItem,
    RangeSelector,
    RationalResourceDto,
    RationalResourceDtoPage,
    RationalResourceRelationDto,
    RationalResourceRelationDtoPage,
    SearchRequest,
    SearchResultDto,
    Selector,
    SyncedResourceDto,
    SyncedResourceDtoPage,
    SyncedResourceStatus,
    UpdateAnnotationRequest,
    UpdateResourceRelationRequest,
    UpdateResourceRequest,
    UpdateSyncedResourceRequest,
    UploadSyncedResourceRequest,
)
from rational_client.deps.backend_knowledge_v0_client.models.list_annotations_sorting_item import (
    ListAnnotationsSortingItem,
)
from rational_client.deps.backend_knowledge_v0_client.types import UNSET, File, Unset
from rational_client.deps.backend_management_v0_client.api.touchpoints import get_touchpoint
from rational_client.deps.backend_management_v0_client.models import TouchpointDto

from .backend_clients import knowledge_client, management_client
from .chat_completion import chat_completion

SyncedResourceSorting = ListSyncedResourcesSortingItem
RationalResourceSorting = ListResourcesSortingItem
AnnotationResourceSorting = ListAnnotationsSortingItem
ResourceRelationSorting = ListResourceRelationsSortingItem


# Knowledge
_get_knowledge = get_knowledge.sync
_get_synced_resource = get_synced_resource.sync
_get_synced_resource_data = get_synced_resource_contents.sync_detailed
_upload_synced_resource = upload_synced_resource.sync
_update_synced_resource = update_synced_resource.sync
_list_synced_resource_paginated = list_synced_resources.sync
_delete_synced_resource = delete_synced_resource.sync
_create_rational_resource = create_resource.sync
_get_resource = get_resource.sync
_get_resource_by_name = get_resource_by_name.sync
_update_resource = update_resource.sync
_list_resources_paginated = list_resources.sync
_delete_resource = delete_resource.sync
_find_similar_annotations = find_similar_annotations.sync_detailed
_find_similar_resources = find_similar_resources.sync_detailed

# RationalResource
_list_annotations_paginated = list_annotations.sync
_get_annotation = get_annotation.sync
_update_annotation = update_annotation.sync
_create_annotation = create_annotation.sync
_delete_annotation = delete_annotation.sync
_create_resource_relation = create_resource_relation.sync
_list_resource_relations_paginated = list_resource_relations.sync
_delete_resource_relation = delete_resource_relation.sync
_update_resource_relation = update_resource_relation.sync


class Annotation:
    def __init__(
        self,
        id: UUID,
        knowledge_id: UUID,
        resource_id: UUID,
        internal_dto: AnnotationDto | None = None,
    ):
        self.annotation_id = id
        self.knowledge_id = knowledge_id
        self.rational_resource_id = resource_id
        self.internal_dto = internal_dto

    def _get_dto(self) -> AnnotationDto:
        if not self.internal_dto:
            result = _get_annotation(
                client=knowledge_client,
                knowledge_id=self.knowledge_id,
                resource_id=self.rational_resource_id,
                annotation_id=self.annotation_id,
            )
            if not isinstance(result, AnnotationDto):
                raise TypeError(result)  # TODO: Enhance error handling!
            self.internal_dto = result
        return self.internal_dto

    def save(self):
        dto = self._get_dto()
        request = UpdateAnnotationRequest(
            data=dto.data,
            keywords=dto.keywords,
            generated_resource_id=dto.generated_resource_id,
        )
        result = _update_annotation(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            resource_id=self.rational_resource_id,
            annotation_id=self.annotation_id,
            body=request,
        )
        if not isinstance(result, AnnotationDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        self.internal_dto = result

    def __getattr__(self, name):
        # Delegate attribute access to the DTO
        dto = self._get_dto()
        if hasattr(dto, name):
            return getattr(dto, name)
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")

    def __setattr__(self, name, value):
        # Allow normal setting for known attributes
        if name in {"knowledge_id", "rational_resource_id", "annotation_id", "internal_dto"}:
            super().__setattr__(name, value)
        else:
            dto = self._get_dto()
            if hasattr(dto, name):
                setattr(dto, name, value)
            else:
                super().__setattr__(name, value)

    def get_keywords(self) -> list[str]:
        """Get keywords from annotation keywords field"""
        dto = self._get_dto()
        return dto.keywords or []

    def set_keywords(self, keywords: list[str]):
        """Set keywords in annotation keywords field"""
        dto = self._get_dto()
        dto.keywords = keywords


class RationalResourceRelation:
    def __init__(
        self,
        id: UUID,
        knowledge_id: UUID,
        resource_id: UUID,
        related_resource_id: UUID,
        internal_dto: RationalResourceRelationDto | None = None,
    ):
        self.relation_id = id
        self.knowledge_id = knowledge_id
        self.resource_id = resource_id
        self.related_resource_id = related_resource_id
        self.internal_dto = internal_dto

    def _get_dto(self) -> RationalResourceRelationDto:
        if not self.internal_dto:
            raise NotImplementedError("Fetching DTO from backend is not implemented.")
        return self.internal_dto

    def save(self):
        # Save current type to backend
        dto = self._get_dto()
        request = UpdateResourceRelationRequest(type_=dto.type_)
        result = _update_resource_relation(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            id=self.relation_id,
            body=request,
        )
        if not isinstance(result, RationalResourceRelationDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        self.internal_dto = result

    @property
    def type(self):
        dto = self._get_dto()
        return dto.type_

    @type.setter
    def type(self, value: str):
        dto = self._get_dto()
        dto.type_ = value


class RationalResource:
    def __init__(
        self,
        knowledge_id: UUID,
        resource_id: UUID,
        internal_dto: RationalResourceDto | None = None,
    ):
        self.knowledge_id = knowledge_id
        self.resource_id = resource_id
        self.internal_dto = internal_dto

    def _get_dto(self):
        if not self.internal_dto:
            result = _get_resource(
                client=knowledge_client,
                knowledge_id=self.knowledge_id,
                resource_id=self.resource_id,
            )
            if not isinstance(result, RationalResourceDto):
                raise TypeError(result)  # TODO: Enhance error handling!
            self.internal_dto = result
        return self.internal_dto

    def save(self):
        dto = self._get_dto()
        request = UpdateResourceRequest(name=dto.name, notes=dto.notes, tags=dto.tags)
        result = _update_resource(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            resource_id=self.resource_id,
            body=request,
        )
        if not isinstance(result, RationalResourceDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        self.internal_dto = result

    def __getattr__(self, name):
        # Delegate attribute access to the DTO
        dto = self._get_dto()
        if hasattr(dto, name):
            return getattr(dto, name)
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")

    def __setattr__(self, name, value):
        # Allow normal setting for known attributes
        if name in {"knowledge_id", "resource_id", "internal_dto"}:
            super().__setattr__(name, value)
        else:
            dto = self._get_dto()
            if hasattr(dto, name):
                setattr(dto, name, value)
            else:
                super().__setattr__(name, value)

    def _get_annotations_paginated(
        self,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        sorting: list[AnnotationResourceSorting] | Unset = UNSET,
    ):
        result = _list_annotations_paginated(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            resource_id=self.resource_id,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
        if isinstance(result, AnnotationDtoPage):
            return result
        else:
            raise TypeError(result)

    def get_annotations(self):
        offset = 0
        while True:
            # sorting by creation timestamp guarantees that the whole collection
            # can be enumerated, assuming no elements are removed
            page = self._get_annotations_paginated(
                offset=offset,
                limit=100,
                sorting=[AnnotationResourceSorting.CREATEDAT],
            )
            for resource in page.items:
                yield Annotation(
                    knowledge_id=self.knowledge_id,
                    resource_id=resource.rational_resource_id,
                    id=resource.id,
                    internal_dto=resource,
                )
            offset += len(page.items)
            if page.count <= offset:
                return

    def add_annotation(
        self,
        annotation_type: AnnotationType,
        selector: Selector | BboxSelector | RangeSelector | None | Unset = UNSET,
        position: int | Unset = UNSET,
        title: str | None | Unset = UNSET,
        content: str | Unset = UNSET,
        label: str | None | Unset = UNSET,
        data: dict[str, Any] | None = None,
        embedding: list[float] | Unset = UNSET,
        generated_resource_id: UUID | None = None,
        keywords: list[str] | None = None,
        auto_extract_keywords: bool = True,
        enabled: bool = True,
    ) -> Annotation:
        """
        Add an annotation to this resource.

        Args:
            annotation_type: The type of annotation (e.g., CHUNK, IMAGE, etc.)
            data: Dictionary containing annotation data
            embedding: Optional pre-computed embedding vector
            generated_resource_id: Optional ID of a generated resource
            keywords: Optional list of keywords. If None and auto_extract_keywords is True,
                     keywords will be automatically extracted from text content based on
                     the Knowledge configuration (AllowKeywordsExtraction must be enabled).
            auto_extract_keywords: Whether to automatically extract keywords from text content
                                  when keywords are not provided (default: True). This still
                                  respects the Knowledge's AllowKeywordsExtraction setting.
            enabled: Whether the annotation is enabled (default: True)

        Returns:
            The created Annotation object
        """
        # Automatically extract keywords if not provided and auto_extract_keywords is enabled
        if keywords is None and auto_extract_keywords and data:
            # Get Knowledge to check configuration
            knowledge = Knowledge(self.knowledge_id)

            # Only proceed if keyword extraction is enabled in the Knowledge configuration
            knowledge_dto = knowledge._get_dto()
            if knowledge_dto.allow_keywords_extraction:
                # Try to extract text content from data
                text_content = None
                if isinstance(data, dict):
                    # Common field names for text content
                    for field in ["content", "text", "description", "notes"]:
                        if field in data and isinstance(data[field], str):
                            text_content = data[field]
                            break

                # If we found text content, extract keywords
                if text_content and len(text_content.strip()) > 0:
                    try:
                        keywords = knowledge.extract_keywords(text_content)
                    except Exception as e:
                        # Log warning but continue without keywords
                        import traceback

                        logging.warning(f"Failed to auto-extract keywords: {e}")
                        logging.debug(f"Traceback: {traceback.format_exc()}")
                        keywords = []
            else:
                logging.debug("Keyword extraction is disabled for this knowledge, skipping auto-extraction")

        selector_param: Selector | Unset = selector or UNSET  # type: ignore

        request = CreateAnnotationRequest(
            annotation_type=annotation_type,
            selector=selector_param,
            position=position,
            title=title,
            content=content,
            enabled=enabled,
            data=data,
            label=label,
            embedding=embedding,
            keywords=keywords,
            generated_resource_id=generated_resource_id,
        )
        result = _create_annotation(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            resource_id=self.resource_id,
            body=request,
        )
        if not isinstance(result, AnnotationDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return Annotation(
            knowledge_id=self.knowledge_id,
            resource_id=self.resource_id,
            id=result.id,
            internal_dto=result,
        )

    def delete_annotation(self, id: UUID):
        result = _delete_annotation(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            resource_id=self.resource_id,
            annotation_id=id,
        )
        if result is None:
            return result
        else:
            raise TypeError(result)

    def clear_annotations(self):
        annotations = self.get_annotations()
        for annotation in annotations:
            result = self.delete_annotation(annotation.annotation_id)
            if result is not None:
                raise TypeError(result)

    def add_relation(
        self,
        related_resource: "RationalResource",
        type: str,
    ):
        request = CreateResourceRelationRequest(
            from_resource_id=self.resource_id,
            to_resource_id=related_resource.resource_id,
            type_=type,
        )
        result = _create_resource_relation(client=knowledge_client, knowledge_id=self.knowledge_id, body=request)
        if not isinstance(result, RationalResourceRelationDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return RationalResourceRelation(
            id=result.id,
            knowledge_id=self.knowledge_id,
            resource_id=self.resource_id,
            related_resource_id=related_resource.resource_id,
            internal_dto=result,
        )

    def _get_relations_paginated(
        self,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        sorting: list[ResourceRelationSorting] | Unset = UNSET,
    ):
        result = _list_resource_relations_paginated(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            from_id=self.resource_id,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
        if isinstance(result, RationalResourceRelationDtoPage):
            return result
        else:
            raise TypeError(result)

    def get_relations(self):
        offset = 0
        while True:
            # sorting by creation timestamp guarantees that the whole collection
            # can be enumerated, assuming no elements are removed
            page = self._get_relations_paginated(
                offset=offset,
                limit=100,
                sorting=[ResourceRelationSorting.ID],  # TODO: Add createdAt sorting option?
            )
            for relation in page.items:
                yield RationalResourceRelation(
                    id=relation.id,
                    knowledge_id=self.knowledge_id,
                    resource_id=self.resource_id,
                    related_resource_id=relation.to_resource_id,
                    internal_dto=relation,
                )
            offset += len(page.items)
            if page.count <= offset:
                return

    def delete_relation(self, id: UUID):
        result = _delete_resource_relation(client=knowledge_client, knowledge_id=self.knowledge_id, id=id)
        if result is not None:
            raise TypeError(result)


class SyncedResource:
    def __init__(
        self,
        knowledge_id: UUID,
        id: UUID,
        internal_dto: SyncedResourceDto | None = None,
    ):
        self.knowledge_id = knowledge_id
        self.id = id
        self.internal_dto = internal_dto

    def _get_dto(self):
        if not self.internal_dto:
            result = _get_synced_resource(
                client=knowledge_client,
                id=self.id,
            )
            if not isinstance(result, SyncedResourceDto):
                raise TypeError(result)  # TODO: Enhance error handling!
            self.internal_dto = result
        return self.internal_dto

    def __getattr__(self, name):
        # Delegate attribute access to the DTO
        dto = self._get_dto()
        if hasattr(dto, name):
            return getattr(dto, name)
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")

    def get_data(self):
        result = _get_synced_resource_data(
            client=knowledge_client,
            id=self.id,
        )
        if result.status_code != 200:
            raise TypeError(result)  # TODO: Enhance error handling!
        return result.content


class Knowledge:
    def __init__(self, knowledge_id: UUID, internal_dto: KnowledgeDto | None = None):
        self.knowledge_id = knowledge_id
        self.internal_dto = internal_dto

    def _get_dto(self):
        if not self.internal_dto:
            result = _get_knowledge(client=knowledge_client, id=self.knowledge_id)
            if not isinstance(result, KnowledgeDto):
                raise TypeError(result)  # TODO: Enhance error handling!
            self.internal_dto = result
        return self.internal_dto

    def __getattr__(self, name):
        dto = self._get_dto()
        if hasattr(dto, name):
            return getattr(dto, name)
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")

    @property
    def embedding_model(self):
        dto = self._get_dto()
        return dto.embedding_model

    @property
    def touchpoint_id(self) -> UUID | None:
        """Get the touchpoint ID associated with this knowledge, if any."""
        dto = self._get_dto()
        touchpoint_id = dto.touchpoint_id
        if isinstance(touchpoint_id, Unset):
            return None
        return touchpoint_id

    def __setattr__(self, name, value):
        if name in {
            "knowledge_id",
            "internal_dto",
        }:
            super().__setattr__(name, value)
        else:
            dto = self._get_dto()
            if hasattr(dto, name):
                setattr(dto, name, value)
            else:
                super().__setattr__(name, value)

    def create_resource(
        self,
        name: str,
        category: str | None | Unset = UNSET,
        notes: str | None | Unset = UNSET,
        tags: list[str] | None | Unset = UNSET,
        synced_resource_id: UUID | None | Unset = UNSET,
    ):
        request = CreateResourceRequest(
            name=name,
            category=category,
            notes=notes,
            synced_resource_id=synced_resource_id,
            tags=tags,
        )
        result = _create_rational_resource(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            body=request,
        )
        if not isinstance(result, RationalResourceDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return RationalResource(
            knowledge_id=result.knowledge_id,
            resource_id=result.id,
            internal_dto=result,
        )

    def get_synced_resources_paginated(
        self,
        name: str | Unset = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        status: SyncedResourceStatus | Unset = UNSET,
        sorting: list[SyncedResourceSorting] | Unset = UNSET,
    ):
        result = _list_synced_resource_paginated(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            status=status,
            name=name,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
        if isinstance(result, SyncedResourceDtoPage):
            return result
        else:
            raise TypeError(result)

    def get_synced_resources(self):
        offset = 0
        while True:
            # sorting by creation timestamp guarantees that the whole collection
            # can be enumerated, assuming no elements are removed
            page = self.get_synced_resources_paginated(
                offset=offset,
                limit=100,
                sorting=[SyncedResourceSorting.CREATEDAT],
            )
            for resource in page.items:
                yield SyncedResource(
                    knowledge_id=resource.knowledge_id,
                    id=resource.id,
                    internal_dto=resource,
                )
            offset += len(page.items)
            if page.count <= offset:
                return

    def delete_synced_resource(self, id: UUID):
        result = _delete_synced_resource(client=knowledge_client, id=id)
        if result is None:
            return result
        else:
            raise TypeError(result)

    def update_synced_resource(
        self,
        id: UUID,
        name: str | Unset = UNSET,
        status: SyncedResourceStatus | Unset = UNSET,
        processing_workflow_id: UUID | None | Unset = UNSET,
        processing_workflow_options: Any | Unset = UNSET,
    ):
        request = UpdateSyncedResourceRequest(
            name=name,
            status=status,
            processing_workflow_id=processing_workflow_id,
            processing_workflow_options=processing_workflow_options,
        )
        result = _update_synced_resource(
            client=knowledge_client,
            id=id,
            body=request,
        )
        if not isinstance(result, SyncedResourceDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return SyncedResource(
            knowledge_id=result.knowledge_id,
            id=result.id,
            internal_dto=result,
        )

    def upload_synced_resource(
        self,
        name: str,
        contents: File,
        parent_id: UUID | Unset = UNSET,
    ):
        result = _upload_synced_resource(
            client=knowledge_client,
            body=UploadSyncedResourceRequest(
                name=name,
                data=contents,
                knowledge_id=self.knowledge_id,
                parent_id=parent_id,
            ),
        )
        if not isinstance(result, SyncedResourceDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return SyncedResource(
            knowledge_id=result.knowledge_id,
            id=result.id,
            internal_dto=result,
        )

    def get_resources_paginated(
        self,
        synced_resource_id: UUID | Unset = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        sorting: list[RationalResourceSorting] | Unset = UNSET,
        tags: list[str] | Unset = UNSET,
    ):
        result = _list_resources_paginated(
            client=knowledge_client,
            knowledge_id=self.knowledge_id,
            synced_resource_id=synced_resource_id,
            offset=offset,
            limit=limit,
            sorting=sorting,
            tags=tags,
        )
        if isinstance(result, RationalResourceDtoPage):
            return result
        else:
            raise TypeError(result)

    def get_resources(
        self,
        synced_resource_id: UUID | Unset = UNSET,
        tags: list[str] | Unset = UNSET,
    ):
        offset = 0
        while True:
            # sorting by creation timestamp guarantees that the whole collection
            # can be enumerated, assuming no elements are removed
            page = self.get_resources_paginated(
                synced_resource_id,
                offset=offset,
                limit=100,
                sorting=[RationalResourceSorting.CREATEDAT],
                tags=tags,
            )
            for resource in page.items:
                yield RationalResource(
                    knowledge_id=resource.knowledge_id,
                    resource_id=resource.id,
                    internal_dto=resource,
                )
            offset += len(page.items)
            if page.count <= offset:
                return

    def get_resource(self, id: UUID):
        result = _get_resource(client=knowledge_client, knowledge_id=self.knowledge_id, resource_id=id)
        if not isinstance(result, RationalResourceDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return RationalResource(
            knowledge_id=result.knowledge_id,
            resource_id=result.id,
            internal_dto=result,
        )

    def get_resource_by_name(self, name: str):
        result = _get_resource_by_name(client=knowledge_client, knowledge_id=self.knowledge_id, resource_name=name)
        if not isinstance(result, RationalResourceDto):
            raise TypeError(result)  # TODO: Enhance error handling!
        return RationalResource(
            knowledge_id=result.knowledge_id,
            resource_id=result.id,
            internal_dto=result,
        )

    def delete_resource(self, id: UUID):
        result = _delete_resource(client=knowledge_client, knowledge_id=self.knowledge_id, resource_id=id)
        if result is None:
            return result
        else:
            raise TypeError(result)

    def find_similar(self, query_vector: list[float], top_k: int = 10):
        """
        Find similar annotations based on a query vector.
        """
        request = SearchRequest(
            query_vector=query_vector,
            top_k=top_k,
        )
        result = _find_similar_annotations(
            client=knowledge_client,
            id=self.knowledge_id,
            body=request,
        )
        if result.status_code.is_success:
            return cast(list[SearchResultDto], result.parsed)
        else:
            raise TypeError(result.parsed)

    def find_similar_resources(self, query_vector: list[float], top_k: int = 10):
        """
        Find similar resources based on a query vector.
        """
        request = SearchRequest(
            query_vector=query_vector,
            top_k=top_k,
        )
        result = _find_similar_resources(client=knowledge_client, id=self.knowledge_id, body=request)
        if result.status_code.is_success:
            return cast(list[SearchResultDto], result.parsed)
        else:
            raise TypeError(result.parsed)

    def embed_one(self, text: str) -> list[float]:
        """
        Embed a text string into a vector representation.
        """
        return self.embed_batch([text])[0]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Embed a batch of text strings into vector representations.
        """
        if not self.embedding_model:
            raise ValueError("No embedding model set on the knowledge")

        embeddings = get_openai_client().embeddings

        result = []
        # use a batch size compatible with TEI defaults
        for batch in batched(texts, 32):
            response = embeddings.create(model=self.embedding_model.model_identifier, input=list(batch))
            if not response or not response.data or not all(item.embedding for item in response.data):
                raise ValueError("Failed to get embeddings from OpenAI API.")
            result.extend(item.embedding for item in response.data)

        return result

    def get_token_count(self, text: str) -> int:
        """
        Get the token count for a given text.
        """
        if not self.embedding_model:
            raise ValueError("No embedding model set on the knowledge")

        response = get_openai_client().embeddings.create(model=self.embedding_model.model_identifier, input=[text])
        if not response or not response.usage:
            raise ValueError("Failed to get token count from OpenAI API.")

        return response.usage.total_tokens

    def extract_keywords(self, text: str, max_keywords: int | None = None) -> list[str]:
        """
        Extract keywords from text using the configured extraction method.

        Extraction method and parameters are taken from the Knowledge configuration:
        - AllowKeywordsExtraction: whether keyword extraction is enabled
        - KeywordExtractionMethod: LLM or RuleBased
        - KeywordExtractionCustomPrompt: custom prompt for LLM method (optional)
        - KeywordExtractionMaxKeywords: max number of keywords to extract (default: 15)

        Args:
            text: The text to extract keywords from
            max_keywords: Optional override for maximum number of keywords.
                         If None, uses KeywordExtractionMaxKeywords from configuration,
                         or defaults to 15.

        Returns:
            A list of extracted keywords, or empty list if extraction is disabled
        """
        dto = self._get_dto()

        # Check if keyword extraction is enabled
        if dto.allow_keywords_extraction is None or not dto.allow_keywords_extraction:
            logging.debug("Keyword extraction is disabled for this knowledge")
            return []

        # Determine max_keywords from configuration or parameter
        if max_keywords is None:
            max_keywords = dto.keyword_extraction_max_keywords if dto.keyword_extraction_max_keywords else 15

        # Get the extraction method (default to LLM if not specified)
        extraction_method = (
            dto.keyword_extraction_method if dto.keyword_extraction_method else KeywordExtractionMethod.LLM
        )

        # Route to appropriate extraction method
        if extraction_method == KeywordExtractionMethod.RULEBASED:
            logging.debug(f"Using rule-based keyword extraction (max_keywords={max_keywords})")
            from .rule_based_keywords import extract_keywords_rule_based

            return extract_keywords_rule_based(text, max_keywords=max_keywords)
        else:  # LLM method
            return self._extract_keywords_llm(text, max_keywords=max_keywords)

    def _extract_keywords_llm(self, text: str, max_keywords: int = 15) -> list[str]:
        """
        Extract keywords from text using an LLM with structured output.

        Args:
            text: The text to extract keywords from
            max_keywords: Maximum number of keywords to extract

        Returns:
            A list of extracted keywords
        """
        dto = self._get_dto()
        model_name = None

        # Use model from touchpoint if knowledge has a touchpoint
        if self.touchpoint_id:
            try:
                touchpoint_result = get_touchpoint.sync(
                    client=management_client,
                    id=self.touchpoint_id,
                )
                if isinstance(touchpoint_result, TouchpointDto) and touchpoint_result.default_model:
                    model_name = touchpoint_result.default_model.model_identifier
                    logging.debug(f"Using model from touchpoint: {model_name}")
            except Exception as e:
                logging.error(f"Failed to get model from touchpoint: {e}")
                raise

        # Verify we have required model information
        if not model_name:
            error_msg = (
                "No model available for keyword extraction. "
                "Knowledge must have a touchpoint with a default model configured."
            )
            logging.error(error_msg)
            raise ValueError(error_msg)

        class KeywordsSchema(BaseModel):
            keywords: list[str]

        # Use custom prompt if provided, otherwise use default
        if dto.keyword_extraction_custom_prompt:
            prompt = f"""{dto.keyword_extraction_custom_prompt}

Text to analyze:
{text}"""
        else:
            # Default prompt
            prompt = f"""Extract the most relevant keywords from the following text.

Guidelines:
- Keywords should be specific and meaningful terms, relevant to the main topics and concepts
- Avoid stop words
- Extract between 5 and {max_keywords} keywords

Examples:

Text: "Machine learning enables computers to learn from data without being explicitly programmed."
Keywords: ["machine learning", "artificial intelligence", "algorithms", "data"]

Text: "The quarterly financial report shows revenue increased by 15% compared to last year."
Keywords: ["quarterly financial report", "revenue", "15% increase", "sales growth"]

Text to analyze:
{text}"""

        try:
            # Convert Pydantic model to OpenAI response format
            response_format = {
                "type": "json_schema",
                "json_schema": {
                    "name": "keyword_extraction",
                    "strict": True,
                    "schema": KeywordsSchema.model_json_schema(),
                },
            }

            # Use the chat_completion function with structured output
            raw_content = chat_completion(
                model_name=model_name,
                prompt=prompt,
                max_tokens=300,
                temperature=0.3,
                response_format=response_format,
            )

            if not raw_content:
                raise ValueError("Failed to get keyword extraction response from LLM.")

            # Parse using Pydantic
            result = KeywordsSchema.model_validate_json(raw_content)

            # Limit to max_keywords and ensure all items are strings
            return [str(kw) for kw in result.keywords[:max_keywords]]

        except json.JSONDecodeError as e:
            logging.warning(f"Failed to parse JSON from LLM response: {e}")
            return []
        except Exception as e:
            logging.warning(f"Keyword extraction failed: {e}")
            return []
