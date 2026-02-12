from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_user_sorting_item import ListUserSortingItem
from ...models.problem_details import ProblemDetails
from ...models.user_dto_page import UserDtoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_id: UUID | Unset = UNSET,
    authentication_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListUserSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_group_id: str | Unset = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = str(group_id)
    params["groupId"] = json_group_id

    params["authenticationId"] = authentication_id

    params["query"] = query

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
        "url": "/management/v0/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | ProblemDetails | UserDtoPage | None:
    if response.status_code == 200:
        response_200 = UserDtoPage.from_dict(response.json())

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
) -> Response[HttpValidationProblemDetails | ProblemDetails | UserDtoPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    authentication_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListUserSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | UserDtoPage]:
    """
    Args:
        group_id (UUID | Unset):
        authentication_id (str | Unset):
        query (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListUserSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | UserDtoPage]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        authentication_id=authentication_id,
        query=query,
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
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    authentication_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListUserSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | UserDtoPage | None:
    """
    Args:
        group_id (UUID | Unset):
        authentication_id (str | Unset):
        query (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListUserSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | UserDtoPage
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        authentication_id=authentication_id,
        query=query,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    authentication_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListUserSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | UserDtoPage]:
    """
    Args:
        group_id (UUID | Unset):
        authentication_id (str | Unset):
        query (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListUserSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | UserDtoPage]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        authentication_id=authentication_id,
        query=query,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    group_id: UUID | Unset = UNSET,
    authentication_id: str | Unset = UNSET,
    query: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListUserSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | UserDtoPage | None:
    """
    Args:
        group_id (UUID | Unset):
        authentication_id (str | Unset):
        query (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListUserSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | UserDtoPage
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            authentication_id=authentication_id,
            query=query,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
