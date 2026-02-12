from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.synced_resource_dto import SyncedResourceDto


T = TypeVar("T", bound="RationalResourceDto")


@_attrs_define
class RationalResourceDto:
    """
    Attributes:
        id (UUID):
        tags (list[str]):
        knowledge_id (UUID):
        related_resources_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        category (None | str | Unset):
        notes (None | str | Unset):
        synced_resource (SyncedResourceDto | Unset):
    """

    id: UUID
    tags: list[str]
    knowledge_id: UUID
    related_resources_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    synced_resource: SyncedResourceDto | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        tags = self.tags

        knowledge_id = str(self.knowledge_id)

        related_resources_count = self.related_resources_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        synced_resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.synced_resource, Unset):
            synced_resource = self.synced_resource.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "tags": tags,
                "knowledgeId": knowledge_id,
                "relatedResourcesCount": related_resources_count,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if notes is not UNSET:
            field_dict["notes"] = notes
        if synced_resource is not UNSET:
            field_dict["syncedResource"] = synced_resource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.synced_resource_dto import SyncedResourceDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        tags = cast(list[str], d.pop("tags"))

        knowledge_id = UUID(d.pop("knowledgeId"))

        related_resources_count = d.pop("relatedResourcesCount")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _synced_resource = d.pop("syncedResource", UNSET)
        synced_resource: SyncedResourceDto | Unset
        if isinstance(_synced_resource, Unset):
            synced_resource = UNSET
        else:
            synced_resource = SyncedResourceDto.from_dict(_synced_resource)

        rational_resource_dto = cls(
            id=id,
            tags=tags,
            knowledge_id=knowledge_id,
            related_resources_count=related_resources_count,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            category=category,
            notes=notes,
            synced_resource=synced_resource,
        )

        return rational_resource_dto
