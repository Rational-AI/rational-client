from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.chunker_type import ChunkerType
from ..models.delete_policy import DeletePolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.processing_rule_entity import ProcessingRuleEntity
    from ..models.source_dto import SourceDto


T = TypeVar("T", bound="KnowledgeSourceDto")


@_attrs_define
class KnowledgeSourceDto:
    """
    Attributes:
        id (UUID):
        knowledge_id (UUID):
        source_id (UUID):
        cron_expression (str):
        on_delete (DeletePolicy):
        source_delete_policy (DeletePolicy):
        mount_paths (list[str]):
        source (Union[Unset, SourceDto]):
        processing_rule (Union[Unset, ProcessingRuleEntity]):
        processing_rule_options (Union[Unset, Any]):
        chunker (Union[Unset, ChunkerType]):
        chunker_options (Union[Unset, Any]):
    """

    id: UUID
    knowledge_id: UUID
    source_id: UUID
    cron_expression: str
    on_delete: DeletePolicy
    source_delete_policy: DeletePolicy
    mount_paths: list[str]
    source: Union[Unset, "SourceDto"] = UNSET
    processing_rule: Union[Unset, "ProcessingRuleEntity"] = UNSET
    processing_rule_options: Union[Unset, Any] = UNSET
    chunker: Union[Unset, ChunkerType] = UNSET
    chunker_options: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        knowledge_id = str(self.knowledge_id)

        source_id = str(self.source_id)

        cron_expression = self.cron_expression

        on_delete = self.on_delete.value

        source_delete_policy = self.source_delete_policy.value

        mount_paths = self.mount_paths

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        processing_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.processing_rule, Unset):
            processing_rule = self.processing_rule.to_dict()

        processing_rule_options = self.processing_rule_options

        chunker: Union[Unset, str] = UNSET
        if not isinstance(self.chunker, Unset):
            chunker = self.chunker.value

        chunker_options = self.chunker_options

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "knowledgeId": knowledge_id,
                "sourceId": source_id,
                "cronExpression": cron_expression,
                "onDelete": on_delete,
                "sourceDeletePolicy": source_delete_policy,
                "mountPaths": mount_paths,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source
        if processing_rule is not UNSET:
            field_dict["processingRule"] = processing_rule
        if processing_rule_options is not UNSET:
            field_dict["processingRuleOptions"] = processing_rule_options
        if chunker is not UNSET:
            field_dict["chunker"] = chunker
        if chunker_options is not UNSET:
            field_dict["chunkerOptions"] = chunker_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.processing_rule_entity import ProcessingRuleEntity
        from ..models.source_dto import SourceDto

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        knowledge_id = UUID(d.pop("knowledgeId"))

        source_id = UUID(d.pop("sourceId"))

        cron_expression = d.pop("cronExpression")

        on_delete = DeletePolicy(d.pop("onDelete"))

        source_delete_policy = DeletePolicy(d.pop("sourceDeletePolicy"))

        mount_paths = cast(list[str], d.pop("mountPaths"))

        _source = d.pop("source", UNSET)
        source: Union[Unset, SourceDto]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SourceDto.from_dict(_source)

        _processing_rule = d.pop("processingRule", UNSET)
        processing_rule: Union[Unset, ProcessingRuleEntity]
        if isinstance(_processing_rule, Unset):
            processing_rule = UNSET
        else:
            processing_rule = ProcessingRuleEntity.from_dict(_processing_rule)

        processing_rule_options = d.pop("processingRuleOptions", UNSET)

        _chunker = d.pop("chunker", UNSET)
        chunker: Union[Unset, ChunkerType]
        if isinstance(_chunker, Unset):
            chunker = UNSET
        else:
            chunker = ChunkerType(_chunker)

        chunker_options = d.pop("chunkerOptions", UNSET)

        knowledge_source_dto = cls(
            id=id,
            knowledge_id=knowledge_id,
            source_id=source_id,
            cron_expression=cron_expression,
            on_delete=on_delete,
            source_delete_policy=source_delete_policy,
            mount_paths=mount_paths,
            source=source,
            processing_rule=processing_rule,
            processing_rule_options=processing_rule_options,
            chunker=chunker,
            chunker_options=chunker_options,
        )

        return knowledge_source_dto
