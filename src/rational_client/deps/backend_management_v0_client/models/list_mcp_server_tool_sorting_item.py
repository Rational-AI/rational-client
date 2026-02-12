from enum import Enum


class ListMcpServerToolSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ENABLED = "enabled"
    ID = "id"
    MCPSERVERCONFIGURATIONID = "mcpServerConfigurationId"
    MCPSERVERCONFIGURATIONNAME = "mcpServerConfigurationName"
    MCPSERVEREXTENSIONICON = "mcpServerExtensionIcon"
    MCPSERVERNAME = "mcpServerName"
    NAME = "name"
    TITLE = "title"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-updatedAt"
    VALUE_13 = "-enabled"
    VALUE_15 = "-mcpServerConfigurationId"
    VALUE_17 = "-mcpServerConfigurationName"
    VALUE_19 = "-mcpServerName"
    VALUE_21 = "-mcpServerExtensionIcon"
    VALUE_3 = "-title"
    VALUE_5 = "-name"
    VALUE_7 = "-description"
    VALUE_9 = "-createdAt"

    def __str__(self) -> str:
        return str(self.value)
