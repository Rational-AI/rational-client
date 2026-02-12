from enum import Enum


class ListRoomConfigurationSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ID = "id"
    ISACTIVE = "isActive"
    REQUESTJSONRESPONSE = "requestJsonResponse"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_3 = "-isActive"
    VALUE_5 = "-requestJsonResponse"
    VALUE_7 = "-createdAt"
    VALUE_9 = "-updatedAt"

    def __str__(self) -> str:
        return str(self.value)
