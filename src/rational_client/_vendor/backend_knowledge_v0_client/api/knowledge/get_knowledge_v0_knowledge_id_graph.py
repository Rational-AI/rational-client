from http import HTTPStatus
from typing import Any, Optional, Union
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
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    knowledge_sources: Union[Unset, list[UUID]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["category"] = category

    json_tags: Union[Unset, list[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_knowledge_sources: Union[Unset, list[str]] = UNSET
    if not isinstance(knowledge_sources, Unset):
        json_knowledge_sources = []
        for knowledge_sources_item_data in knowledge_sources:
            knowledge_sources_item = str(knowledge_sources_item_data)
            json_knowledge_sources.append(knowledge_sources_item)

    params["knowledgeSources"] = json_knowledge_sources

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/knowledge/v0/knowledge/{id}/graph",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    knowledge_sources: Union[Unset, list[UUID]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]:
    """
    Args:
        id (UUID):
        query (Union[Unset, str]):
        category (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        knowledge_sources (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    knowledge_sources: Union[Unset, list[UUID]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]:
    """
    Args:
        id (UUID):
        query (Union[Unset, str]):
        category (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        knowledge_sources (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]
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
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    knowledge_sources: Union[Unset, list[UUID]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]:
    """
    Args:
        id (UUID):
        query (Union[Unset, str]):
        category (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        knowledge_sources (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    tags: Union[Unset, list[str]] = UNSET,
    knowledge_sources: Union[Unset, list[UUID]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]]:
    """
    Args:
        id (UUID):
        query (Union[Unset, str]):
        category (Union[Unset, str]):
        tags (Union[Unset, list[str]]):
        knowledge_sources (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeGraphDto, ProblemDetails]
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
