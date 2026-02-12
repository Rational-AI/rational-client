from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="ApiKeyDto")


@_attrs_define
class ApiKeyDto:
    """
    Attributes:
        id (UUID):
        name (str):
        masked_key (str):
        enabled (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    name: str
    masked_key: str
    enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        masked_key = self.masked_key

        enabled = self.enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "maskedKey": masked_key,
                "enabled": enabled,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        masked_key = d.pop("maskedKey")

        enabled = d.pop("enabled")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        api_key_dto = cls(
            id=id,
            name=name,
            masked_key=masked_key,
            enabled=enabled,
            created_at=created_at,
            updated_at=updated_at,
        )

        return api_key_dto
