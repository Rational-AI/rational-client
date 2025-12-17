from enum import Enum


class ListChannelSortingItem(str, Enum):
    DESCRIPTION = "description"
    EXTENSIONCHANNELPROVIDERID = "extensionChannelProviderId"
    EXTENSIONID = "extensionId"
    ICON = "icon"
    ID = "id"
    MODE = "mode"
    NAME = "name"
    TYPE = "type"
    VALUE_1 = "-id"
    VALUE_11 = "-type"
    VALUE_13 = "-icon"
    VALUE_15 = "-extensionId"
    VALUE_3 = "-name"
    VALUE_5 = "-extensionChannelProviderId"
    VALUE_7 = "-description"
    VALUE_9 = "-mode"

    def __str__(self) -> str:
        return str(self.value)
