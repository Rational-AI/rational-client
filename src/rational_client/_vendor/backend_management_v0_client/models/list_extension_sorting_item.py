from enum import Enum


class ListExtensionSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    EXTENSIONSREGISTRYID = "extensionsRegistryId"
    ICON = "icon"
    ID = "id"
    INSTALLED = "installed"
    ISENABLED = "isEnabled"
    NAME = "name"
    NUMBEROFCHANNELS = "numberOfChannels"
    NUMBEROFTOOLS = "numberOfTools"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-icon"
    VALUE_13 = "-isEnabled"
    VALUE_15 = "-installed"
    VALUE_17 = "-numberOfChannels"
    VALUE_19 = "-numberOfTools"
    VALUE_21 = "-createdAt"
    VALUE_23 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-extensionsRegistryId"
    VALUE_9 = "-version"
    VERSION = "version"

    def __str__(self) -> str:
        return str(self.value)
