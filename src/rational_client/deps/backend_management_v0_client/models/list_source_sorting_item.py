from enum import Enum


class ListSourceSortingItem(str, Enum):
    CONNECTORID = "connectorId"
    CRONEXPRESSION = "cronExpression"
    DESCRIPTION = "description"
    ICON = "icon"
    ID = "id"
    NAME = "name"
    ONDELETE = "onDelete"
    ROOT = "root"
    TYPE = "type"
    VALUE_1 = "-id"
    VALUE_11 = "-cronExpression"
    VALUE_13 = "-onDelete"
    VALUE_15 = "-root"
    VALUE_17 = "-connectorId"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-type"
    VALUE_9 = "-icon"

    def __str__(self) -> str:
        return str(self.value)
