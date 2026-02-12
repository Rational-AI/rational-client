from uuid import UUID

from rational_client.core import Knowledge
from rational_client.core.backend_clients import knowledge_client, management_client
from rational_client.deps.backend_knowledge_v0_client.api.knowledge import create_knowledge as create_knowledge_api
from rational_client.deps.backend_knowledge_v0_client.api.knowledge import delete_knowledge as delete_knowledge_api
from rational_client.deps.backend_knowledge_v0_client.models import (
    CreateKnowledgeRequest,
    KeywordExtractionMethod,
    KnowledgeDto,
)
from rational_client.deps.backend_knowledge_v0_client.types import UNSET
from rational_client.deps.backend_management_v0_client.api.models import list_model
from rational_client.deps.backend_management_v0_client.models import ModelDtoPage, ModelPurpose

_create_knowledge = create_knowledge_api.sync
_delete_knowledge = delete_knowledge_api.sync
_list_models = list_model.sync


def list_embedding_models():
    """
    List all available embedding models.
    """
    result = _list_models(client=management_client, purpose=ModelPurpose.EMBEDDING)
    if not isinstance(result, ModelDtoPage):
        raise TypeError(result)
    return result


def list_chat_models():
    """
    List all available chat/text generation models.
    """
    result = _list_models(client=management_client, purpose=ModelPurpose.TEXTGENERATION)
    if not isinstance(result, ModelDtoPage):
        raise TypeError(result)
    return result


def create_knowledge(
    name: str,
    allow_keywords_extraction: bool | None = None,
    keyword_extraction_method: KeywordExtractionMethod | None = None,
    keyword_extraction_max_keywords: int | None = None,
    keyword_extraction_custom_prompt: str | None = None,
):
    """
    Create a new knowledge base with embedding model and optional keyword extraction configuration.

    Parameters
    ----------
    name : str
        Name of the knowledge base
    allow_keywords_extraction : bool, optional
        Whether to enable keyword extraction (default: True in backend)
    keyword_extraction_method : KeywordExtractionMethod, optional
        Method to use for keyword extraction (LLM or RuleBased, default: LLM in backend)
    keyword_extraction_max_keywords : int, optional
        Maximum number of keywords to extract (default: 15)
    keyword_extraction_custom_prompt : str, optional
        Custom prompt for LLM-based keyword extraction

    Returns
    -------
    Knowledge
        The created Knowledge object
    """
    embedding_model = list_embedding_models().items[0]
    request = CreateKnowledgeRequest(
        name=name,
        enabled=True,
        embedding_model_id=embedding_model.id,
        allow_keywords_extraction=allow_keywords_extraction or UNSET,
        keyword_extraction_method=keyword_extraction_method or UNSET,
        keyword_extraction_max_keywords=keyword_extraction_max_keywords or UNSET,
        keyword_extraction_custom_prompt=keyword_extraction_custom_prompt or UNSET,
    )
    result = _create_knowledge(client=knowledge_client, body=request)
    if not isinstance(result, KnowledgeDto):
        raise TypeError(result)
    return Knowledge(knowledge_id=result.id, internal_dto=result)


def delete_knowledge(knowledge_id: UUID):
    """
    Delete the knowledge base.
    """
    result = _delete_knowledge(client=knowledge_client, id=knowledge_id)
    if result is not None:
        raise TypeError(result)
