from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessingRuleConfig")


@_attrs_define
class ProcessingRuleConfig:
    """
    Attributes:
        id (UUID):
        options (Union[Unset, Any]):
    """

    id: UUID
    options: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        options = self.options

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        options = d.pop("options", UNSET)

        processing_rule_config = cls(
            id=id,
            options=options,
        )

        return processing_rule_config
