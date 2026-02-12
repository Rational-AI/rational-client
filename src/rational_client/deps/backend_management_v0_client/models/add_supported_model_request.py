from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.model_purpose import ModelPurpose
from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSupportedModelRequest")


@_attrs_define
class AddSupportedModelRequest:
    """
    Attributes:
        name (str):
        type_ (ModelType):
        purpose (ModelPurpose):
        hugging_face_id (None | str | Unset):
        architecture (None | str | Unset):
        publisher (None | str | Unset):
        description (None | str | Unset):
    """

    name: str
    type_: ModelType
    purpose: ModelPurpose
    hugging_face_id: None | str | Unset = UNSET
    architecture: None | str | Unset = UNSET
    publisher: None | str | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        purpose = self.purpose.value

        hugging_face_id: None | str | Unset
        if isinstance(self.hugging_face_id, Unset):
            hugging_face_id = UNSET
        else:
            hugging_face_id = self.hugging_face_id

        architecture: None | str | Unset
        if isinstance(self.architecture, Unset):
            architecture = UNSET
        else:
            architecture = self.architecture

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "purpose": purpose,
            }
        )
        if hugging_face_id is not UNSET:
            field_dict["huggingFaceId"] = hugging_face_id
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ModelType(d.pop("type"))

        purpose = ModelPurpose(d.pop("purpose"))

        def _parse_hugging_face_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hugging_face_id = _parse_hugging_face_id(d.pop("huggingFaceId", UNSET))

        def _parse_architecture(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        architecture = _parse_architecture(d.pop("architecture", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        add_supported_model_request = cls(
            name=name,
            type_=type_,
            purpose=purpose,
            hugging_face_id=hugging_face_id,
            architecture=architecture,
            publisher=publisher,
            description=description,
        )

        return add_supported_model_request
