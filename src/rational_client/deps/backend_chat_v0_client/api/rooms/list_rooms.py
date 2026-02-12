from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignee_type import AssigneeType
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_rooms_sorting_item import ListRoomsSortingItem
from ...models.problem_details import ProblemDetails
from ...models.room_dto_page import RoomDtoPage
from ...models.room_status import RoomStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: RoomStatus | Unset = UNSET,
    assignee_type: AssigneeType | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    sentiment: str | Unset = UNSET,
    topic: str | Unset = UNSET,
    query: str | Unset = UNSET,
    has_messages: bool | Unset = UNSET,
    is_starred: bool | Unset = UNSET,
    touchpoint_ids: list[UUID] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListRoomsSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_assignee_type: str | Unset = UNSET
    if not isinstance(assignee_type, Unset):
        json_assignee_type = assignee_type.value

    params["assigneeType"] = json_assignee_type

    json_assignee_id: str | Unset = UNSET
    if not isinstance(assignee_id, Unset):
        json_assignee_id = str(assignee_id)
    params["assigneeId"] = json_assignee_id

    params["sentiment"] = sentiment

    params["topic"] = topic

    params["query"] = query

    params["hasMessages"] = has_messages

    params["isStarred"] = is_starred

    json_touchpoint_ids: list[str] | Unset = UNSET
    if not isinstance(touchpoint_ids, Unset):
        json_touchpoint_ids = []
        for touchpoint_ids_item_data in touchpoint_ids:
            touchpoint_ids_item = str(touchpoint_ids_item_data)
            json_touchpoint_ids.append(touchpoint_ids_item)

    params["touchpointIds"] = json_touchpoint_ids

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
        "url": "/chat/v0/rooms",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | ProblemDetails | RoomDtoPage | None:
    if response.status_code == 200:
        response_200 = RoomDtoPage.from_dict(response.json())

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
) -> Response[HttpValidationProblemDetails | ProblemDetails | RoomDtoPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: RoomStatus | Unset = UNSET,
    assignee_type: AssigneeType | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    sentiment: str | Unset = UNSET,
    topic: str | Unset = UNSET,
    query: str | Unset = UNSET,
    has_messages: bool | Unset = UNSET,
    is_starred: bool | Unset = UNSET,
    touchpoint_ids: list[UUID] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListRoomsSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RoomDtoPage]:
    """
    Args:
        status (RoomStatus | Unset):
        assignee_type (AssigneeType | Unset):
        assignee_id (UUID | Unset):
        sentiment (str | Unset):
        topic (str | Unset):
        query (str | Unset):
        has_messages (bool | Unset):
        is_starred (bool | Unset):
        touchpoint_ids (list[UUID] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListRoomsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RoomDtoPage]
    """

    kwargs = _get_kwargs(
        status=status,
        assignee_type=assignee_type,
        assignee_id=assignee_id,
        sentiment=sentiment,
        topic=topic,
        query=query,
        has_messages=has_messages,
        is_starred=is_starred,
        touchpoint_ids=touchpoint_ids,
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
    status: RoomStatus | Unset = UNSET,
    assignee_type: AssigneeType | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    sentiment: str | Unset = UNSET,
    topic: str | Unset = UNSET,
    query: str | Unset = UNSET,
    has_messages: bool | Unset = UNSET,
    is_starred: bool | Unset = UNSET,
    touchpoint_ids: list[UUID] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListRoomsSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | RoomDtoPage | None:
    """
    Args:
        status (RoomStatus | Unset):
        assignee_type (AssigneeType | Unset):
        assignee_id (UUID | Unset):
        sentiment (str | Unset):
        topic (str | Unset):
        query (str | Unset):
        has_messages (bool | Unset):
        is_starred (bool | Unset):
        touchpoint_ids (list[UUID] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListRoomsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RoomDtoPage
    """

    return sync_detailed(
        client=client,
        status=status,
        assignee_type=assignee_type,
        assignee_id=assignee_id,
        sentiment=sentiment,
        topic=topic,
        query=query,
        has_messages=has_messages,
        is_starred=is_starred,
        touchpoint_ids=touchpoint_ids,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: RoomStatus | Unset = UNSET,
    assignee_type: AssigneeType | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    sentiment: str | Unset = UNSET,
    topic: str | Unset = UNSET,
    query: str | Unset = UNSET,
    has_messages: bool | Unset = UNSET,
    is_starred: bool | Unset = UNSET,
    touchpoint_ids: list[UUID] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListRoomsSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RoomDtoPage]:
    """
    Args:
        status (RoomStatus | Unset):
        assignee_type (AssigneeType | Unset):
        assignee_id (UUID | Unset):
        sentiment (str | Unset):
        topic (str | Unset):
        query (str | Unset):
        has_messages (bool | Unset):
        is_starred (bool | Unset):
        touchpoint_ids (list[UUID] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListRoomsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RoomDtoPage]
    """

    kwargs = _get_kwargs(
        status=status,
        assignee_type=assignee_type,
        assignee_id=assignee_id,
        sentiment=sentiment,
        topic=topic,
        query=query,
        has_messages=has_messages,
        is_starred=is_starred,
        touchpoint_ids=touchpoint_ids,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: RoomStatus | Unset = UNSET,
    assignee_type: AssigneeType | Unset = UNSET,
    assignee_id: UUID | Unset = UNSET,
    sentiment: str | Unset = UNSET,
    topic: str | Unset = UNSET,
    query: str | Unset = UNSET,
    has_messages: bool | Unset = UNSET,
    is_starred: bool | Unset = UNSET,
    touchpoint_ids: list[UUID] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListRoomsSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | ProblemDetails | RoomDtoPage | None:
    """
    Args:
        status (RoomStatus | Unset):
        assignee_type (AssigneeType | Unset):
        assignee_id (UUID | Unset):
        sentiment (str | Unset):
        topic (str | Unset):
        query (str | Unset):
        has_messages (bool | Unset):
        is_starred (bool | Unset):
        touchpoint_ids (list[UUID] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListRoomsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RoomDtoPage
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            assignee_type=assignee_type,
            assignee_id=assignee_id,
            sentiment=sentiment,
            topic=topic,
            query=query,
            has_messages=has_messages,
            is_starred=is_starred,
            touchpoint_ids=touchpoint_ids,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
