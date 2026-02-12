from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BboxSelector")


@_attrs_define
class BboxSelector:
    """
    Attributes:
        kind (str):
        container (None | str | Unset):
        page (int | None | Unset):
        xmin (float | Unset):
        ymin (float | Unset):
        xmax (float | Unset):
        ymax (float | Unset):
    """

    kind: str
    container: None | str | Unset = UNSET
    page: int | None | Unset = UNSET
    xmin: float | Unset = UNSET
    ymin: float | Unset = UNSET
    xmax: float | Unset = UNSET
    ymax: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        xmin = self.xmin

        ymin = self.ymin

        xmax = self.xmax

        ymax = self.ymax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if container is not UNSET:
            field_dict["container"] = container
        if page is not UNSET:
            field_dict["page"] = page
        if xmin is not UNSET:
            field_dict["xmin"] = xmin
        if ymin is not UNSET:
            field_dict["ymin"] = ymin
        if xmax is not UNSET:
            field_dict["xmax"] = xmax
        if ymax is not UNSET:
            field_dict["ymax"] = ymax

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

        xmin = d.pop("xmin", UNSET)

        ymin = d.pop("ymin", UNSET)

        xmax = d.pop("xmax", UNSET)

        ymax = d.pop("ymax", UNSET)

        bbox_selector = cls(
            kind=kind,
            container=container,
            page=page,
            xmin=xmin,
            ymin=ymin,
            xmax=xmax,
            ymax=ymax,
        )

        bbox_selector.additional_properties = d
        return bbox_selector

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
