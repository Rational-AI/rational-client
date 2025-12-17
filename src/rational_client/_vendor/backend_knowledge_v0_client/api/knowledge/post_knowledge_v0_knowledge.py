from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_knowledge_request import CreateKnowledgeRequest
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.knowledge_dto import KnowledgeDto
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: CreateKnowledgeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/knowledge/v0/knowledge",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]:
    if response.status_code == 201:
        response_201 = KnowledgeDto.from_dict(response.json())

        return response_201
    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409
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
) -> Response[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateKnowledgeRequest,
) -> Response[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]:
    """
    Args:
        body (CreateKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateKnowledgeRequest,
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]:
    """
    Args:
        body (CreateKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateKnowledgeRequest,
) -> Response[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]:
    """
    Args:
        body (CreateKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateKnowledgeRequest,
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]]:
    """
    Args:
        body (CreateKnowledgeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeDto, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
