from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.setting_visibility import SettingVisibility

T = TypeVar("T", bound="SettingDto")


@_attrs_define
class SettingDto:
    """
    Attributes:
        id (UUID):
        key (str):
        value (Any):
        visibility (SettingVisibility):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    key: str
    value: Any
    visibility: SettingVisibility
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        key = self.key

        value = self.value

        visibility = self.visibility.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "key": key,
                "value": value,
                "visibility": visibility,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        key = d.pop("key")

        value = d.pop("value")

        visibility = SettingVisibility(d.pop("visibility"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        setting_dto = cls(
            id=id,
            key=key,
            value=value,
            visibility=visibility,
            created_at=created_at,
            updated_at=updated_at,
        )

        return setting_dto
