from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProcessingWorkflowRequest")


@_attrs_define
class UpdateProcessingWorkflowRequest:
    """
    Attributes:
        name (str | Unset):
        description (None | str | Unset):
        code (str | Unset):
        is_active (bool | Unset):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    code: str | Unset = UNSET
    is_active: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        code = self.code

        is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if code is not UNSET:
            field_dict["code"] = code
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        code = d.pop("code", UNSET)

        is_active = d.pop("isActive", UNSET)

        update_processing_workflow_request = cls(
            name=name,
            description=description,
            code=code,
            is_active=is_active,
        )

        return update_processing_workflow_request
