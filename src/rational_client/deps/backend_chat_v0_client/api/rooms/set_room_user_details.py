from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.set_room_user_details_request import SetRoomUserDetailsRequest
from ...types import Response


def _get_kwargs(
    room_id: UUID,
    *,
    body: SetRoomUserDetailsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/chat/v0/rooms/{room_id}/user-details".format(
            room_id=quote(str(room_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HttpValidationProblemDetails | ProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HttpValidationProblemDetails | ProblemDetails]:
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
    body: SetRoomUserDetailsRequest,
) -> Response[Any | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        room_id (UUID):
        body (SetRoomUserDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetRoomUserDetailsRequest,
) -> Any | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        room_id (UUID):
        body (SetRoomUserDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HttpValidationProblemDetails | ProblemDetails
    """

    return sync_detailed(
        room_id=room_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetRoomUserDetailsRequest,
) -> Response[Any | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        room_id (UUID):
        body (SetRoomUserDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SetRoomUserDetailsRequest,
) -> Any | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        room_id (UUID):
        body (SetRoomUserDetailsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HttpValidationProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            client=client,
            body=body,
        )
    ).parsed
