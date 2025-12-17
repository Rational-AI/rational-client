from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extension_dto import ExtensionDto
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.install_extension_request import InstallExtensionRequest
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: InstallExtensionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/management/v0/extensions-registry/{id}/install",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = ExtensionDto.from_dict(response.json())

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
) -> Response[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallExtensionRequest,
) -> Response[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        id (str):
        body (InstallExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallExtensionRequest,
) -> Optional[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        id (str):
        body (InstallExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallExtensionRequest,
) -> Response[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        id (str):
        body (InstallExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: InstallExtensionRequest,
) -> Optional[Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        id (str):
        body (InstallExtensionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ExtensionDto, HttpValidationProblemDetails, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
