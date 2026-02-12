from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.source_type import SourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_source_origin_contents_request_configuration_type_0 import (
        ListSourceOriginContentsRequestConfigurationType0,
    )


T = TypeVar("T", bound="ListSourceOriginContentsRequest")


@_attrs_define
class ListSourceOriginContentsRequest:
    """
    Attributes:
        type_ (SourceType):
        connector_id (None | Unset | UUID):
        root (None | str | Unset):
        paths (list[str] | None | Unset):
        configuration (ListSourceOriginContentsRequestConfigurationType0 | None | Unset):
    """

    type_: SourceType
    connector_id: None | Unset | UUID = UNSET
    root: None | str | Unset = UNSET
    paths: list[str] | None | Unset = UNSET
    configuration: ListSourceOriginContentsRequestConfigurationType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.list_source_origin_contents_request_configuration_type_0 import (
            ListSourceOriginContentsRequestConfigurationType0,
        )

        type_ = self.type_.value

        connector_id: None | str | Unset
        if isinstance(self.connector_id, Unset):
            connector_id = UNSET
        elif isinstance(self.connector_id, UUID):
            connector_id = str(self.connector_id)
        else:
            connector_id = self.connector_id

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
        elif isinstance(self.configuration, ListSourceOriginContentsRequestConfigurationType0):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if connector_id is not UNSET:
            field_dict["connectorId"] = connector_id
        if root is not UNSET:
            field_dict["root"] = root
        if paths is not UNSET:
            field_dict["paths"] = paths
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_source_origin_contents_request_configuration_type_0 import (
            ListSourceOriginContentsRequestConfigurationType0,
        )

        d = dict(src_dict)
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

        def _parse_configuration(data: object) -> ListSourceOriginContentsRequestConfigurationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = ListSourceOriginContentsRequestConfigurationType0.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListSourceOriginContentsRequestConfigurationType0 | None | Unset, data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        list_source_origin_contents_request = cls(
            type_=type_,
            connector_id=connector_id,
            root=root,
            paths=paths,
            configuration=configuration,
        )

        return list_source_origin_contents_request
