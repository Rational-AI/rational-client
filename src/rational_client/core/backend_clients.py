from os import getenv

from backend_knowledge_v0_client.client import AuthenticatedClient as KnowledgeClient
from backend_management_v0_client.client import AuthenticatedClient as ManagementClient

BACKEND_ADDRESS = getenv("BACKEND_ADDRESS", "http://backend:14000/")
BACKEND_API_KEY = getenv("BACKEND_API_KEY", "")

knowledge_client = KnowledgeClient(
    base_url=BACKEND_ADDRESS,
    token=BACKEND_API_KEY,
)

management_client = ManagementClient(
    base_url=BACKEND_ADDRESS,
    token=BACKEND_API_KEY,
)


def _reset_client(client: KnowledgeClient | ManagementClient, base_url: str, api_key: str):
    if client._base_url != base_url or client.token != api_key:
        client._client = None
        client._async_client = None
        client._base_url = base_url
        client.token = api_key


def reset_credentials(base_url: str, api_key: str):
    _reset_client(knowledge_client, base_url, api_key)
    _reset_client(management_client, base_url, api_key)
