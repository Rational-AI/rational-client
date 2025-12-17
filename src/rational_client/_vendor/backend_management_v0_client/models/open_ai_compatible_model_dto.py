import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_purpose import ModelPurpose
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenAICompatibleModelDto")


@_attrs_define
class OpenAICompatibleModelDto:
    """
    Attributes:
        id (str):
        owned_by (Union[None, Unset, str]):
        created (Union[None, Unset, int]):
        purpose (Union[Unset, ModelPurpose]):
        created_at (Union[None, Unset, datetime.datetime]):
    """

    id: str
    owned_by: Union[None, Unset, str] = UNSET
    created: Union[None, Unset, int] = UNSET
    purpose: Union[Unset, ModelPurpose] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        owned_by: Union[None, Unset, str]
        if isinstance(self.owned_by, Unset):
            owned_by = UNSET
        else:
            owned_by = self.owned_by

        created: Union[None, Unset, int]
        if isinstance(self.created, Unset):
            created = UNSET
        else:
            created = self.created

        purpose: Union[Unset, str] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if owned_by is not UNSET:
            field_dict["ownedBy"] = owned_by
        if created is not UNSET:
            field_dict["created"] = created
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_owned_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        owned_by = _parse_owned_by(d.pop("ownedBy", UNSET))

        def _parse_created(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        created = _parse_created(d.pop("created", UNSET))

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, ModelPurpose]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = ModelPurpose(_purpose)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        open_ai_compatible_model_dto = cls(
            id=id,
            owned_by=owned_by,
            created=created,
            purpose=purpose,
            created_at=created_at,
        )

        open_ai_compatible_model_dto.additional_properties = d
        return open_ai_compatible_model_dto

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
