from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.model_purpose import ModelPurpose
from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSupportedModelDto")


@_attrs_define
class UpdateSupportedModelDto:
    """
    Attributes:
        name (str):
        type_ (ModelType):
        purpose (ModelPurpose):
        hugging_face_id (Union[None, Unset, str]):
        architecture (Union[None, Unset, str]):
        publisher (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
    """

    name: str
    type_: ModelType
    purpose: ModelPurpose
    hugging_face_id: Union[None, Unset, str] = UNSET
    architecture: Union[None, Unset, str] = UNSET
    publisher: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        purpose = self.purpose.value

        hugging_face_id: Union[None, Unset, str]
        if isinstance(self.hugging_face_id, Unset):
            hugging_face_id = UNSET
        else:
            hugging_face_id = self.hugging_face_id

        architecture: Union[None, Unset, str]
        if isinstance(self.architecture, Unset):
            architecture = UNSET
        else:
            architecture = self.architecture

        publisher: Union[None, Unset, str]
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        description: Union[None, Unset, str]
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

        def _parse_hugging_face_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hugging_face_id = _parse_hugging_face_id(d.pop("huggingFaceId", UNSET))

        def _parse_architecture(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        architecture = _parse_architecture(d.pop("architecture", UNSET))

        def _parse_publisher(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        update_supported_model_dto = cls(
            name=name,
            type_=type_,
            purpose=purpose,
            hugging_face_id=hugging_face_id,
            architecture=architecture,
            publisher=publisher,
            description=description,
        )

        return update_supported_model_dto
