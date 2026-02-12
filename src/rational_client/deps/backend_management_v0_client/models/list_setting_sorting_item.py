from enum import Enum


class ListSettingSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ID = "id"
    KEY = "key"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_3 = "-key"
    VALUE_5 = "-visibility"
    VALUE_7 = "-createdAt"
    VALUE_9 = "-updatedAt"
    VISIBILITY = "visibility"

    def __str__(self) -> str:
        return str(self.value)
