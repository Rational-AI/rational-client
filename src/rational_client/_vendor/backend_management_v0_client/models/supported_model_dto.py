import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.model_purpose import ModelPurpose
from ..models.model_type import ModelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportedModelDto")


@_attrs_define
class SupportedModelDto:
    """
    Attributes:
        id (UUID):
        name (str):
        type_ (ModelType):
        purpose (ModelPurpose):
        model_created_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        model_card (Union[None, Unset, str]):
        hugging_face_id (Union[None, Unset, str]):
        architecture (Union[None, Unset, str]):
        number_of_params (Union[None, Unset, int]):
        publisher (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    type_: ModelType
    purpose: ModelPurpose
    model_created_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    model_card: Union[None, Unset, str] = UNSET
    hugging_face_id: Union[None, Unset, str] = UNSET
    architecture: Union[None, Unset, str] = UNSET
    number_of_params: Union[None, Unset, int] = UNSET
    publisher: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        purpose = self.purpose.value

        model_created_at = self.model_created_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        model_card: Union[None, Unset, str]
        if isinstance(self.model_card, Unset):
            model_card = UNSET
        else:
            model_card = self.model_card

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

        number_of_params: Union[None, Unset, int]
        if isinstance(self.number_of_params, Unset):
            number_of_params = UNSET
        else:
            number_of_params = self.number_of_params

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
                "id": id,
                "name": name,
                "type": type_,
                "purpose": purpose,
                "modelCreatedAt": model_created_at,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if model_card is not UNSET:
            field_dict["modelCard"] = model_card
        if hugging_face_id is not UNSET:
            field_dict["huggingFaceId"] = hugging_face_id
        if architecture is not UNSET:
            field_dict["architecture"] = architecture
        if number_of_params is not UNSET:
            field_dict["numberOfParams"] = number_of_params
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = ModelType(d.pop("type"))

        purpose = ModelPurpose(d.pop("purpose"))

        model_created_at = isoparse(d.pop("modelCreatedAt"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_model_card(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model_card = _parse_model_card(d.pop("modelCard", UNSET))

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

        def _parse_number_of_params(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_params = _parse_number_of_params(d.pop("numberOfParams", UNSET))

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

        supported_model_dto = cls(
            id=id,
            name=name,
            type_=type_,
            purpose=purpose,
            model_created_at=model_created_at,
            created_at=created_at,
            updated_at=updated_at,
            model_card=model_card,
            hugging_face_id=hugging_face_id,
            architecture=architecture,
            number_of_params=number_of_params,
            publisher=publisher,
            description=description,
        )

        return supported_model_dto
