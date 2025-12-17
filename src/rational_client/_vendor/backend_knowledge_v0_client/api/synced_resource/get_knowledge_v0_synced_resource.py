from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_knowledge_v0_synced_resource_sorting_item import GetKnowledgeV0SyncedResourceSortingItem
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.synced_resource_dto_page import SyncedResourceDtoPage
from ...models.synced_resource_status import SyncedResourceStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    knowledge_id: Union[Unset, UUID] = UNSET,
    knowledge_source_id: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, SyncedResourceStatus] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_knowledge_id: Union[Unset, str] = UNSET
    if not isinstance(knowledge_id, Unset):
        json_knowledge_id = str(knowledge_id)
    params["knowledgeId"] = json_knowledge_id

    json_knowledge_source_id: Union[Unset, str] = UNSET
    if not isinstance(knowledge_source_id, Unset):
        json_knowledge_source_id = str(knowledge_source_id)
    params["knowledgeSourceId"] = json_knowledge_source_id

    params["name"] = name

    json_parent_id: Union[Unset, str] = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parentId"] = json_parent_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["offset"] = offset

    params["limit"] = limit

    json_sorting: Union[Unset, list[str]] = UNSET
    if not isinstance(sorting, Unset):
        json_sorting = []
        for sorting_item_data in sorting:
            sorting_item = sorting_item_data.value
            json_sorting.append(sorting_item)

    params["sorting"] = json_sorting

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/knowledge/v0/synced-resource",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]:
    if response.status_code == 200:
        response_200 = SyncedResourceDtoPage.from_dict(response.json())

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
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    knowledge_id: Union[Unset, UUID] = UNSET,
    knowledge_source_id: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, SyncedResourceStatus] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]:
    """
    Args:
        knowledge_id (Union[Unset, UUID]):
        knowledge_source_id (Union[Unset, UUID]):
        name (Union[Unset, str]):
        parent_id (Union[Unset, UUID]):
        status (Union[Unset, SyncedResourceStatus]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        knowledge_source_id=knowledge_source_id,
        name=name,
        parent_id=parent_id,
        status=status,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    knowledge_id: Union[Unset, UUID] = UNSET,
    knowledge_source_id: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, SyncedResourceStatus] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]:
    """
    Args:
        knowledge_id (Union[Unset, UUID]):
        knowledge_source_id (Union[Unset, UUID]):
        name (Union[Unset, str]):
        parent_id (Union[Unset, UUID]):
        status (Union[Unset, SyncedResourceStatus]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]
    """

    return sync_detailed(
        client=client,
        knowledge_id=knowledge_id,
        knowledge_source_id=knowledge_source_id,
        name=name,
        parent_id=parent_id,
        status=status,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    knowledge_id: Union[Unset, UUID] = UNSET,
    knowledge_source_id: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, SyncedResourceStatus] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]:
    """
    Args:
        knowledge_id (Union[Unset, UUID]):
        knowledge_source_id (Union[Unset, UUID]):
        name (Union[Unset, str]):
        parent_id (Union[Unset, UUID]):
        status (Union[Unset, SyncedResourceStatus]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        knowledge_source_id=knowledge_source_id,
        name=name,
        parent_id=parent_id,
        status=status,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    knowledge_id: Union[Unset, UUID] = UNSET,
    knowledge_source_id: Union[Unset, UUID] = UNSET,
    name: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, UUID] = UNSET,
    status: Union[Unset, SyncedResourceStatus] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]]:
    """
    Args:
        knowledge_id (Union[Unset, UUID]):
        knowledge_source_id (Union[Unset, UUID]):
        name (Union[Unset, str]):
        parent_id (Union[Unset, UUID]):
        status (Union[Unset, SyncedResourceStatus]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[GetKnowledgeV0SyncedResourceSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, SyncedResourceDtoPage]
    """

    return (
        await asyncio_detailed(
            client=client,
            knowledge_id=knowledge_id,
            knowledge_source_id=knowledge_source_id,
            name=name,
            parent_id=parent_id,
            status=status,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
