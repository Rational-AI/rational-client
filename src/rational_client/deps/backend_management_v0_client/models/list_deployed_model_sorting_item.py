from enum import Enum


class ListDeployedModelSortingItem(str, Enum):
    CREATEDAT = "createdAt"
    DEPLOYMENTID = "deploymentId"
    ERRORMESSAGE = "errorMessage"
    GPUCOUNT = "gpuCount"
    HUGGINGFACEID = "huggingFaceId"
    ID = "id"
    LASTUSEDAT = "lastUsedAt"
    MODELID = "modelId"
    MODELNAME = "modelName"
    SERVICEURL = "serviceUrl"
    STATUS = "status"
    VALUE_1 = "-id"
    VALUE_11 = "-serviceUrl"
    VALUE_13 = "-gpuCount"
    VALUE_15 = "-createdAt"
    VALUE_17 = "-lastUsedAt"
    VALUE_19 = "-errorMessage"
    VALUE_21 = "-huggingFaceId"
    VALUE_3 = "-deploymentId"
    VALUE_5 = "-modelId"
    VALUE_7 = "-modelName"
    VALUE_9 = "-status"

    def __str__(self) -> str:
        return str(self.value)
