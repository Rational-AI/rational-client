import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.model_purpose import ModelPurpose
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_pricing_dto import ModelPricingDto


T = TypeVar("T", bound="ModelDto")


@_attrs_define
class ModelDto:
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
        description (Union[None, Unset, str]):
        proxy_id (Union[None, UUID, Unset]):
    """

    discriminator: str
    id: UUID
    name: str
    model_identifier: str
    purpose: ModelPurpose
    pricing: "ModelPricingDto"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: Union[None, Unset, str] = UNSET
    proxy_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        discriminator = self.discriminator

        id = str(self.id)

        name = self.name

        model_identifier = self.model_identifier

        purpose = self.purpose.value

        pricing = self.pricing.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        field_dict: dict[str, Any] = {}

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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        model_dto = cls(
            discriminator=discriminator,
            id=id,
            name=name,
            model_identifier=model_identifier,
            purpose=purpose,
            pricing=pricing,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            proxy_id=proxy_id,
        )

        return model_dto
