from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateResourceRelationRequest")


@_attrs_define
class CreateResourceRelationRequest:
    """
    Attributes:
        type_ (str):
        from_resource_id (UUID):
        to_resource_id (UUID):
    """

    type_: str
    from_resource_id: UUID
    to_resource_id: UUID

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        from_resource_id = str(self.from_resource_id)

        to_resource_id = str(self.to_resource_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "fromResourceId": from_resource_id,
                "toResourceId": to_resource_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        from_resource_id = UUID(d.pop("fromResourceId"))

        to_resource_id = UUID(d.pop("toResourceId"))

        create_resource_relation_request = cls(
            type_=type_,
            from_resource_id=from_resource_id,
            to_resource_id=to_resource_id,
        )

        return create_resource_relation_request
