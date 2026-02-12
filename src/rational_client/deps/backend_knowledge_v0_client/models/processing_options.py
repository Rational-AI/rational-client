from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessingOptions")


@_attrs_define
class ProcessingOptions:
    """
    Attributes:
        evaluate_rules (bool | None | Unset):
        evaluate_workflow (bool | None | Unset):
        wait_for_completion (bool | None | Unset):
    """

    evaluate_rules: bool | None | Unset = UNSET
    evaluate_workflow: bool | None | Unset = UNSET
    wait_for_completion: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        evaluate_rules: bool | None | Unset
        if isinstance(self.evaluate_rules, Unset):
            evaluate_rules = UNSET
        else:
            evaluate_rules = self.evaluate_rules

        evaluate_workflow: bool | None | Unset
        if isinstance(self.evaluate_workflow, Unset):
            evaluate_workflow = UNSET
        else:
            evaluate_workflow = self.evaluate_workflow

        wait_for_completion: bool | None | Unset
        if isinstance(self.wait_for_completion, Unset):
            wait_for_completion = UNSET
        else:
            wait_for_completion = self.wait_for_completion

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if evaluate_rules is not UNSET:
            field_dict["evaluateRules"] = evaluate_rules
        if evaluate_workflow is not UNSET:
            field_dict["evaluateWorkflow"] = evaluate_workflow
        if wait_for_completion is not UNSET:
            field_dict["waitForCompletion"] = wait_for_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_evaluate_rules(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        evaluate_rules = _parse_evaluate_rules(d.pop("evaluateRules", UNSET))

        def _parse_evaluate_workflow(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        evaluate_workflow = _parse_evaluate_workflow(d.pop("evaluateWorkflow", UNSET))

        def _parse_wait_for_completion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        wait_for_completion = _parse_wait_for_completion(d.pop("waitForCompletion", UNSET))

        processing_options = cls(
            evaluate_rules=evaluate_rules,
            evaluate_workflow=evaluate_workflow,
            wait_for_completion=wait_for_completion,
        )

        return processing_options
