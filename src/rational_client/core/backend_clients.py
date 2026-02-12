from os import getenv

from rational_client.deps.backend_knowledge_v0_client.client import AuthenticatedClient as KnowledgeClient
from rational_client.deps.backend_management_v0_client.client import AuthenticatedClient as ManagementClient

BACKEND_ADDRESS = getenv("BACKEND_ADDRESS", "")
BACKEND_API_KEY = getenv("BACKEND_API_KEY", "")
RATIONALAI_TENANT = getenv("RATIONALAI_TENANT")

tenant_headers = {}
if RATIONALAI_TENANT:
    tenant_headers["X-RationalAI-Tenant"] = RATIONALAI_TENANT

knowledge_client = KnowledgeClient(
    base_url=BACKEND_ADDRESS,
    token=BACKEND_API_KEY,
    headers={**tenant_headers},
)

management_client = ManagementClient(
    base_url=BACKEND_ADDRESS,
    token=BACKEND_API_KEY,
    headers={**tenant_headers},
)


def _reset_client(
    client: KnowledgeClient | ManagementClient,
    base_url: str,
    api_key: str,
    tenant: str | None = None,
):
    headers = {"Authorization": f"Bearer {api_key}"}
    if tenant:
        headers["X-RationalAI-Tenant"] = tenant

    if client._base_url != base_url:
        client._client = None
        client._async_client = None
        client._base_url = base_url

    client.token = api_key
    client._headers = headers

    if client._client is not None:
        client._client.headers.update(headers)
    if client._async_client is not None:
        client._async_client.headers.update(headers)


def reset_credentials(base_url: str, api_key: str, tenant: str | None = None):
    _reset_client(knowledge_client, base_url, api_key, tenant)
    _reset_client(management_client, base_url, api_key, tenant)
