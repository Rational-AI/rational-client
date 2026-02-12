from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="ProcessingRuleDto")


@_attrs_define
class ProcessingRuleDto:
    """
    Attributes:
        id (UUID):
        name (str):
        code (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    name: str
    code: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        code = self.code

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "code": code,
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

        code = d.pop("code")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        processing_rule_dto = cls(
            id=id,
            name=name,
            code=code,
            created_at=created_at,
            updated_at=updated_at,
        )

        return processing_rule_dto
