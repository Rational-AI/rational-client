from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderDto")


@_attrs_define
class ProviderDto:
    """
    Attributes:
        name (str):
        display_name (str):
        description (str):
        supported_models (list[str]):
        api_key_format (str):
        base_url (str):
        api_key_header_name (str):
        status (None | str | Unset):
        error_message (None | str | Unset):
    """

    name: str
    display_name: str
    description: str
    supported_models: list[str]
    api_key_format: str
    base_url: str
    api_key_header_name: str
    status: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        description = self.description

        supported_models = self.supported_models

        api_key_format = self.api_key_format

        base_url = self.base_url

        api_key_header_name = self.api_key_header_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "displayName": display_name,
                "description": description,
                "supportedModels": supported_models,
                "apiKeyFormat": api_key_format,
                "baseUrl": base_url,
                "apiKeyHeaderName": api_key_header_name,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        display_name = d.pop("displayName")

        description = d.pop("description")

        supported_models = cast(list[str], d.pop("supportedModels"))

        api_key_format = d.pop("apiKeyFormat")

        base_url = d.pop("baseUrl")

        api_key_header_name = d.pop("apiKeyHeaderName")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        provider_dto = cls(
            name=name,
            display_name=display_name,
            description=description,
            supported_models=supported_models,
            api_key_format=api_key_format,
            base_url=base_url,
            api_key_header_name=api_key_header_name,
            status=status,
            error_message=error_message,
        )

        return provider_dto
