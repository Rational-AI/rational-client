from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.model_type import ModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_default_parameters import ModelDefaultParameters


T = TypeVar("T", bound="RegisterModelRequest")


@_attrs_define
class RegisterModelRequest:
    """
    Attributes:
        name (str):
        type_ (ModelType):
        is_fine_tuned (bool):
        number_of_params (Union[None, Unset, str]):
        publisher (Union[None, Unset, str]):
        quant (Union[None, Unset, str]):
        size (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        card (Union[None, Unset, str]):
        hugging_face_id (Union[None, Unset, str]):
        default_parameters (Union[Unset, ModelDefaultParameters]):
    """

    name: str
    type_: ModelType
    is_fine_tuned: bool
    number_of_params: Union[None, Unset, str] = UNSET
    publisher: Union[None, Unset, str] = UNSET
    quant: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    card: Union[None, Unset, str] = UNSET
    hugging_face_id: Union[None, Unset, str] = UNSET
    default_parameters: Union[Unset, "ModelDefaultParameters"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        is_fine_tuned = self.is_fine_tuned

        number_of_params: Union[None, Unset, str]
        if isinstance(self.number_of_params, Unset):
            number_of_params = UNSET
        else:
            number_of_params = self.number_of_params

        publisher: Union[None, Unset, str]
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        quant: Union[None, Unset, str]
        if isinstance(self.quant, Unset):
            quant = UNSET
        else:
            quant = self.quant

        size: Union[None, Unset, str]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        card: Union[None, Unset, str]
        if isinstance(self.card, Unset):
            card = UNSET
        else:
            card = self.card

        hugging_face_id: Union[None, Unset, str]
        if isinstance(self.hugging_face_id, Unset):
            hugging_face_id = UNSET
        else:
            hugging_face_id = self.hugging_face_id

        default_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_parameters, Unset):
            default_parameters = self.default_parameters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "isFineTuned": is_fine_tuned,
            }
        )
        if number_of_params is not UNSET:
            field_dict["numberOfParams"] = number_of_params
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if quant is not UNSET:
            field_dict["quant"] = quant
        if size is not UNSET:
            field_dict["size"] = size
        if description is not UNSET:
            field_dict["description"] = description
        if card is not UNSET:
            field_dict["card"] = card
        if hugging_face_id is not UNSET:
            field_dict["huggingFaceId"] = hugging_face_id
        if default_parameters is not UNSET:
            field_dict["defaultParameters"] = default_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_default_parameters import ModelDefaultParameters

        d = dict(src_dict)
        name = d.pop("name")

        type_ = ModelType(d.pop("type"))

        is_fine_tuned = d.pop("isFineTuned")

        def _parse_number_of_params(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number_of_params = _parse_number_of_params(d.pop("numberOfParams", UNSET))

        def _parse_publisher(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_quant(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        quant = _parse_quant(d.pop("quant", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_card(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        card = _parse_card(d.pop("card", UNSET))

        def _parse_hugging_face_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hugging_face_id = _parse_hugging_face_id(d.pop("huggingFaceId", UNSET))

        _default_parameters = d.pop("defaultParameters", UNSET)
        default_parameters: Union[Unset, ModelDefaultParameters]
        if isinstance(_default_parameters, Unset):
            default_parameters = UNSET
        else:
            default_parameters = ModelDefaultParameters.from_dict(_default_parameters)

        register_model_request = cls(
            name=name,
            type_=type_,
            is_fine_tuned=is_fine_tuned,
            number_of_params=number_of_params,
            publisher=publisher,
            quant=quant,
            size=size,
            description=description,
            card=card,
            hugging_face_id=hugging_face_id,
            default_parameters=default_parameters,
        )

        return register_model_request
