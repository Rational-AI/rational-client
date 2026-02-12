from enum import Enum


class ListResourcesSortingItem(str, Enum):
    CATEGORY = "category"
    CREATEDAT = "createdAt"
    ID = "id"
    KNOWLEDGEID = "knowledgeId"
    NAME = "name"
    NOTES = "notes"
    RELATEDRESOURCESCOUNT = "relatedResourcesCount"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-relatedResourcesCount"
    VALUE_13 = "-createdAt"
    VALUE_15 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-category"
    VALUE_7 = "-notes"
    VALUE_9 = "-knowledgeId"

    def __str__(self) -> str:
        return str(self.value)
