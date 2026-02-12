from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_resource_relation_request import CreateResourceRelationRequest
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.rational_resource_relation_dto import RationalResourceRelationDto
from ...types import Response


def _get_kwargs(
    knowledge_id: UUID,
    *,
    body: CreateResourceRelationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/knowledge/v0/knowledge/{knowledge_id}/resource-relations".format(
            knowledge_id=quote(str(knowledge_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto | None:
    if response.status_code == 201:
        response_201 = RationalResourceRelationDto.from_dict(response.json())

        return response_201

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
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto]:
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
    body: CreateResourceRelationRequest,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto]:
    """
    Args:
        knowledge_id (UUID):
        body (CreateResourceRelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateResourceRelationRequest,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto | None:
    """
    Args:
        knowledge_id (UUID):
        body (CreateResourceRelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateResourceRelationRequest,
) -> Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto]:
    """
    Args:
        knowledge_id (UUID):
        body (CreateResourceRelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateResourceRelationRequest,
) -> HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto | None:
    """
    Args:
        knowledge_id (UUID):
        body (CreateResourceRelationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | ProblemDetails | RationalResourceRelationDto
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            client=client,
            body=body,
        )
    ).parsed
