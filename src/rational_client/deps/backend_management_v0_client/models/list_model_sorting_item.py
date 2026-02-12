from enum import Enum


class ListModelSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    DISCRIMINATOR = "discriminator"
    ID = "id"
    MODELIDENTIFIER = "modelIdentifier"
    NAME = "name"
    PRICING_COSTPERINPUTTOKEN = "pricing.costPerInputToken"
    PRICING_COSTPEROUTPUTTOKEN = "pricing.costPerOutputToken"
    PRICING_COSTPERREQUEST = "pricing.costPerRequest"
    PRICING_COSTPERSECOND = "pricing.costPerSecond"
    PRICING_ENABLED = "pricing.enabled"
    PROVIDERMODELIDENTIFIER = "providerModelIdentifier"
    PROXYID = "proxyId"
    PURPOSE = "purpose"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-description"
    VALUE_13 = "-purpose"
    VALUE_15 = "-pricing.enabled"
    VALUE_17 = "-pricing.costPerRequest"
    VALUE_19 = "-pricing.costPerSecond"
    VALUE_21 = "-pricing.costPerInputToken"
    VALUE_23 = "-pricing.costPerOutputToken"
    VALUE_25 = "-createdAt"
    VALUE_27 = "-updatedAt"
    VALUE_29 = "-proxyId"
    VALUE_3 = "-discriminator"
    VALUE_5 = "-name"
    VALUE_7 = "-modelIdentifier"
    VALUE_9 = "-providerModelIdentifier"

    def __str__(self) -> str:
        return str(self.value)
