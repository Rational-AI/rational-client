from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProcessingRuleRequest")


@_attrs_define
class UpdateProcessingRuleRequest:
    """
    Attributes:
        rule_name (Union[None, Unset, str]):
        rule_code (Union[None, Unset, str]):
    """

    rule_name: Union[None, Unset, str] = UNSET
    rule_code: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        rule_name: Union[None, Unset, str]
        if isinstance(self.rule_name, Unset):
            rule_name = UNSET
        else:
            rule_name = self.rule_name

        rule_code: Union[None, Unset, str]
        if isinstance(self.rule_code, Unset):
            rule_code = UNSET
        else:
            rule_code = self.rule_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if rule_code is not UNSET:
            field_dict["ruleCode"] = rule_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rule_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rule_name = _parse_rule_name(d.pop("ruleName", UNSET))

        def _parse_rule_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rule_code = _parse_rule_code(d.pop("ruleCode", UNSET))

        update_processing_rule_request = cls(
            rule_name=rule_name,
            rule_code=rule_code,
        )

        return update_processing_rule_request
