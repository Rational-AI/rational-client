from enum import Enum


class GetKnowledgeV0ProcessingWorkflowSortingItem(str, Enum):
    CODE = "code"
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ID = "id"
    ISACTIVE = "isActive"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-createdAt"
    VALUE_13 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-code"
    VALUE_9 = "-isActive"

    def __str__(self) -> str:
        return str(self.value)
