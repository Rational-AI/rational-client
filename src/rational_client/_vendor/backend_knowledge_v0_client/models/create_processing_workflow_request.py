from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProcessingWorkflowRequest")


@_attrs_define
class CreateProcessingWorkflowRequest:
    """
    Attributes:
        name (str):
        code (str):
        description (Union[None, Unset, str]):
        is_active (Union[None, Unset, bool]):
    """

    name: str
    code: str
    description: Union[None, Unset, str] = UNSET
    is_active: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        code = self.code

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active: Union[None, Unset, bool]
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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_active = _parse_is_active(d.pop("isActive", UNSET))

        create_processing_workflow_request = cls(
            name=name,
            code=code,
            description=description,
            is_active=is_active,
        )

        return create_processing_workflow_request
