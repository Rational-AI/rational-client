from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_knowledge_v0_knowledge_knowledge_id_resource_relations_sorting_item import (
    GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem,
)
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.rational_resource_relation_dto_page import RationalResourceRelationDtoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    knowledge_id: UUID,
    *,
    to_or_from_id: Union[Unset, UUID] = UNSET,
    from_id: Union[Unset, UUID] = UNSET,
    to_id: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_to_or_from_id: Union[Unset, str] = UNSET
    if not isinstance(to_or_from_id, Unset):
        json_to_or_from_id = str(to_or_from_id)
    params["toOrFromId"] = json_to_or_from_id

    json_from_id: Union[Unset, str] = UNSET
    if not isinstance(from_id, Unset):
        json_from_id = str(from_id)
    params["fromId"] = json_from_id

    json_to_id: Union[Unset, str] = UNSET
    if not isinstance(to_id, Unset):
        json_to_id = str(to_id)
    params["toId"] = json_to_id

    params["type"] = type_

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
        "url": f"/knowledge/v0/knowledge/{knowledge_id}/resource-relations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]:
    if response.status_code == 200:
        response_200 = RationalResourceRelationDtoPage.from_dict(response.json())

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
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    to_or_from_id: Union[Unset, UUID] = UNSET,
    from_id: Union[Unset, UUID] = UNSET,
    to_id: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (Union[Unset, UUID]):
        from_id (Union[Unset, UUID]):
        to_id (Union[Unset, UUID]):
        type_ (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset,
            list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        to_or_from_id=to_or_from_id,
        from_id=from_id,
        to_id=to_id,
        type_=type_,
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
    client: Union[AuthenticatedClient, Client],
    to_or_from_id: Union[Unset, UUID] = UNSET,
    from_id: Union[Unset, UUID] = UNSET,
    to_id: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (Union[Unset, UUID]):
        from_id (Union[Unset, UUID]):
        to_id (Union[Unset, UUID]):
        type_ (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset,
            list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        client=client,
        to_or_from_id=to_or_from_id,
        from_id=from_id,
        to_id=to_id,
        type_=type_,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    to_or_from_id: Union[Unset, UUID] = UNSET,
    from_id: Union[Unset, UUID] = UNSET,
    to_id: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (Union[Unset, UUID]):
        from_id (Union[Unset, UUID]):
        to_id (Union[Unset, UUID]):
        type_ (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset,
            list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        to_or_from_id=to_or_from_id,
        from_id=from_id,
        to_id=to_id,
        type_=type_,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    to_or_from_id: Union[Unset, UUID] = UNSET,
    from_id: Union[Unset, UUID] = UNSET,
    to_id: Union[Unset, UUID] = UNSET,
    type_: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]]:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (Union[Unset, UUID]):
        from_id (Union[Unset, UUID]):
        to_id (Union[Unset, UUID]):
        type_ (Union[Unset, str]):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset,
            list[GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, RationalResourceRelationDtoPage]
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            client=client,
            to_or_from_id=to_or_from_id,
            from_id=from_id,
            to_id=to_id,
            type_=type_,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
