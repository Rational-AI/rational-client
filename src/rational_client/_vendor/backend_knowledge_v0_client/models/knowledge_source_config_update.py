from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.chunker_type import ChunkerType
from ..models.delete_policy import DeletePolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processing_rule_config import ProcessingRuleConfig


T = TypeVar("T", bound="KnowledgeSourceConfigUpdate")


@_attrs_define
class KnowledgeSourceConfigUpdate:
    """
    Attributes:
        source_id (UUID):
        cron_expression (str):
        on_delete (DeletePolicy):
        source_delete_policy (DeletePolicy):
        mount_paths (list[str]):
        processing_rule (Union[Unset, ProcessingRuleConfig]):
        chunker (Union[Unset, ChunkerType]):
        chunker_options (Union[Unset, Any]):
        id (Union[None, UUID, Unset]):
    """

    source_id: UUID
    cron_expression: str
    on_delete: DeletePolicy
    source_delete_policy: DeletePolicy
    mount_paths: list[str]
    processing_rule: Union[Unset, "ProcessingRuleConfig"] = UNSET
    chunker: Union[Unset, ChunkerType] = UNSET
    chunker_options: Union[Unset, Any] = UNSET
    id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_id = str(self.source_id)

        cron_expression = self.cron_expression

        on_delete = self.on_delete.value

        source_delete_policy = self.source_delete_policy.value

        mount_paths = self.mount_paths

        processing_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.processing_rule, Unset):
            processing_rule = self.processing_rule.to_dict()

        chunker: Union[Unset, str] = UNSET
        if not isinstance(self.chunker, Unset):
            chunker = self.chunker.value

        chunker_options = self.chunker_options

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sourceId": source_id,
                "cronExpression": cron_expression,
                "onDelete": on_delete,
                "sourceDeletePolicy": source_delete_policy,
                "mountPaths": mount_paths,
            }
        )
        if processing_rule is not UNSET:
            field_dict["processingRule"] = processing_rule
        if chunker is not UNSET:
            field_dict["chunker"] = chunker
        if chunker_options is not UNSET:
            field_dict["chunkerOptions"] = chunker_options
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_rule_config import ProcessingRuleConfig

        d = dict(src_dict)
        source_id = UUID(d.pop("sourceId"))

        cron_expression = d.pop("cronExpression")

        on_delete = DeletePolicy(d.pop("onDelete"))

        source_delete_policy = DeletePolicy(d.pop("sourceDeletePolicy"))

        mount_paths = cast(list[str], d.pop("mountPaths"))

        _processing_rule = d.pop("processingRule", UNSET)
        processing_rule: Union[Unset, ProcessingRuleConfig]
        if isinstance(_processing_rule, Unset):
            processing_rule = UNSET
        else:
            processing_rule = ProcessingRuleConfig.from_dict(_processing_rule)

        _chunker = d.pop("chunker", UNSET)
        chunker: Union[Unset, ChunkerType]
        if isinstance(_chunker, Unset):
            chunker = UNSET
        else:
            chunker = ChunkerType(_chunker)

        chunker_options = d.pop("chunkerOptions", UNSET)

        def _parse_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        id = _parse_id(d.pop("id", UNSET))

        knowledge_source_config_update = cls(
            source_id=source_id,
            cron_expression=cron_expression,
            on_delete=on_delete,
            source_delete_policy=source_delete_policy,
            mount_paths=mount_paths,
            processing_rule=processing_rule,
            chunker=chunker,
            chunker_options=chunker_options,
            id=id,
        )

        return knowledge_source_config_update
