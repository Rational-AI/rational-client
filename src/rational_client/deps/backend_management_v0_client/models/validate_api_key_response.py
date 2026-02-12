from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateApiKeyResponse")


@_attrs_define
class ValidateApiKeyResponse:
    """
    Attributes:
        is_valid (bool):
        error_message (None | str | Unset):
    """

    is_valid: bool
    error_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isValid": is_valid,
            }
        )
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_valid = d.pop("isValid")

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        validate_api_key_response = cls(
            is_valid=is_valid,
            error_message=error_message,
        )

        return validate_api_key_response
