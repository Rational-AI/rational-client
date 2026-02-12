from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="KnowledgeEdgeDto")


@_attrs_define
class KnowledgeEdgeDto:
    """
    Attributes:
        id (UUID):
        type_ (str):
        from_resource_id (UUID):
        to_resource_id (UUID):
    """

    id: UUID
    type_: str
    from_resource_id: UUID
    to_resource_id: UUID

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        type_ = self.type_

        from_resource_id = str(self.from_resource_id)

        to_resource_id = str(self.to_resource_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "fromResourceId": from_resource_id,
                "toResourceId": to_resource_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = d.pop("type")

        from_resource_id = UUID(d.pop("fromResourceId"))

        to_resource_id = UUID(d.pop("toResourceId"))

        knowledge_edge_dto = cls(
            id=id,
            type_=type_,
            from_resource_id=from_resource_id,
            to_resource_id=to_resource_id,
        )

        return knowledge_edge_dto
