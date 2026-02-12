from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.delete_policy import DeletePolicy
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
        connector_id (None | Unset | UUID):
        description (None | str | Unset):
        icon_url (None | str | Unset):
        on_delete (DeletePolicy | Unset):
        cron_expression (None | str | Unset):
        root (None | str | Unset):
        paths (list[str] | None | Unset):
        configuration (CreateSourceRequestConfigurationType0 | None | Unset):
    """

    name: str
    type_: SourceType
    connector_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    on_delete: DeletePolicy | Unset = UNSET
    cron_expression: None | str | Unset = UNSET
    root: None | str | Unset = UNSET
    paths: list[str] | None | Unset = UNSET
    configuration: CreateSourceRequestConfigurationType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_source_request_configuration_type_0 import CreateSourceRequestConfigurationType0

        name = self.name

        type_ = self.type_.value

        connector_id: None | str | Unset
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        on_delete: str | Unset = UNSET
        if not isinstance(self.on_delete, Unset):
            on_delete = self.on_delete.value

        cron_expression: None | str | Unset
        if isinstance(self.cron_expression, Unset):
            cron_expression = UNSET
        else:
            cron_expression = self.cron_expression

        root: None | str | Unset
        if isinstance(self.root, Unset):
            root = UNSET
        else:
            root = self.root

        paths: list[str] | None | Unset
        if isinstance(self.paths, Unset):
            paths = UNSET
        elif isinstance(self.paths, list):
            paths = self.paths

        else:
            paths = self.paths

        configuration: dict[str, Any] | None | Unset
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
        if on_delete is not UNSET:
            field_dict["onDelete"] = on_delete
        if cron_expression is not UNSET:
            field_dict["cronExpression"] = cron_expression
        if root is not UNSET:
            field_dict["root"] = root
        if paths is not UNSET:
            field_dict["paths"] = paths
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_source_request_configuration_type_0 import CreateSourceRequestConfigurationType0

        d = dict(src_dict)
        name = d.pop("name")

        type_ = SourceType(d.pop("type"))

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("iconUrl", UNSET))

        _on_delete = d.pop("onDelete", UNSET)
        on_delete: DeletePolicy | Unset
        if isinstance(_on_delete, Unset):
            on_delete = UNSET
        else:
            on_delete = DeletePolicy(_on_delete)

        def _parse_cron_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cron_expression = _parse_cron_expression(d.pop("cronExpression", UNSET))

        def _parse_root(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        root = _parse_root(d.pop("root", UNSET))

        def _parse_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                paths_type_0 = cast(list[str], data)

                return paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        paths = _parse_paths(d.pop("paths", UNSET))

        def _parse_configuration(data: object) -> CreateSourceRequestConfigurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = CreateSourceRequestConfigurationType0.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateSourceRequestConfigurationType0 | None | Unset, data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        create_source_request = cls(
            name=name,
            type_=type_,
            connector_id=connector_id,
            description=description,
            icon_url=icon_url,
            on_delete=on_delete,
            cron_expression=cron_expression,
            root=root,
            paths=paths,
            configuration=configuration,
        )

        return create_source_request
