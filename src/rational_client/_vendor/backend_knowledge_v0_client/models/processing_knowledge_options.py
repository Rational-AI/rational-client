from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessingKnowledgeOptions")


@_attrs_define
class ProcessingKnowledgeOptions:
    """
    Attributes:
        force_process_all (Union[None, Unset, bool]):
        wait_for_completion (Union[None, Unset, bool]):
    """

    force_process_all: Union[None, Unset, bool] = UNSET
    wait_for_completion: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        force_process_all: Union[None, Unset, bool]
        if isinstance(self.force_process_all, Unset):
            force_process_all = UNSET
        else:
            force_process_all = self.force_process_all

        wait_for_completion: Union[None, Unset, bool]
        if isinstance(self.wait_for_completion, Unset):
            wait_for_completion = UNSET
        else:
            wait_for_completion = self.wait_for_completion

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if force_process_all is not UNSET:
            field_dict["forceProcessAll"] = force_process_all
        if wait_for_completion is not UNSET:
            field_dict["waitForCompletion"] = wait_for_completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_force_process_all(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        force_process_all = _parse_force_process_all(d.pop("forceProcessAll", UNSET))

        def _parse_wait_for_completion(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        wait_for_completion = _parse_wait_for_completion(d.pop("waitForCompletion", UNSET))

        processing_knowledge_options = cls(
            force_process_all=force_process_all,
            wait_for_completion=wait_for_completion,
        )

        return processing_knowledge_options
