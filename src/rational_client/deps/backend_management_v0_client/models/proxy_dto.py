from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.proxy_provider import ProxyProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProxyDto")


@_attrs_define
class ProxyDto:
    """
    Attributes:
        id (UUID):
        name (str):
        provider (ProxyProvider):
        provider_base_url (str):
        track_usage (bool):
        proxy_api_key_suffix (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        rotated_at (datetime.datetime):
        description (None | str | Unset):
        connector_id (None | Unset | UUID):
        proxy_api_key (None | str | Unset):
    """

    id: UUID
    name: str
    provider: ProxyProvider
    provider_base_url: str
    track_usage: bool
    proxy_api_key_suffix: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    rotated_at: datetime.datetime
    description: None | str | Unset = UNSET
    connector_id: None | Unset | UUID = UNSET
    proxy_api_key: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        provider = self.provider.value

        provider_base_url = self.provider_base_url

        track_usage = self.track_usage

        proxy_api_key_suffix = self.proxy_api_key_suffix

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        rotated_at = self.rotated_at.isoformat()

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

        proxy_api_key: None | str | Unset
        if isinstance(self.proxy_api_key, Unset):
            proxy_api_key = UNSET
        else:
            proxy_api_key = self.proxy_api_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "provider": provider,
                "providerBaseUrl": provider_base_url,
                "trackUsage": track_usage,
                "proxyApiKeySuffix": proxy_api_key_suffix,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "rotatedAt": rotated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if proxy_api_key is not UNSET:
            field_dict["proxyApiKey"] = proxy_api_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        provider = ProxyProvider(d.pop("provider"))

        provider_base_url = d.pop("providerBaseUrl")

        track_usage = d.pop("trackUsage")

        proxy_api_key_suffix = d.pop("proxyApiKeySuffix")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        rotated_at = isoparse(d.pop("rotatedAt"))

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

        def _parse_proxy_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_api_key = _parse_proxy_api_key(d.pop("proxyApiKey", UNSET))

        proxy_dto = cls(
            id=id,
            name=name,
            provider=provider,
            provider_base_url=provider_base_url,
            track_usage=track_usage,
            proxy_api_key_suffix=proxy_api_key_suffix,
            created_at=created_at,
            updated_at=updated_at,
            rotated_at=rotated_at,
            description=description,
            connector_id=connector_id,
            proxy_api_key=proxy_api_key,
        )

        return proxy_dto
