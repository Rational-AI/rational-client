import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

T = TypeVar("T", bound="KnowledgeCategoryDto")


@_attrs_define
class KnowledgeCategoryDto:
    """
    Attributes:
        id (UUID):
        name (str):
        color (str):
        knowledge_id (UUID):
        is_default (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    name: str
    color: str
    knowledge_id: UUID
    is_default: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        color = self.color

        knowledge_id = str(self.knowledge_id)

        is_default = self.is_default

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "color": color,
                "knowledgeId": knowledge_id,
                "isDefault": is_default,
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

        color = d.pop("color")

        knowledge_id = UUID(d.pop("knowledgeId"))

        is_default = d.pop("isDefault")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        knowledge_category_dto = cls(
            id=id,
            name=name,
            color=color,
            knowledge_id=knowledge_id,
            is_default=is_default,
            created_at=created_at,
            updated_at=updated_at,
        )

        return knowledge_category_dto
