from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.rational_resource_dto import RationalResourceDto
from ...models.update_resource_request import UpdateResourceRequest
from ...types import Response


def _get_kwargs(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    body: UpdateResourceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/knowledge/v0/knowledge/{knowledge_id}/resource/{resource_id}".format(
            knowledge_id=quote(str(knowledge_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceDto | None:
    if response.status_code == 200:
        response_200 = RationalResourceDto.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateResourceRequest,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDto]:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        body (UpdateResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDto]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateResourceRequest,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceDto | None:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        body (UpdateResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceDto
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateResourceRequest,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDto]:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        body (UpdateResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceDto]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateResourceRequest,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceDto | None:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        body (UpdateResourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceDto
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            resource_id=resource_id,
            client=client,
            body=body,
        )
    ).parsed
