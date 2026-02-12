from enum import Enum


class ListSyncedResourcesSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ID = "id"
    KNOWLEDGEID = "knowledgeId"
    KNOWLEDGESOURCEID = "knowledgeSourceId"
    LASTERROR = "lastError"
    MIMETYPE = "mimeType"
    NAME = "name"
    PARENTID = "parentId"
    SIZE = "size"
    STATUS = "status"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-lastError"
    VALUE_13 = "-knowledgeId"
    VALUE_15 = "-knowledgeSourceId"
    VALUE_17 = "-parentId"
    VALUE_19 = "-createdAt"
    VALUE_21 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-size"
    VALUE_7 = "-mimeType"
    VALUE_9 = "-status"

    def __str__(self) -> str:
        return str(self.value)
