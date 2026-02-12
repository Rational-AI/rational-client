from enum import Enum


class ListEventsSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ID = "id"
    ROOMID = "roomId"
    SENDERTYPE = "senderType"
    STATUS = "status"
    STATUSDETAILS = "statusDetails"
    TYPE = "type"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-type"
    VALUE_13 = "-status"
    VALUE_15 = "-statusDetails"
    VALUE_3 = "-createdAt"
    VALUE_5 = "-updatedAt"
    VALUE_7 = "-roomId"
    VALUE_9 = "-senderType"

    def __str__(self) -> str:
        return str(self.value)
