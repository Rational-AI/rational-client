from enum import Enum


class ListProxiesSortingItem(str, Enum):
    CONNECTORID = "connectorId"
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ID = "id"
    NAME = "name"
    PROVIDER = "provider"
    PROVIDERBASEURL = "providerBaseUrl"
    PROXYAPIKEY = "proxyApiKey"
    PROXYAPIKEYSUFFIX = "proxyApiKeySuffix"
    ROTATEDAT = "rotatedAt"
    TRACKUSAGE = "trackUsage"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-providerBaseUrl"
    VALUE_13 = "-trackUsage"
    VALUE_15 = "-proxyApiKeySuffix"
    VALUE_17 = "-proxyApiKey"
    VALUE_19 = "-createdAt"
    VALUE_21 = "-updatedAt"
    VALUE_23 = "-rotatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-connectorId"
    VALUE_9 = "-provider"

    def __str__(self) -> str:
        return str(self.value)
