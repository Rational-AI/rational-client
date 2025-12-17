from enum import Enum


class ListSupportedModelSortingItem(str, Enum):
    ARCHITECTURE = "architecture"
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    HUGGINGFACEID = "huggingFaceId"
    ID = "id"
    MODELCARD = "modelCard"
    MODELCREATEDAT = "modelCreatedAt"
    NAME = "name"
    NUMBEROFPARAMS = "numberOfParams"
    PUBLISHER = "publisher"
    PURPOSE = "purpose"
    TYPE = "type"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-numberOfParams"
    VALUE_13 = "-type"
    VALUE_15 = "-purpose"
    VALUE_17 = "-publisher"
    VALUE_19 = "-description"
    VALUE_21 = "-modelCreatedAt"
    VALUE_23 = "-createdAt"
    VALUE_25 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-modelCard"
    VALUE_7 = "-huggingFaceId"
    VALUE_9 = "-architecture"

    def __str__(self) -> str:
        return str(self.value)
