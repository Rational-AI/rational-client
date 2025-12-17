from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.processing_workflow_dto import ProcessingWorkflowDto
from ...models.update_processing_workflow_request import UpdateProcessingWorkflowRequest
from ...types import Response


def _get_kwargs(
    workflow_id: UUID,
    *,
    body: UpdateProcessingWorkflowRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/knowledge/v0/processingWorkflow/{workflow_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]:
    if response.status_code == 200:
        response_200 = ProcessingWorkflowDto.from_dict(response.json())

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
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateProcessingWorkflowRequest,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]:
    """
    Args:
        workflow_id (UUID):
        body (UpdateProcessingWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateProcessingWorkflowRequest,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]:
    """
    Args:
        workflow_id (UUID):
        body (UpdateProcessingWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateProcessingWorkflowRequest,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]:
    """
    Args:
        workflow_id (UUID):
        body (UpdateProcessingWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateProcessingWorkflowRequest,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]]:
    """
    Args:
        workflow_id (UUID):
        body (UpdateProcessingWorkflowRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, ProcessingWorkflowDto]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
