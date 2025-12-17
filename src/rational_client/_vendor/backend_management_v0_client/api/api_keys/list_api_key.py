from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_dto_page import ApiKeyDtoPage
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_api_key_sorting_item import ListApiKeySortingItem
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[ListApiKeySortingItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_sorting: Union[Unset, list[str]] = UNSET
    if not isinstance(sorting, Unset):
        json_sorting = []
        for sorting_item_data in sorting:
            sorting_item = sorting_item_data.value
            json_sorting.append(sorting_item)

    params["sorting"] = json_sorting

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/management/v0/api-keys",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = ApiKeyDtoPage.from_dict(response.json())

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
) -> Response[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[ListApiKeySortingItem]] = UNSET,
) -> Response[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[ListApiKeySortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[ListApiKeySortingItem]] = UNSET,
) -> Optional[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[ListApiKeySortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[ListApiKeySortingItem]] = UNSET,
) -> Response[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[ListApiKeySortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 20,
    sorting: Union[Unset, list[ListApiKeySortingItem]] = UNSET,
) -> Optional[Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]]:
    """
    Args:
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 20.
        sorting (Union[Unset, list[ListApiKeySortingItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyDtoPage, HttpValidationProblemDetails, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
