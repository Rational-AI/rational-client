from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.knowledge_category_dto import KnowledgeCategoryDto
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    knowledge_id: UUID,
    id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/knowledge/v0/knowledge/{knowledge_id}/categories/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = KnowledgeCategoryDto.from_dict(response.json())

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
) -> Response[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_id: UUID,
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeCategoryDto, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            id=id,
            client=client,
        )
    ).parsed
