from enum import Enum


class ListSourceSortingItem(str, Enum):
    CONNECTORID = "connectorId"
    DESCRIPTION = "description"
    ICON = "icon"
    ID = "id"
    NAME = "name"
    TYPE = "type"
    VALUE_1 = "-id"
    VALUE_11 = "-icon"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-type"
    VALUE_9 = "-connectorId"

    def __str__(self) -> str:
        return str(self.value)
