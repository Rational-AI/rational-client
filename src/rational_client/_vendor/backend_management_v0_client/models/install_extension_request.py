from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.install_extension_request_configuration import InstallExtensionRequestConfiguration


T = TypeVar("T", bound="InstallExtensionRequest")


@_attrs_define
class InstallExtensionRequest:
    """
    Attributes:
        configuration (InstallExtensionRequestConfiguration):
        source_ids (list[UUID]):
    """

    configuration: "InstallExtensionRequestConfiguration"
    source_ids: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        source_ids = []
        for source_ids_item_data in self.source_ids:
            source_ids_item = str(source_ids_item_data)
            source_ids.append(source_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration": configuration,
                "sourceIds": source_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.install_extension_request_configuration import InstallExtensionRequestConfiguration

        d = dict(src_dict)
        configuration = InstallExtensionRequestConfiguration.from_dict(d.pop("configuration"))

        source_ids = []
        _source_ids = d.pop("sourceIds")
        for source_ids_item_data in _source_ids:
            source_ids_item = UUID(source_ids_item_data)

            source_ids.append(source_ids_item)

        install_extension_request = cls(
            configuration=configuration,
            source_ids=source_ids,
        )

        return install_extension_request
