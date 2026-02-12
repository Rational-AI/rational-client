from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_resources_sorting_item import ListResourcesSortingItem
from ...models.problem_details import ProblemDetails
from ...models.rational_resource_dto_page import RationalResourceDtoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    knowledge_id: UUID,
    *,
    query: str | Unset = UNSET,
    synced_resource_id: UUID | Unset = UNSET,
    knowledge_source_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    categories: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourcesSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_synced_resource_id: str | Unset = UNSET
    if not isinstance(synced_resource_id, Unset):
        json_synced_resource_id = str(synced_resource_id)
    params["syncedResourceId"] = json_synced_resource_id

    json_knowledge_source_id: str | Unset = UNSET
    if not isinstance(knowledge_source_id, Unset):
        json_knowledge_source_id = str(knowledge_source_id)
    params["knowledgeSourceId"] = json_knowledge_source_id

    json_source_id: str | Unset = UNSET
    if not isinstance(source_id, Unset):
        json_source_id = str(source_id)
    params["sourceId"] = json_source_id

    json_categories: list[str] | Unset = UNSET
    if not isinstance(categories, Unset):
        json_categories = categories

    params["categories"] = json_categories

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params["offset"] = offset

    params["limit"] = limit

    json_sorting: list[str] | Unset = UNSET
    if not isinstance(sorting, Unset):
        json_sorting = []
        for sorting_item_data in sorting:
            sorting_item = sorting_item_data.value
            json_sorting.append(sorting_item)

    params["sorting"] = json_sorting

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/knowledge/v0/knowledge/{knowledge_id}/resource".format(
            knowledge_id=quote(str(knowledge_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage | None:
    if response.status_code == 200:
        response_200 = RationalResourceDtoPage.from_dict(response.json())

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
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    synced_resource_id: UUID | Unset = UNSET,
    knowledge_source_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    categories: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourcesSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage]:
    """
    Args:
        knowledge_id (UUID):
        query (str | Unset):
        synced_resource_id (UUID | Unset):
        knowledge_source_id (UUID | Unset):
        source_id (UUID | Unset):
        categories (list[str] | Unset):
        tags (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourcesSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        query=query,
        synced_resource_id=synced_resource_id,
        knowledge_source_id=knowledge_source_id,
        source_id=source_id,
        categories=categories,
        tags=tags,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    synced_resource_id: UUID | Unset = UNSET,
    knowledge_source_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    categories: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourcesSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage | None:
    """
    Args:
        knowledge_id (UUID):
        query (str | Unset):
        synced_resource_id (UUID | Unset):
        knowledge_source_id (UUID | Unset):
        source_id (UUID | Unset):
        categories (list[str] | Unset):
        tags (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourcesSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        client=client,
        query=query,
        synced_resource_id=synced_resource_id,
        knowledge_source_id=knowledge_source_id,
        source_id=source_id,
        categories=categories,
        tags=tags,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    synced_resource_id: UUID | Unset = UNSET,
    knowledge_source_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    categories: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourcesSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage]:
    """
    Args:
        knowledge_id (UUID):
        query (str | Unset):
        synced_resource_id (UUID | Unset):
        knowledge_source_id (UUID | Unset):
        source_id (UUID | Unset):
        categories (list[str] | Unset):
        tags (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourcesSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        query=query,
        synced_resource_id=synced_resource_id,
        knowledge_source_id=knowledge_source_id,
        source_id=source_id,
        categories=categories,
        tags=tags,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    synced_resource_id: UUID | Unset = UNSET,
    knowledge_source_id: UUID | Unset = UNSET,
    source_id: UUID | Unset = UNSET,
    categories: list[str] | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourcesSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage | None:
    """
    Args:
        knowledge_id (UUID):
        query (str | Unset):
        synced_resource_id (UUID | Unset):
        knowledge_source_id (UUID | Unset):
        source_id (UUID | Unset):
        categories (list[str] | Unset):
        tags (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourcesSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceDtoPage
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            client=client,
            query=query,
            synced_resource_id=synced_resource_id,
            knowledge_source_id=knowledge_source_id,
            source_id=source_id,
            categories=categories,
            tags=tags,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
