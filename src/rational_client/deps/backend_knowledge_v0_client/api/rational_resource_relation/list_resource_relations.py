from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_resource_relations_sorting_item import ListResourceRelationsSortingItem
from ...models.problem_details import ProblemDetails
from ...models.rational_resource_relation_dto_page import RationalResourceRelationDtoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    knowledge_id: UUID,
    *,
    to_or_from_id: UUID | Unset = UNSET,
    from_id: UUID | Unset = UNSET,
    to_id: UUID | Unset = UNSET,
    type_: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourceRelationsSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_to_or_from_id: str | Unset = UNSET
    if not isinstance(to_or_from_id, Unset):
        json_to_or_from_id = str(to_or_from_id)
    params["toOrFromId"] = json_to_or_from_id

    json_from_id: str | Unset = UNSET
    if not isinstance(from_id, Unset):
        json_from_id = str(from_id)
    params["fromId"] = json_from_id

    json_to_id: str | Unset = UNSET
    if not isinstance(to_id, Unset):
        json_to_id = str(to_id)
    params["toId"] = json_to_id

    params["type"] = type_

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
        "url": "/knowledge/v0/knowledge/{knowledge_id}/resource-relations".format(
            knowledge_id=quote(str(knowledge_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage]:
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
    to_or_from_id: UUID | Unset = UNSET,
    from_id: UUID | Unset = UNSET,
    to_id: UUID | Unset = UNSET,
    type_: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourceRelationsSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage]:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (UUID | Unset):
        from_id (UUID | Unset):
        to_id (UUID | Unset):
        type_ (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourceRelationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage]
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
    client: AuthenticatedClient | Client,
    to_or_from_id: UUID | Unset = UNSET,
    from_id: UUID | Unset = UNSET,
    to_id: UUID | Unset = UNSET,
    type_: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourceRelationsSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage | None:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (UUID | Unset):
        from_id (UUID | Unset):
        to_id (UUID | Unset):
        type_ (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourceRelationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage
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
    client: AuthenticatedClient | Client,
    to_or_from_id: UUID | Unset = UNSET,
    from_id: UUID | Unset = UNSET,
    to_id: UUID | Unset = UNSET,
    type_: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourceRelationsSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage]:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (UUID | Unset):
        from_id (UUID | Unset):
        to_id (UUID | Unset):
        type_ (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourceRelationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage]
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
    client: AuthenticatedClient | Client,
    to_or_from_id: UUID | Unset = UNSET,
    from_id: UUID | Unset = UNSET,
    to_id: UUID | Unset = UNSET,
    type_: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListResourceRelationsSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage | None:
    """
    Args:
        knowledge_id (UUID):
        to_or_from_id (UUID | Unset):
        from_id (UUID | Unset):
        to_id (UUID | Unset):
        type_ (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListResourceRelationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDtoPage
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
