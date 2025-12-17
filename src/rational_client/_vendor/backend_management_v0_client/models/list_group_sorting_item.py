from enum import Enum


class ListGroupSortingItem(str, Enum):
    ALLOWANONYMOUS = "allowAnonymous"
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ID = "id"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    USERSCOUNT = "usersCount"
    VALUE_1 = "-id"
    VALUE_11 = "-createdAt"
    VALUE_13 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-allowAnonymous"
    VALUE_9 = "-usersCount"

    def __str__(self) -> str:
        return str(self.value)
