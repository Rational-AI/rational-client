from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_dto_configuration import SourceDtoConfiguration


T = TypeVar("T", bound="SourceDto")


@_attrs_define
class SourceDto:
    """
    Attributes:
        id (UUID):
        name (str):
        type_ (SourceType):
        configuration (SourceDtoConfiguration):
        description (Union[None, Unset, str]):
        connector_id (Union[None, UUID, Unset]):
        icon (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    type_: SourceType
    configuration: "SourceDtoConfiguration"
    description: Union[None, Unset, str] = UNSET
    connector_id: Union[None, UUID, Unset] = UNSET
    icon: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        configuration = self.configuration.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        connector_id: Union[None, Unset, str]
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

        icon: Union[None, Unset, str]
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "configuration": configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_dto_configuration import SourceDtoConfiguration

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = SourceType(d.pop("type"))

        configuration = SourceDtoConfiguration.from_dict(d.pop("configuration"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_connector_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connector_id_type_0 = UUID(data)

                return connector_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        connector_id = _parse_connector_id(d.pop("connectorId", UNSET))

        def _parse_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon = _parse_icon(d.pop("icon", UNSET))

        source_dto = cls(
            id=id,
            name=name,
            type_=type_,
            configuration=configuration,
            description=description,
            connector_id=connector_id,
            icon=icon,
        )

        return source_dto
