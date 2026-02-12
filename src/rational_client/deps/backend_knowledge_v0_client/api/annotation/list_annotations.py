from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.annotation_dto_page import AnnotationDtoPage
from ...models.annotation_type import AnnotationType
from ...models.http_validation_problem_details import HttpValidationProblemDetails
from ...models.list_annotations_sorting_item import ListAnnotationsSortingItem
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    annotation_type: list[AnnotationType] | Unset = UNSET,
    container: str | Unset = UNSET,
    page: int | Unset = UNSET,
    title: str | Unset = UNSET,
    content: str | Unset = UNSET,
    note: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    labels: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListAnnotationsSortingItem] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_annotation_type: list[str] | Unset = UNSET
    if not isinstance(annotation_type, Unset):
        json_annotation_type = []
        for annotation_type_item_data in annotation_type:
            annotation_type_item = annotation_type_item_data.value
            json_annotation_type.append(annotation_type_item)

    params["annotationType"] = json_annotation_type

    params["container"] = container

    params["page"] = page

    params["title"] = title

    params["content"] = content

    params["note"] = note

    params["enabled"] = enabled

    json_labels: list[str] | Unset = UNSET
    if not isinstance(labels, Unset):
        json_labels = labels

    params["labels"] = json_labels

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
        "url": "/knowledge/v0/knowledge/{knowledge_id}/resources/{resource_id}/annotation".format(
            knowledge_id=quote(str(knowledge_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = AnnotationDtoPage.from_dict(response.json())

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
) -> Response[AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    annotation_type: list[AnnotationType] | Unset = UNSET,
    container: str | Unset = UNSET,
    page: int | Unset = UNSET,
    title: str | Unset = UNSET,
    content: str | Unset = UNSET,
    note: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    labels: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListAnnotationsSortingItem] | Unset = UNSET,
) -> Response[AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_type (list[AnnotationType] | Unset):
        container (str | Unset):
        page (int | Unset):
        title (str | Unset):
        content (str | Unset):
        note (str | Unset):
        enabled (bool | Unset):
        labels (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListAnnotationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        annotation_type=annotation_type,
        container=container,
        page=page,
        title=title,
        content=content,
        note=note,
        enabled=enabled,
        labels=labels,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    annotation_type: list[AnnotationType] | Unset = UNSET,
    container: str | Unset = UNSET,
    page: int | Unset = UNSET,
    title: str | Unset = UNSET,
    content: str | Unset = UNSET,
    note: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    labels: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListAnnotationsSortingItem] | Unset = UNSET,
) -> AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_type (list[AnnotationType] | Unset):
        container (str | Unset):
        page (int | Unset):
        title (str | Unset):
        content (str | Unset):
        note (str | Unset):
        enabled (bool | Unset):
        labels (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListAnnotationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails
    """

    return sync_detailed(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        client=client,
        annotation_type=annotation_type,
        container=container,
        page=page,
        title=title,
        content=content,
        note=note,
        enabled=enabled,
        labels=labels,
        offset=offset,
        limit=limit,
        sorting=sorting,
    ).parsed


async def asyncio_detailed(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    annotation_type: list[AnnotationType] | Unset = UNSET,
    container: str | Unset = UNSET,
    page: int | Unset = UNSET,
    title: str | Unset = UNSET,
    content: str | Unset = UNSET,
    note: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    labels: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListAnnotationsSortingItem] | Unset = UNSET,
) -> Response[AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails]:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_type (list[AnnotationType] | Unset):
        container (str | Unset):
        page (int | Unset):
        title (str | Unset):
        content (str | Unset):
        note (str | Unset):
        enabled (bool | Unset):
        labels (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListAnnotationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        knowledge_id=knowledge_id,
        resource_id=resource_id,
        annotation_type=annotation_type,
        container=container,
        page=page,
        title=title,
        content=content,
        note=note,
        enabled=enabled,
        labels=labels,
        offset=offset,
        limit=limit,
        sorting=sorting,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    knowledge_id: UUID,
    resource_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    annotation_type: list[AnnotationType] | Unset = UNSET,
    container: str | Unset = UNSET,
    page: int | Unset = UNSET,
    title: str | Unset = UNSET,
    content: str | Unset = UNSET,
    note: str | Unset = UNSET,
    enabled: bool | Unset = UNSET,
    labels: list[str] | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    sorting: list[ListAnnotationsSortingItem] | Unset = UNSET,
) -> AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails | None:
    """
    Args:
        knowledge_id (UUID):
        resource_id (UUID):
        annotation_type (list[AnnotationType] | Unset):
        container (str | Unset):
        page (int | Unset):
        title (str | Unset):
        content (str | Unset):
        note (str | Unset):
        enabled (bool | Unset):
        labels (list[str] | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        sorting (list[ListAnnotationsSortingItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnnotationDtoPage | HttpValidationProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            knowledge_id=knowledge_id,
            resource_id=resource_id,
            client=client,
            annotation_type=annotation_type,
            container=container,
            page=page,
            title=title,
            content=content,
            note=note,
            enabled=enabled,
            labels=labels,
            offset=offset,
            limit=limit,
            sorting=sorting,
        )
    ).parsed
