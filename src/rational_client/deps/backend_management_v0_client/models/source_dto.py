from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.delete_policy import DeletePolicy
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
        on_delete (DeletePolicy):
        root (str):
        paths (list[str]):
        configuration (SourceDtoConfiguration):
        description (None | str | Unset):
        icon (None | str | Unset):
        cron_expression (None | str | Unset):
        connector_id (None | Unset | UUID):
    """

    id: UUID
    name: str
    type_: SourceType
    on_delete: DeletePolicy
    root: str
    paths: list[str]
    configuration: SourceDtoConfiguration
    description: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    cron_expression: None | str | Unset = UNSET
    connector_id: None | Unset | UUID = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        type_ = self.type_.value

        on_delete = self.on_delete.value

        root = self.root

        paths = self.paths

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

        cron_expression: None | str | Unset
        if isinstance(self.cron_expression, Unset):
            cron_expression = UNSET
        else:
            cron_expression = self.cron_expression

        connector_id: None | str | Unset
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "onDelete": on_delete,
                "root": root,
                "paths": paths,
                "configuration": configuration,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_dto_configuration import SourceDtoConfiguration

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        type_ = SourceType(d.pop("type"))

        on_delete = DeletePolicy(d.pop("onDelete"))

        root = d.pop("root")

        paths = cast(list[str], d.pop("paths"))

        configuration = SourceDtoConfiguration.from_dict(d.pop("configuration"))

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

        def _parse_cron_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron_expression = _parse_cron_expression(d.pop("cronExpression", UNSET))

        def _parse_connector_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connector_id_type_0 = UUID(data)

                return connector_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        connector_id = _parse_connector_id(d.pop("connectorId", UNSET))

        source_dto = cls(
            id=id,
            name=name,
            type_=type_,
            on_delete=on_delete,
            root=root,
            paths=paths,
            configuration=configuration,
            description=description,
            icon=icon,
            cron_expression=cron_expression,
            connector_id=connector_id,
        )

        return source_dto
