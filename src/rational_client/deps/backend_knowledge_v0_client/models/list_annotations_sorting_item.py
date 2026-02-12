from enum import Enum


class ListAnnotationsSortingItem(str, Enum):
    ANNOTATIONTYPE = "annotationType"
    CONTENT = "content"
    CREATEDAT = "createdAt"
    ENABLED = "enabled"
    GENERATEDRESOURCEID = "generatedResourceId"
    ID = "id"
    LABEL = "label"
    NOTE = "note"
    POSITION = "position"
    RATIONALRESOURCEID = "rationalResourceId"
    TITLE = "title"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-note"
    VALUE_13 = "-label"
    VALUE_15 = "-rationalResourceId"
    VALUE_17 = "-generatedResourceId"
    VALUE_19 = "-enabled"
    VALUE_21 = "-createdAt"
    VALUE_23 = "-updatedAt"
    VALUE_3 = "-annotationType"
    VALUE_5 = "-position"
    VALUE_7 = "-title"
    VALUE_9 = "-content"

    def __str__(self) -> str:
        return str(self.value)
