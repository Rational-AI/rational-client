from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    knowledge_id: UUID,
    resource_id: UUID,
    annotation_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/knowledge/v0/knowledge/{knowledge_id}/resources/{resource_id}/annotation/{annotation_id}".format(
            knowledge_id=quote(str(knowledge_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
            annotation_id=quote(str(annotation_id), safe=""),
        ),
    }

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
    knowledge_id: UUID,
    resource_id: UUID,
    annotation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        annotation_id=annotation_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    resource_id: UUID,
    annotation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HttpValidationProblemDetails | ProblemDetails
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        annotation_id=annotation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    resource_id: UUID,
    annotation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        annotation_id=annotation_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    resource_id: UUID,
    annotation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HttpValidationProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            resource_id=resource_id,
            annotation_id=annotation_id,
            client=client,
        )
    ).parsed
