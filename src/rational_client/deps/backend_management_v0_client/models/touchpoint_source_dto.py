from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.touchpoint_source_dto_configuration import TouchpointSourceDtoConfiguration


T = TypeVar("T", bound="TouchpointSourceDto")


@_attrs_define
class TouchpointSourceDto:
    """
    Attributes:
        id (UUID):
        name (str):
        configuration (TouchpointSourceDtoConfiguration):
        description (None | str | Unset):
        icon (None | str | Unset):
    """

    id: UUID
    name: str
    configuration: TouchpointSourceDtoConfiguration
    description: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        configuration = self.configuration.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "configuration": configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.touchpoint_source_dto_configuration import TouchpointSourceDtoConfiguration

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        configuration = TouchpointSourceDtoConfiguration.from_dict(d.pop("configuration"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        touchpoint_source_dto = cls(
            id=id,
            name=name,
            configuration=configuration,
            description=description,
            icon=icon,
        )

        return touchpoint_source_dto
