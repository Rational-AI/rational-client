from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BulkOperationResponse")


@_attrs_define
class BulkOperationResponse:
    """
    Attributes:
        total (int):
        success_count (int):
        failed_count (int):
    """

    total: int
    success_count: int
    failed_count: int

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        success_count = self.success_count

        failed_count = self.failed_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
                "successCount": success_count,
                "failedCount": failed_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        success_count = d.pop("successCount")

        failed_count = d.pop("failedCount")

        bulk_operation_response = cls(
            total=total,
            success_count=success_count,
            failed_count=failed_count,
        )

        return bulk_operation_response
