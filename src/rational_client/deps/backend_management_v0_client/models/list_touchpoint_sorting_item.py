from enum import Enum


class ListTouchpointSortingItem(str, Enum):
    ALLOWANONYMOUS = "allowAnonymous"
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ENABLEQUESTIONS = "enableQuestions"
    ICON = "icon"
    ID = "id"
    ISENABLED = "isEnabled"
    MODELPROMPT = "modelPrompt"
    NAME = "name"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-isEnabled"
    VALUE_13 = "-allowAnonymous"
    VALUE_15 = "-enableQuestions"
    VALUE_17 = "-createdAt"
    VALUE_19 = "-updatedAt"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-icon"
    VALUE_9 = "-modelPrompt"

    def __str__(self) -> str:
        return str(self.value)
