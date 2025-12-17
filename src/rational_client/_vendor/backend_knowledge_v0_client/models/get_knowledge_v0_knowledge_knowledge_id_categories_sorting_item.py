from enum import Enum


class GetKnowledgeV0KnowledgeKnowledgeIdCategoriesSortingItem(str, Enum):
    COLOR = "color"
    CREATEDAT = "createdAt"
    ID = "id"
    ISDEFAULT = "isDefault"
    KNOWLEDGEID = "knowledgeId"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-createdAt"
    VALUE_13 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-color"
    VALUE_7 = "-knowledgeId"
    VALUE_9 = "-isDefault"

    def __str__(self) -> str:
        return str(self.value)
