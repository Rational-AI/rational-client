from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.knowledge_graph_dto import KnowledgeGraphDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    query: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    knowledge_sources: list[UUID] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    params["category"] = category

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_knowledge_sources: list[str] | Unset = UNSET
    if not isinstance(knowledge_sources, Unset):
        json_knowledge_sources = []
        for knowledge_sources_item_data in knowledge_sources:
            knowledge_sources_item = str(knowledge_sources_item_data)
            json_knowledge_sources.append(knowledge_sources_item)

    params["knowledgeSources"] = json_knowledge_sources

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/knowledge/v0/knowledge/{id}/graph".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = KnowledgeGraphDto.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = HttpValidationProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    knowledge_sources: list[UUID] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails]:
    """
    Args:
        id (UUID):
        query (str | Unset):
        category (str | Unset):
        tags (list[str] | Unset):
        knowledge_sources (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        id=id,
        query=query,
        category=category,
        tags=tags,
        knowledge_sources=knowledge_sources,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    knowledge_sources: list[UUID] | Unset = UNSET,
) -> HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails | None:
    """
    Args:
        id (UUID):
        query (str | Unset):
        category (str | Unset):
        tags (list[str] | Unset):
        knowledge_sources (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails
    """

    return sync_detailed(
        id=id,
        client=client,
        query=query,
        category=category,
        tags=tags,
        knowledge_sources=knowledge_sources,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    knowledge_sources: list[UUID] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails]:
    """
    Args:
        id (UUID):
        query (str | Unset):
        category (str | Unset):
        tags (list[str] | Unset):
        knowledge_sources (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        id=id,
        query=query,
        category=category,
        tags=tags,
        knowledge_sources=knowledge_sources,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    category: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    knowledge_sources: list[UUID] | Unset = UNSET,
) -> HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails | None:
    """
    Args:
        id (UUID):
        query (str | Unset):
        category (str | Unset):
        tags (list[str] | Unset):
        knowledge_sources (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | KnowledgeGraphDto | ProblemDetails
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            query=query,
            category=category,
            tags=tags,
            knowledge_sources=knowledge_sources,
        )
    ).parsed
