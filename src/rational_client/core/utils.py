from httpx import URL
from openai import OpenAI

from .backend_clients import knowledge_client


def get_openai_client() -> OpenAI:
    """Get an OpenAI client configured to use the Rational backend's OpenAI compatibility layer."""
    return OpenAI(
        base_url=URL(knowledge_client._base_url).join("./compat/v0/openai"),
        api_key=knowledge_client.token,
        default_headers=knowledge_client._headers,
    )
