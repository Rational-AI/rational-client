from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncSourceOptions")


@_attrs_define
class SyncSourceOptions:
    """
    Attributes:
        wait_for_completion (bool | None | Unset):
    """

    wait_for_completion: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        wait_for_completion: bool | None | Unset
        if isinstance(self.wait_for_completion, Unset):
            wait_for_completion = UNSET
        else:
            wait_for_completion = self.wait_for_completion

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if wait_for_completion is not UNSET:
            field_dict["waitForCompletion"] = wait_for_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_wait_for_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        wait_for_completion = _parse_wait_for_completion(d.pop("waitForCompletion", UNSET))

        sync_source_options = cls(
            wait_for_completion=wait_for_completion,
        )

        return sync_source_options
