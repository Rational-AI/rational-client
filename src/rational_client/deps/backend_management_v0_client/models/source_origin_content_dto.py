from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SourceOriginContentDto")


@_attrs_define
class SourceOriginContentDto:
    """
    Attributes:
        name (str):
        path (str):
        is_bucket (bool):
        is_dir (bool):
    """

    name: str
    path: str
    is_bucket: bool
    is_dir: bool

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        is_bucket = self.is_bucket

        is_dir = self.is_dir

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "path": path,
                "isBucket": is_bucket,
                "isDir": is_dir,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        is_bucket = d.pop("isBucket")

        is_dir = d.pop("isDir")

        source_origin_content_dto = cls(
            name=name,
            path=path,
            is_bucket=is_bucket,
            is_dir=is_dir,
        )

        return source_origin_content_dto
