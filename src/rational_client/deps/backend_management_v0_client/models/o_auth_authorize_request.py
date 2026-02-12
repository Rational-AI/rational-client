from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="OAuthAuthorizeRequest")


@_attrs_define
class OAuthAuthorizeRequest:
    """
    Attributes:
        connector_id (UUID):
        scopes (list[str]):
    """

    connector_id: UUID
    scopes: list[str]

    def to_dict(self) -> dict[str, Any]:
        connector_id = str(self.connector_id)

        scopes = self.scopes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "connectorId": connector_id,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_id = UUID(d.pop("connectorId"))

        scopes = cast(list[str], d.pop("scopes"))

        o_auth_authorize_request = cls(
            connector_id=connector_id,
            scopes=scopes,
        )

        return o_auth_authorize_request
