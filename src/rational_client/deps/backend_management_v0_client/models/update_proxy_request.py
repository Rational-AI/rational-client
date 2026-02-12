from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProxyRequest")


@_attrs_define
class UpdateProxyRequest:
    """
    Attributes:
        name (str | Unset):
        description (None | str | Unset):
        connector_id (None | Unset | UUID):
        provider_base_url (str | Unset):
        track_usage (bool | Unset):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    connector_id: None | Unset | UUID = UNSET
    provider_base_url: str | Unset = UNSET
    track_usage: bool | Unset = UNSET

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

        provider_base_url = self.provider_base_url

        track_usage = self.track_usage

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        name = d.pop("name", UNSET)

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

        provider_base_url = d.pop("providerBaseUrl", UNSET)

        track_usage = d.pop("trackUsage", UNSET)

        update_proxy_request = cls(
            name=name,
            description=description,
            connector_id=connector_id,
            provider_base_url=provider_base_url,
            track_usage=track_usage,
        )

        return update_proxy_request
