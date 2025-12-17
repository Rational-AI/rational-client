from enum import Enum


class GetKnowledgeV0KnowledgeKnowledgeIdResourcesResourceIdAnnotationSortingItem(str, Enum):
    ANNOTATIONTYPE = "annotationType"
    CREATEDAT = "createdAt"
    GENERATEDRESOURCEID = "generatedResourceId"
    ID = "id"
    RATIONALRESOURCEID = "rationalResourceId"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-updatedAt"
    VALUE_3 = "-annotationType"
    VALUE_5 = "-rationalResourceId"
    VALUE_7 = "-generatedResourceId"
    VALUE_9 = "-createdAt"

    def __str__(self) -> str:
        return str(self.value)
