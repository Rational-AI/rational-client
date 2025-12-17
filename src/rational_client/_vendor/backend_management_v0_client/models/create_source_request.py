from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_source_request_configuration_type_0 import CreateSourceRequestConfigurationType0


T = TypeVar("T", bound="CreateSourceRequest")


@_attrs_define
class CreateSourceRequest:
    """
    Attributes:
        name (str):
        type_ (SourceType):
        connector_id (Union[None, UUID, Unset]):
        description (Union[None, Unset, str]):
        icon_url (Union[None, Unset, str]):
        configuration (Union['CreateSourceRequestConfigurationType0', None, Unset]):
    """

    name: str
    type_: SourceType
    connector_id: Union[None, UUID, Unset] = UNSET
    description: Union[None, Unset, str] = UNSET
    icon_url: Union[None, Unset, str] = UNSET
    configuration: Union["CreateSourceRequestConfigurationType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_source_request_configuration_type_0 import CreateSourceRequestConfigurationType0

        name = self.name

        type_ = self.type_.value

        connector_id: Union[None, Unset, str]
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon_url: Union[None, Unset, str]
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        configuration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, CreateSourceRequestConfigurationType0):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_source_request_configuration_type_0 import CreateSourceRequestConfigurationType0

        d = dict(src_dict)
        name = d.pop("name")

        type_ = SourceType(d.pop("type"))

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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_icon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        def _parse_configuration(data: object) -> Union["CreateSourceRequestConfigurationType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = CreateSourceRequestConfigurationType0.from_dict(data)

                return configuration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CreateSourceRequestConfigurationType0", None, Unset], data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        create_source_request = cls(
            name=name,
            type_=type_,
            connector_id=connector_id,
            description=description,
            icon_url=icon_url,
            configuration=configuration,
        )

        return create_source_request
