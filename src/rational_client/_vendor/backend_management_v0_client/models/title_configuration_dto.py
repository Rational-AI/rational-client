from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TitleConfigurationDto")


@_attrs_define
class TitleConfigurationDto:
    """
    Attributes:
        enabled (bool):
        frequency (int):
        user_message_amount (int):
        model_id (Union[None, UUID, Unset]):
        prompt_template (Union[None, Unset, str]):
    """

    enabled: bool
    frequency: int
    user_message_amount: int
    model_id: Union[None, UUID, Unset] = UNSET
    prompt_template: Union[None, Unset, str] = UNSET

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        title_configuration_dto = cls(
            enabled=enabled,
            frequency=frequency,
            user_message_amount=user_message_amount,
            model_id=model_id,
            prompt_template=prompt_template,
        )

        return title_configuration_dto
