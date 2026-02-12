from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Selector")


@_attrs_define
class Selector:
    """
    Attributes:
        kind (str):
        container (None | str | Unset):
        page (int | None | Unset):
    """

    kind: str
    container: None | str | Unset = UNSET
    page: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        container: None | str | Unset
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        page: int | None | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if container is not UNSET:
            field_dict["container"] = container
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        def _parse_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container = _parse_container(d.pop("container", UNSET))

        def _parse_page(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page = _parse_page(d.pop("page", UNSET))

        selector = cls(
            kind=kind,
            container=container,
            page=page,
        )

        return selector
