from enum import Enum


class ListProcessingRulesSortingItem(str, Enum):
    CODE = "code"
    CREATEDAT = "createdAt"
    ID = "id"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_3 = "-name"
    VALUE_5 = "-code"
    VALUE_7 = "-createdAt"
    VALUE_9 = "-updatedAt"

    def __str__(self) -> str:
        return str(self.value)
