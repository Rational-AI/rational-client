from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_label import TopicLabel


T = TypeVar("T", bound="TopicConfigurationDto")


@_attrs_define
class TopicConfigurationDto:
    """
    Attributes:
        enabled (bool):
        frequency (int):
        user_message_amount (int):
        model_id (Union[None, UUID, Unset]):
        prompt_template (Union[None, Unset, str]):
        labels (Union[None, Unset, list['TopicLabel']]):
    """

    enabled: bool
    frequency: int
    user_message_amount: int
    model_id: Union[None, UUID, Unset] = UNSET
    prompt_template: Union[None, Unset, str] = UNSET
    labels: Union[None, Unset, list["TopicLabel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        frequency = self.frequency

        user_message_amount = self.user_message_amount

        model_id: Union[None, Unset, str]
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        elif isinstance(self.model_id, UUID):
            model_id = str(self.model_id)
        else:
            model_id = self.model_id

        prompt_template: Union[None, Unset, str]
        if isinstance(self.prompt_template, Unset):
            prompt_template = UNSET
        else:
            prompt_template = self.prompt_template

        labels: Union[None, Unset, list[dict[str, Any]]]
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
        from ..models.topic_label import TopicLabel

        d = dict(src_dict)
        enabled = d.pop("enabled")

        frequency = d.pop("frequency")

        user_message_amount = d.pop("userMessageAmount")

        def _parse_model_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_id_type_0 = UUID(data)

                return model_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        model_id = _parse_model_id(d.pop("modelId", UNSET))

        def _parse_prompt_template(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prompt_template = _parse_prompt_template(d.pop("promptTemplate", UNSET))

        def _parse_labels(data: object) -> Union[None, Unset, list["TopicLabel"]]:
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
                    labels_type_0_item = TopicLabel.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TopicLabel"]], data)

        labels = _parse_labels(d.pop("labels", UNSET))

        topic_configuration_dto = cls(
            enabled=enabled,
            frequency=frequency,
            user_message_amount=user_message_amount,
            model_id=model_id,
            prompt_template=prompt_template,
            labels=labels,
        )

        return topic_configuration_dto
