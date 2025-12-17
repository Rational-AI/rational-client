from enum import Enum


class ListMcpServerSortingItem(str, Enum):
    AFTERCALLSCRIPT = "afterCallScript"
    BEFORECALLSCRIPT = "beforeCallScript"
    COMMAND = "command"
    CREATEDAT = "createdAt"
    ID = "id"
    INSTALLSCRIPT = "installScript"
    NAME = "name"
    TOOLSCOUNT = "toolsCount"
    UNINSTALLSCRIPT = "uninstallScript"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-command"
    VALUE_13 = "-toolsCount"
    VALUE_15 = "-afterCallScript"
    VALUE_17 = "-createdAt"
    VALUE_19 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-installScript"
    VALUE_7 = "-uninstallScript"
    VALUE_9 = "-beforeCallScript"

    def __str__(self) -> str:
        return str(self.value)
