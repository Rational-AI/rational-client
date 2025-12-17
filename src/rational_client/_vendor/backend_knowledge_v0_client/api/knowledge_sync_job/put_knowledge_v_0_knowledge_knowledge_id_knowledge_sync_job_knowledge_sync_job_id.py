from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.knowledge_sync_job_dto import KnowledgeSyncJobDto
from ...models.problem_details import ProblemDetails
from ...models.update_knowledge_sync_job_request import UpdateKnowledgeSyncJobRequest
from ...types import Response


def _get_kwargs(
    knowledge_id: UUID,
    knowledge_sync_job_id: UUID,
    *,
    body: UpdateKnowledgeSyncJobRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/knowledge/v0/knowledge/{knowledge_id}/knowledgeSyncJob/{knowledge_sync_job_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = KnowledgeSyncJobDto.from_dict(response.json())

        return response_200
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
) -> Response[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_id: UUID,
    knowledge_sync_job_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateKnowledgeSyncJobRequest,
) -> Response[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        knowledge_sync_job_id (UUID):
        body (UpdateKnowledgeSyncJobRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        knowledge_sync_job_id=knowledge_sync_job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    knowledge_sync_job_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateKnowledgeSyncJobRequest,
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        knowledge_sync_job_id (UUID):
        body (UpdateKnowledgeSyncJobRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        knowledge_sync_job_id=knowledge_sync_job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    knowledge_sync_job_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateKnowledgeSyncJobRequest,
) -> Response[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        knowledge_sync_job_id (UUID):
        body (UpdateKnowledgeSyncJobRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        knowledge_sync_job_id=knowledge_sync_job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    knowledge_sync_job_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateKnowledgeSyncJobRequest,
) -> Optional[Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]]:
    """
    Args:
        knowledge_id (UUID):
        knowledge_sync_job_id (UUID):
        body (UpdateKnowledgeSyncJobRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, KnowledgeSyncJobDto, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            knowledge_sync_job_id=knowledge_sync_job_id,
            client=client,
            body=body,
        )
    ).parsed
