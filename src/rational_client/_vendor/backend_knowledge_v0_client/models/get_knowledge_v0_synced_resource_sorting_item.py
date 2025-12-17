from enum import Enum


class GetKnowledgeV0SyncedResourceSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ID = "id"
    KNOWLEDGEID = "knowledgeId"
    KNOWLEDGESOURCEID = "knowledgeSourceId"
    MIMETYPE = "mimeType"
    NAME = "name"
    PARENTID = "parentId"
    SIZE = "size"
    STATUS = "status"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-knowledgeId"
    VALUE_13 = "-knowledgeSourceId"
    VALUE_15 = "-parentId"
    VALUE_17 = "-createdAt"
    VALUE_19 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-size"
    VALUE_7 = "-mimeType"
    VALUE_9 = "-status"

    def __str__(self) -> str:
        return str(self.value)
