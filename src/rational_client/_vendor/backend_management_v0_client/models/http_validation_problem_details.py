from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_validation_problem_details_errors import HttpValidationProblemDetailsErrors


T = TypeVar("T", bound="HttpValidationProblemDetails")


@_attrs_define
class HttpValidationProblemDetails:
    """
    Attributes:
        errors (HttpValidationProblemDetailsErrors):
        type_ (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        status (Union[None, Unset, int]):
        detail (Union[None, Unset, str]):
        instance (Union[None, Unset, str]):
    """

    errors: "HttpValidationProblemDetailsErrors"
    type_: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, int] = UNSET
    detail: Union[None, Unset, str] = UNSET
    instance: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors.to_dict()

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: Union[None, Unset, int]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        detail: Union[None, Unset, str]
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: Union[None, Unset, str]
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_validation_problem_details_errors import HttpValidationProblemDetailsErrors

        d = dict(src_dict)
        errors = HttpValidationProblemDetailsErrors.from_dict(d.pop("errors"))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_detail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_instance(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance = _parse_instance(d.pop("instance", UNSET))

        http_validation_problem_details = cls(
            errors=errors,
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
        )

        http_validation_problem_details.additional_properties = d
        return http_validation_problem_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
