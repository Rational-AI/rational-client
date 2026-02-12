from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sentiment_label import SentimentLabel


T = TypeVar("T", bound="SentimentConfigurationDto")


@_attrs_define
class SentimentConfigurationDto:
    """
    Attributes:
        enabled (bool):
        frequency (int):
        user_message_amount (int):
        model_id (None | Unset | UUID):
        prompt_template (None | str | Unset):
        labels (list[SentimentLabel] | None | Unset):
    """

    enabled: bool
    frequency: int
    user_message_amount: int
    model_id: None | Unset | UUID = UNSET
    prompt_template: None | str | Unset = UNSET
    labels: list[SentimentLabel] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        frequency = self.frequency

        user_message_amount = self.user_message_amount

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        elif isinstance(self.model_id, UUID):
            model_id = str(self.model_id)
        else:
            model_id = self.model_id

        prompt_template: None | str | Unset
        if isinstance(self.prompt_template, Unset):
            prompt_template = UNSET
        else:
            prompt_template = self.prompt_template

        labels: list[dict[str, Any]] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "frequency": frequency,
                "userMessageAmount": user_message_amount,
            }
        )
        if model_id is not UNSET:
            field_dict["modelId"] = model_id
        if prompt_template is not UNSET:
            field_dict["promptTemplate"] = prompt_template
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sentiment_label import SentimentLabel

        d = dict(src_dict)
        enabled = d.pop("enabled")

        frequency = d.pop("frequency")

        user_message_amount = d.pop("userMessageAmount")

        def _parse_model_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_id_type_0 = UUID(data)

                return model_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        model_id = _parse_model_id(d.pop("modelId", UNSET))

        def _parse_prompt_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_template = _parse_prompt_template(d.pop("promptTemplate", UNSET))

        def _parse_labels(data: object) -> list[SentimentLabel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in _labels_type_0:
                    labels_type_0_item = SentimentLabel.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SentimentLabel] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        sentiment_configuration_dto = cls(
            enabled=enabled,
            frequency=frequency,
            user_message_amount=user_message_amount,
            model_id=model_id,
            prompt_template=prompt_template,
            labels=labels,
        )

        return sentiment_configuration_dto
