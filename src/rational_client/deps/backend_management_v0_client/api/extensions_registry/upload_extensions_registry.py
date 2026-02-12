from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extension_manifest_dto import ExtensionManifestDto
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...models.upload_extensions_registry_body import UploadExtensionsRegistryBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadExtensionsRegistryBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/management/v0/extensions-registry",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails | None:
    if response.status_code == 201:
        response_201 = ExtensionManifestDto.from_dict(response.json())

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
) -> Response[ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadExtensionsRegistryBody | Unset = UNSET,
) -> Response[ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        body (UploadExtensionsRegistryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails]
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
    client: AuthenticatedClient | Client,
    body: UploadExtensionsRegistryBody | Unset = UNSET,
) -> ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        body (UploadExtensionsRegistryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UploadExtensionsRegistryBody | Unset = UNSET,
) -> Response[ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        body (UploadExtensionsRegistryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UploadExtensionsRegistryBody | Unset = UNSET,
) -> ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        body (UploadExtensionsRegistryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtensionManifestDto | HttpValidationProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
