from enum import Enum


class ListTouchpointToolSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ID = "id"
    NAME = "name"
    TITLE = "title"
    TOUCHPOINTID = "touchpointId"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-createdAt"
    VALUE_13 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-title"
    VALUE_7 = "-description"
    VALUE_9 = "-touchpointId"

    def __str__(self) -> str:
        return str(self.value)
