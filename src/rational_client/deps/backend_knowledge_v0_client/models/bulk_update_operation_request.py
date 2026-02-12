from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_request import UpdateRequest


T = TypeVar("T", bound="BulkUpdateOperationRequest")


@_attrs_define
class BulkUpdateOperationRequest:
    """
    Attributes:
        update (UpdateRequest):
        ids (list[UUID] | None | Unset):
    """

    update: UpdateRequest
    ids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update = self.update.to_dict()

        ids: list[str] | None | Unset
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = []
            for ids_type_0_item_data in self.ids:
                ids_type_0_item = str(ids_type_0_item_data)
                ids.append(ids_type_0_item)

        else:
            ids = self.ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "update": update,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_request import UpdateRequest

        d = dict(src_dict)
        update = UpdateRequest.from_dict(d.pop("update"))

        def _parse_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = []
                _ids_type_0 = data
                for ids_type_0_item_data in _ids_type_0:
                    ids_type_0_item = UUID(ids_type_0_item_data)

                    ids_type_0.append(ids_type_0_item)

                return ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        ids = _parse_ids(d.pop("ids", UNSET))

        bulk_update_operation_request = cls(
            update=update,
            ids=ids,
        )

        return bulk_update_operation_request
