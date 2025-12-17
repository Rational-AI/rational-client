import os
from uuid import UUID

from backend_knowledge_v0_client.api.knowledge import delete_knowledge_v0_knowledge_id, post_knowledge_v0_knowledge
from backend_knowledge_v0_client.client import AuthenticatedClient as KnowledgeClient
from backend_knowledge_v0_client.models import CreateKnowledgeRequest, KeywordExtractionMethod, KnowledgeDto
from backend_knowledge_v0_client.types import UNSET
from backend_management_v0_client.api.models import list_model
from backend_management_v0_client.client import AuthenticatedClient as ManagementClient
from backend_management_v0_client.models import ModelDtoPage, ModelPurpose
from rational_client.core import Knowledge

BACKEND_ADDRESS = os.getenv("BACKEND_ADDRESS", "http://backend:14000/")
BACKEND_API_KEY = os.getenv(
    "BACKEND_API_KEY",
    "test_AZ7Z6ON0dv7E8ggnqLlBJ0TbY8wEh5uCXcEtfgWOCNAaMqoGUcJ9Vr5hSO16EtnkCZ0HhSHaaQU1X6yncN6cEmuKD12Fk4bbflGpit8GlbM9AKrTZjWHrQykzpI",
)

os.environ["BACKEND_API_KEY"] = BACKEND_API_KEY


k_client = KnowledgeClient(
    base_url=BACKEND_ADDRESS,
    token=BACKEND_API_KEY,
)
m_client = ManagementClient(
    base_url=BACKEND_ADDRESS,
    token=BACKEND_API_KEY,
)

_create_knowledge = post_knowledge_v0_knowledge.sync
_delete_knowledge = delete_knowledge_v0_knowledge_id.sync
_list_models = list_model.sync


def list_embedding_models():
    """
    List all available embedding models.
    """
    result = _list_models(client=m_client, purpose=ModelPurpose.EMBEDDING)
    if not isinstance(result, ModelDtoPage):
        raise TypeError(result)
    return result


def list_chat_models():
    """
    List all available chat/text generation models.
    """
    result = _list_models(client=m_client, purpose=ModelPurpose.TEXTGENERATION)
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
    result = _create_knowledge(client=k_client, body=request)
    if not isinstance(result, KnowledgeDto):
        raise TypeError(result)
    return Knowledge(knowledge_id=result.id, internal_dto=result)


def delete_knowledge(knowledge_id: UUID):
    """
    Delete the knowledge base.
    """
    result = _delete_knowledge(client=k_client, id=knowledge_id)
    if result is not None:
        raise TypeError(result)
