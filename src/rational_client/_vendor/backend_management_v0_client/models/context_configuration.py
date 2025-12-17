from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.widget import Widget


T = TypeVar("T", bound="ContextConfiguration")


@_attrs_define
class ContextConfiguration:
    """
    Attributes:
        widgets (Union[None, Unset, list['Widget']]):
    """

    widgets: Union[None, Unset, list["Widget"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        widgets: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.widgets, Unset):
            widgets = UNSET
        elif isinstance(self.widgets, list):
            widgets = []
            for widgets_type_0_item_data in self.widgets:
                widgets_type_0_item = widgets_type_0_item_data.to_dict()
                widgets.append(widgets_type_0_item)

        else:
            widgets = self.widgets

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.widget import Widget

        d = dict(src_dict)

        def _parse_widgets(data: object) -> Union[None, Unset, list["Widget"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                widgets_type_0 = []
                _widgets_type_0 = data
                for widgets_type_0_item_data in _widgets_type_0:
                    widgets_type_0_item = Widget.from_dict(widgets_type_0_item_data)

                    widgets_type_0.append(widgets_type_0_item)

                return widgets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Widget"]], data)

        widgets = _parse_widgets(d.pop("widgets", UNSET))

        context_configuration = cls(
            widgets=widgets,
        )

        return context_configuration
