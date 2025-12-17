import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.model_architecture import ModelArchitecture
from ..models.model_purpose import ModelPurpose
from ..models.model_type import ModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_default_parameters import ModelDefaultParameters
    from ..models.model_deployment_dto import ModelDeploymentDto
    from ..models.model_pricing_dto import ModelPricingDto


T = TypeVar("T", bound="RationalModelDto")


@_attrs_define
class RationalModelDto:
    """
    Attributes:
        discriminator (str):
        id (UUID):
        name (str):
        model_identifier (str):
        purpose (ModelPurpose):
        pricing (ModelPricingDto):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_fine_tuned (bool):
        architecture (ModelArchitecture):
        type_ (ModelType):
        description (Union[None, Unset, str]):
        proxy_id (Union[None, UUID, Unset]):
        number_of_params (Union[None, Unset, str]):
        publisher (Union[None, Unset, str]):
        quant (Union[None, Unset, str]):
        size (Union[None, Unset, str]):
        card (Union[None, Unset, str]):
        read_me (Union[None, Unset, str]):
        default_parameters (Union[Unset, ModelDefaultParameters]):
        deployments (Union[Unset, list['ModelDeploymentDto']]):
    """

    discriminator: str
    id: UUID
    name: str
    model_identifier: str
    purpose: ModelPurpose
    pricing: "ModelPricingDto"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_fine_tuned: bool
    architecture: ModelArchitecture
    type_: ModelType
    description: Union[None, Unset, str] = UNSET
    proxy_id: Union[None, UUID, Unset] = UNSET
    number_of_params: Union[None, Unset, str] = UNSET
    publisher: Union[None, Unset, str] = UNSET
    quant: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, str] = UNSET
    card: Union[None, Unset, str] = UNSET
    read_me: Union[None, Unset, str] = UNSET
    default_parameters: Union[Unset, "ModelDefaultParameters"] = UNSET
    deployments: Union[Unset, list["ModelDeploymentDto"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discriminator = self.discriminator

        id = str(self.id)

        name = self.name

        model_identifier = self.model_identifier

        purpose = self.purpose.value

        pricing = self.pricing.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_fine_tuned = self.is_fine_tuned

        architecture = self.architecture.value

        type_ = self.type_.value

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        proxy_id: Union[None, Unset, str]
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        elif isinstance(self.proxy_id, UUID):
            proxy_id = str(self.proxy_id)
        else:
            proxy_id = self.proxy_id

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

        card: Union[None, Unset, str]
        if isinstance(self.card, Unset):
            card = UNSET
        else:
            card = self.card

        read_me: Union[None, Unset, str]
        if isinstance(self.read_me, Unset):
            read_me = UNSET
        else:
            read_me = self.read_me

        default_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_parameters, Unset):
            default_parameters = self.default_parameters.to_dict()

        deployments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = []
            for deployments_item_data in self.deployments:
                deployments_item = deployments_item_data.to_dict()
                deployments.append(deployments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "discriminator": discriminator,
                "id": id,
                "name": name,
                "modelIdentifier": model_identifier,
                "purpose": purpose,
                "pricing": pricing,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "isFineTuned": is_fine_tuned,
                "architecture": architecture,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id
        if number_of_params is not UNSET:
            field_dict["numberOfParams"] = number_of_params
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if quant is not UNSET:
            field_dict["quant"] = quant
        if size is not UNSET:
            field_dict["size"] = size
        if card is not UNSET:
            field_dict["card"] = card
        if read_me is not UNSET:
            field_dict["readMe"] = read_me
        if default_parameters is not UNSET:
            field_dict["defaultParameters"] = default_parameters
        if deployments is not UNSET:
            field_dict["deployments"] = deployments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_default_parameters import ModelDefaultParameters
        from ..models.model_deployment_dto import ModelDeploymentDto
        from ..models.model_pricing_dto import ModelPricingDto

        d = dict(src_dict)
        discriminator = d.pop("discriminator")

        id = UUID(d.pop("id"))

        name = d.pop("name")

        model_identifier = d.pop("modelIdentifier")

        purpose = ModelPurpose(d.pop("purpose"))

        pricing = ModelPricingDto.from_dict(d.pop("pricing"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        is_fine_tuned = d.pop("isFineTuned")

        architecture = ModelArchitecture(d.pop("architecture"))

        type_ = ModelType(d.pop("type"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_proxy_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_id_type_0 = UUID(data)

                return proxy_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proxy_id = _parse_proxy_id(d.pop("proxyId", UNSET))

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

        def _parse_card(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        card = _parse_card(d.pop("card", UNSET))

        def _parse_read_me(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        read_me = _parse_read_me(d.pop("readMe", UNSET))

        _default_parameters = d.pop("defaultParameters", UNSET)
        default_parameters: Union[Unset, ModelDefaultParameters]
        if isinstance(_default_parameters, Unset):
            default_parameters = UNSET
        else:
            default_parameters = ModelDefaultParameters.from_dict(_default_parameters)

        deployments = []
        _deployments = d.pop("deployments", UNSET)
        for deployments_item_data in _deployments or []:
            deployments_item = ModelDeploymentDto.from_dict(deployments_item_data)

            deployments.append(deployments_item)

        rational_model_dto = cls(
            discriminator=discriminator,
            id=id,
            name=name,
            model_identifier=model_identifier,
            purpose=purpose,
            pricing=pricing,
            created_at=created_at,
            updated_at=updated_at,
            is_fine_tuned=is_fine_tuned,
            architecture=architecture,
            type_=type_,
            description=description,
            proxy_id=proxy_id,
            number_of_params=number_of_params,
            publisher=publisher,
            quant=quant,
            size=size,
            card=card,
            read_me=read_me,
            default_parameters=default_parameters,
            deployments=deployments,
        )

        rational_model_dto.additional_properties = d
        return rational_model_dto

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
