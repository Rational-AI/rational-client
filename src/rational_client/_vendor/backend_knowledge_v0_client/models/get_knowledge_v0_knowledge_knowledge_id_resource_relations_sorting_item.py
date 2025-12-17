from enum import Enum


class GetKnowledgeV0KnowledgeKnowledgeIdResourceRelationsSortingItem(str, Enum):
    FROMRESOURCEID = "fromResourceId"
    ID = "id"
    TORESOURCEID = "toResourceId"
    TYPE = "type"
    VALUE_1 = "-id"
    VALUE_3 = "-type"
    VALUE_5 = "-fromResourceId"
    VALUE_7 = "-toResourceId"

    def __str__(self) -> str:
        return str(self.value)
