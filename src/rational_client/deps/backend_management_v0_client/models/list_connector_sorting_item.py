from enum import Enum


class ListConnectorSortingItem(str, Enum):
    BUILTIN = "builtIn"
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
    VALUE_11 = "-modelsCount"
    VALUE_13 = "-sourcesCount"
    VALUE_15 = "-toolsCount"
    VALUE_17 = "-createdAt"
    VALUE_19 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-type"
    VALUE_9 = "-builtIn"

    def __str__(self) -> str:
        return str(self.value)
