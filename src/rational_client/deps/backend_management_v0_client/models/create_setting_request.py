from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.setting_visibility import SettingVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSettingRequest")


@_attrs_define
class CreateSettingRequest:
    """
    Attributes:
        key (str):
        value (Any):
        visibility (SettingVisibility | Unset):
        overwrite (bool | None | Unset):
    """

    key: str
    value: Any
    visibility: SettingVisibility | Unset = UNSET
    overwrite: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        overwrite: bool | None | Unset
        if isinstance(self.overwrite, Unset):
            overwrite = UNSET
        else:
            overwrite = self.overwrite

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        _visibility = d.pop("visibility", UNSET)
        visibility: SettingVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = SettingVisibility(_visibility)

        def _parse_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite = _parse_overwrite(d.pop("overwrite", UNSET))

        create_setting_request = cls(
            key=key,
            value=value,
            visibility=visibility,
            overwrite=overwrite,
        )

        return create_setting_request
