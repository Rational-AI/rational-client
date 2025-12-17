from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    deployment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/management/v0/models/{deployment_id}/cancel",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HttpValidationProblemDetails, ProblemDetails]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
) -> Response[Union[Any, HttpValidationProblemDetails, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HttpValidationProblemDetails, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        deployment_id=deployment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HttpValidationProblemDetails, ProblemDetails]
    """

    return sync_detailed(
        deployment_id=deployment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HttpValidationProblemDetails, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        deployment_id=deployment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        deployment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HttpValidationProblemDetails, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            deployment_id=deployment_id,
            client=client,
        )
    ).parsed
