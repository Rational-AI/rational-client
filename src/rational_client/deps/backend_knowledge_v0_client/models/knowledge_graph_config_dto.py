from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.color_config import ColorConfig


T = TypeVar("T", bound="KnowledgeGraphConfigDto")


@_attrs_define
class KnowledgeGraphConfigDto:
    """
    Attributes:
        category_config (ColorConfig | Unset):
        tag_config (ColorConfig | Unset):
        relation_config (ColorConfig | Unset):
        label_config (ColorConfig | Unset):
    """

    category_config: ColorConfig | Unset = UNSET
    tag_config: ColorConfig | Unset = UNSET
    relation_config: ColorConfig | Unset = UNSET
    label_config: ColorConfig | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category_config, Unset):
            category_config = self.category_config.to_dict()

        tag_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_config, Unset):
            tag_config = self.tag_config.to_dict()

        relation_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation_config, Unset):
            relation_config = self.relation_config.to_dict()

        label_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_config, Unset):
            label_config = self.label_config.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category_config is not UNSET:
            field_dict["categoryConfig"] = category_config
        if tag_config is not UNSET:
            field_dict["tagConfig"] = tag_config
        if relation_config is not UNSET:
            field_dict["relationConfig"] = relation_config
        if label_config is not UNSET:
            field_dict["labelConfig"] = label_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color_config import ColorConfig

        d = dict(src_dict)
        _category_config = d.pop("categoryConfig", UNSET)
        category_config: ColorConfig | Unset
        if isinstance(_category_config, Unset):
            category_config = UNSET
        else:
            category_config = ColorConfig.from_dict(_category_config)

        _tag_config = d.pop("tagConfig", UNSET)
        tag_config: ColorConfig | Unset
        if isinstance(_tag_config, Unset):
            tag_config = UNSET
        else:
            tag_config = ColorConfig.from_dict(_tag_config)

        _relation_config = d.pop("relationConfig", UNSET)
        relation_config: ColorConfig | Unset
        if isinstance(_relation_config, Unset):
            relation_config = UNSET
        else:
            relation_config = ColorConfig.from_dict(_relation_config)

        _label_config = d.pop("labelConfig", UNSET)
        label_config: ColorConfig | Unset
        if isinstance(_label_config, Unset):
            label_config = UNSET
        else:
            label_config = ColorConfig.from_dict(_label_config)

        knowledge_graph_config_dto = cls(
            category_config=category_config,
            tag_config=tag_config,
            relation_config=relation_config,
            label_config=label_config,
        )

        return knowledge_graph_config_dto
