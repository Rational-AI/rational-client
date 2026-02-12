from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_mcp_server_configuration_sorting_item import ListMcpServerConfigurationSortingItem
from ...models.mcp_server_configuration_dto_page import McpServerConfigurationDtoPage
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    mcp_server_ids: list[UUID] | Unset = UNSET,
    is_default: bool | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListMcpServerConfigurationSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_mcp_server_ids: list[str] | Unset = UNSET
    if not isinstance(mcp_server_ids, Unset):
        json_mcp_server_ids = []
        for mcp_server_ids_item_data in mcp_server_ids:
            mcp_server_ids_item = str(mcp_server_ids_item_data)
            json_mcp_server_ids.append(mcp_server_ids_item)

    params["mcpServerIds"] = json_mcp_server_ids

    params["isDefault"] = is_default

    params["offset"] = offset

    params["limit"] = limit

    json_sorting: list[str] | Unset = UNSET
    if not isinstance(sorting, Unset):
        json_sorting = []
        for sorting_item_data in sorting:
            sorting_item = sorting_item_data.value
            json_sorting.append(sorting_item)

    params["sorting"] = json_sorting

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/management/v0/mcpServersConfigurations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = McpServerConfigurationDtoPage.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    mcp_server_ids: list[UUID] | Unset = UNSET,
    is_default: bool | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListMcpServerConfigurationSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails]:
    """
    Args:
        query (str | Unset):
        mcp_server_ids (list[UUID] | Unset):
        is_default (bool | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListMcpServerConfigurationSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails]
    """

    kwargs = _get_kwargs(
        query=query,
        mcp_server_ids=mcp_server_ids,
        is_default=is_default,
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
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    mcp_server_ids: list[UUID] | Unset = UNSET,
    is_default: bool | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListMcpServerConfigurationSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails | None:
    """
    Args:
        query (str | Unset):
        mcp_server_ids (list[UUID] | Unset):
        is_default (bool | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListMcpServerConfigurationSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails
    """

    return sync_detailed(
        client=client,
        query=query,
        mcp_server_ids=mcp_server_ids,
        is_default=is_default,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    mcp_server_ids: list[UUID] | Unset = UNSET,
    is_default: bool | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListMcpServerConfigurationSortingItem] | Unset = UNSET,
) -> Response[HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails]:
    """
    Args:
        query (str | Unset):
        mcp_server_ids (list[UUID] | Unset):
        is_default (bool | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListMcpServerConfigurationSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails]
    """

    kwargs = _get_kwargs(
        query=query,
        mcp_server_ids=mcp_server_ids,
        is_default=is_default,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str | Unset = UNSET,
    mcp_server_ids: list[UUID] | Unset = UNSET,
    is_default: bool | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListMcpServerConfigurationSortingItem] | Unset = UNSET,
) -> HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails | None:
    """
    Args:
        query (str | Unset):
        mcp_server_ids (list[UUID] | Unset):
        is_default (bool | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListMcpServerConfigurationSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HttpValidationProblemDetails | McpServerConfigurationDtoPage | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            mcp_server_ids=mcp_server_ids,
            is_default=is_default,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
