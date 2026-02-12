from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.delete_policy import DeletePolicy
from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_source_request_configuration import UpdateSourceRequestConfiguration


T = TypeVar("T", bound="UpdateSourceRequest")


@_attrs_define
class UpdateSourceRequest:
    """
    Attributes:
        name (str | Unset):
        description (None | str | Unset):
        icon_url (None | str | Unset):
        type_ (SourceType | Unset):
        connector_id (None | Unset | UUID):
        on_delete (DeletePolicy | Unset):
        cron_expression (None | str | Unset):
        root (str | Unset):
        paths (list[str] | Unset):
        configuration (UpdateSourceRequestConfiguration | Unset):
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    type_: SourceType | Unset = UNSET
    connector_id: None | Unset | UUID = UNSET
    on_delete: DeletePolicy | Unset = UNSET
    cron_expression: None | str | Unset = UNSET
    root: str | Unset = UNSET
    paths: list[str] | Unset = UNSET
    configuration: UpdateSourceRequestConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        connector_id: None | str | Unset
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

        on_delete: str | Unset = UNSET
        if not isinstance(self.on_delete, Unset):
            on_delete = self.on_delete.value

        cron_expression: None | str | Unset
        if isinstance(self.cron_expression, Unset):
            cron_expression = UNSET
        else:
            cron_expression = self.cron_expression

        root = self.root

        paths: list[str] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
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
        from ..models.update_source_request_configuration import UpdateSourceRequestConfiguration

        d = dict(src_dict)
        name = d.pop("name", UNSET)

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

        _type_ = d.pop("type", UNSET)
        type_: SourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SourceType(_type_)

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

        root = d.pop("root", UNSET)

        paths = cast(list[str], d.pop("paths", UNSET))

        _configuration = d.pop("configuration", UNSET)
        configuration: UpdateSourceRequestConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = UpdateSourceRequestConfiguration.from_dict(_configuration)

        update_source_request = cls(
            name=name,
            description=description,
            icon_url=icon_url,
            type_=type_,
            connector_id=connector_id,
            on_delete=on_delete,
            cron_expression=cron_expression,
            root=root,
            paths=paths,
            configuration=configuration,
        )

        return update_source_request
