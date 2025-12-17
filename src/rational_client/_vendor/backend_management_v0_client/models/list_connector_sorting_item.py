from enum import Enum


class ListConnectorSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ID = "id"
    MODELSCOUNT = "modelsCount"
    NAME = "name"
    SOURCESCOUNT = "sourcesCount"
    TOOLSCOUNT = "toolsCount"
    TYPE = "type"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-sourcesCount"
    VALUE_13 = "-toolsCount"
    VALUE_15 = "-createdAt"
    VALUE_17 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-type"
    VALUE_9 = "-modelsCount"

    def __str__(self) -> str:
        return str(self.value)
