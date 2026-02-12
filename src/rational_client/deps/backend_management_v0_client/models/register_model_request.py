from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        number_of_params (None | str | Unset):
        publisher (None | str | Unset):
        quant (None | str | Unset):
        size (None | str | Unset):
        description (None | str | Unset):
        card (None | str | Unset):
        hugging_face_id (None | str | Unset):
        default_parameters (ModelDefaultParameters | Unset):
    """

    name: str
    type_: ModelType
    is_fine_tuned: bool
    number_of_params: None | str | Unset = UNSET
    publisher: None | str | Unset = UNSET
    quant: None | str | Unset = UNSET
    size: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    card: None | str | Unset = UNSET
    hugging_face_id: None | str | Unset = UNSET
    default_parameters: ModelDefaultParameters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        is_fine_tuned = self.is_fine_tuned

        number_of_params: None | str | Unset
        if isinstance(self.number_of_params, Unset):
            number_of_params = UNSET
        else:
            number_of_params = self.number_of_params

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        quant: None | str | Unset
        if isinstance(self.quant, Unset):
            quant = UNSET
        else:
            quant = self.quant

        size: None | str | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        card: None | str | Unset
        if isinstance(self.card, Unset):
            card = UNSET
        else:
            card = self.card

        hugging_face_id: None | str | Unset
        if isinstance(self.hugging_face_id, Unset):
            hugging_face_id = UNSET
        else:
            hugging_face_id = self.hugging_face_id

        default_parameters: dict[str, Any] | Unset = UNSET
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

        def _parse_number_of_params(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_of_params = _parse_number_of_params(d.pop("numberOfParams", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        def _parse_quant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quant = _parse_quant(d.pop("quant", UNSET))

        def _parse_size(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_card(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card = _parse_card(d.pop("card", UNSET))

        def _parse_hugging_face_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hugging_face_id = _parse_hugging_face_id(d.pop("huggingFaceId", UNSET))

        _default_parameters = d.pop("defaultParameters", UNSET)
        default_parameters: ModelDefaultParameters | Unset
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
