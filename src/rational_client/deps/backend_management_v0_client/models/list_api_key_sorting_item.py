from enum import Enum


class ListApiKeySortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ENABLED = "enabled"
    ID = "id"
    MASKEDKEY = "maskedKey"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-maskedKey"
    VALUE_7 = "-enabled"
    VALUE_9 = "-createdAt"

    def __str__(self) -> str:
        return str(self.value)
