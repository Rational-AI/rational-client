from enum import Enum


class ListUserSortingItem(str, Enum):
    AUTHENTICATIONID = "authenticationId"
    CREATEDAT = "createdAt"
    EMAIL = "email"
    FAMILYNAME = "familyName"
    GIVENNAME = "givenName"
    ID = "id"
    ISADMIN = "isAdmin"
    ISENABLED = "isEnabled"
    ROOMSCOUNT = "roomsCount"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-givenName"
    VALUE_13 = "-email"
    VALUE_15 = "-roomsCount"
    VALUE_17 = "-createdAt"
    VALUE_19 = "-updatedAt"
    VALUE_3 = "-authenticationId"
    VALUE_5 = "-isAdmin"
    VALUE_7 = "-isEnabled"
    VALUE_9 = "-familyName"

    def __str__(self) -> str:
        return str(self.value)
