from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProcessingWorkflowRequest")


@_attrs_define
class CreateProcessingWorkflowRequest:
    """
    Attributes:
        name (str):
        code (str):
        description (None | str | Unset):
        is_active (bool | None | Unset):
    """

    name: str
    code: str
    description: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "code": code,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        code = d.pop("code")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))

        create_processing_workflow_request = cls(
            name=name,
            code=code,
            description=description,
            is_active=is_active,
        )

        return create_processing_workflow_request
