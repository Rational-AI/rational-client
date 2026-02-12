from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_dto_page import EventDtoPage
from ...models.event_type import EventType
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_events_sorting_item import ListEventsSortingItem
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    room_id: UUID,
    *,
    type_: EventType | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListEventsSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

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
        "url": "/chat/v0/rooms/{room_id}/events".format(
            room_id=quote(str(room_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventDtoPage | HttpValidationProblemDetails | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = EventDtoPage.from_dict(response.json())

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
) -> Response[EventDtoPage | HttpValidationProblemDetails | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    type_: EventType | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListEventsSortingItem] | Unset = UNSET,
) -> Response[EventDtoPage | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        room_id (UUID):
        type_ (EventType | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListEventsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventDtoPage | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
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
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    type_: EventType | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListEventsSortingItem] | Unset = UNSET,
) -> EventDtoPage | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        room_id (UUID):
        type_ (EventType | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListEventsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventDtoPage | HttpValidationProblemDetails | ProblemDetails
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        type_=type_,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    type_: EventType | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListEventsSortingItem] | Unset = UNSET,
) -> Response[EventDtoPage | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        room_id (UUID):
        type_ (EventType | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListEventsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventDtoPage | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        type_=type_,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    type_: EventType | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListEventsSortingItem] | Unset = UNSET,
) -> EventDtoPage | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        room_id (UUID):
        type_ (EventType | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListEventsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventDtoPage | HttpValidationProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            type_=type_,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
