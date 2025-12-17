from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extension_manifest_dto import ExtensionManifestDto
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
    exclude_ids: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    json_exclude_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_ids, Unset):
        json_exclude_ids = exclude_ids

    params["excludeIds"] = json_exclude_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/management/v0/extensions-registry",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, list["ExtensionManifestDto"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExtensionManifestDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, list["ExtensionManifestDto"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    exclude_ids: Union[Unset, list[str]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, list["ExtensionManifestDto"]]]:
    """
    Args:
        query (Union[Unset, str]):
        exclude_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, list['ExtensionManifestDto']]]
    """

    kwargs = _get_kwargs(
        query=query,
        exclude_ids=exclude_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    exclude_ids: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, list["ExtensionManifestDto"]]]:
    """
    Args:
        query (Union[Unset, str]):
        exclude_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, list['ExtensionManifestDto']]
    """

    return sync_detailed(
        client=client,
        query=query,
        exclude_ids=exclude_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    exclude_ids: Union[Unset, list[str]] = UNSET,
) -> Response[Union[HttpValidationProblemDetails, ProblemDetails, list["ExtensionManifestDto"]]]:
    """
    Args:
        query (Union[Unset, str]):
        exclude_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HttpValidationProblemDetails, ProblemDetails, list['ExtensionManifestDto']]]
    """

    kwargs = _get_kwargs(
        query=query,
        exclude_ids=exclude_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    exclude_ids: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[HttpValidationProblemDetails, ProblemDetails, list["ExtensionManifestDto"]]]:
    """
    Args:
        query (Union[Unset, str]):
        exclude_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HttpValidationProblemDetails, ProblemDetails, list['ExtensionManifestDto']]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            exclude_ids=exclude_ids,
        )
    ).parsed
