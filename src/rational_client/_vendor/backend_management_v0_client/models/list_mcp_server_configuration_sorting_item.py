from enum import Enum


class ListMcpServerConfigurationSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    ID = "id"
    ISDEFAULT = "isDefault"
    MCPSERVEREXTENSIONICON = "mcpServerExtensionIcon"
    MCPSERVERID = "mcpServerId"
    MCPSERVERNAME = "mcpServerName"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-mcpServerExtensionIcon"
    VALUE_13 = "-createdAt"
    VALUE_15 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-isDefault"
    VALUE_7 = "-mcpServerId"
    VALUE_9 = "-mcpServerName"

    def __str__(self) -> str:
        return str(self.value)
