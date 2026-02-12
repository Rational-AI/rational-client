from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProxyRequest")


@_attrs_define
class CreateProxyRequest:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        connector_id (None | Unset | UUID):
        provider_base_url (None | str | Unset):
        track_usage (bool | None | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    connector_id: None | Unset | UUID = UNSET
    provider_base_url: None | str | Unset = UNSET
    track_usage: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        connector_id: None | str | Unset
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

        provider_base_url: None | str | Unset
        if isinstance(self.provider_base_url, Unset):
            provider_base_url = UNSET
        else:
            provider_base_url = self.provider_base_url

        track_usage: bool | None | Unset
        if isinstance(self.track_usage, Unset):
            track_usage = UNSET
        else:
            track_usage = self.track_usage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if provider_base_url is not UNSET:
            field_dict["providerBaseUrl"] = provider_base_url
        if track_usage is not UNSET:
            field_dict["trackUsage"] = track_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_connector_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connector_id_type_0 = UUID(data)

                return connector_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        connector_id = _parse_connector_id(d.pop("connectorId", UNSET))

        def _parse_provider_base_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_base_url = _parse_provider_base_url(d.pop("providerBaseUrl", UNSET))

        def _parse_track_usage(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        track_usage = _parse_track_usage(d.pop("trackUsage", UNSET))

        create_proxy_request = cls(
            name=name,
            description=description,
            connector_id=connector_id,
            provider_base_url=provider_base_url,
            track_usage=track_usage,
        )

        return create_proxy_request
