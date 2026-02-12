from enum import Enum


class ListKnowledgesSortingItem(str, Enum):
    ALLOWAISEARCH = "allowAiSearch"
    ALLOWKEYWORDSEXTRACTION = "allowKeywordsExtraction"
    CHUNKER = "chunker"
    CREATEDAT = "createdAt"
    DESCRIPTION = "description"
    ENABLED = "enabled"
    ID = "id"
    KEYWORDEXTRACTIONCUSTOMPROMPT = "keywordExtractionCustomPrompt"
    KEYWORDEXTRACTIONMAXKEYWORDS = "keywordExtractionMaxKeywords"
    KEYWORDEXTRACTIONMETHOD = "keywordExtractionMethod"
    NAME = "name"
    RATIONALRESOURCESCOUNT = "rationalResourcesCount"
    SYNCEDRESOURCESCOUNT = "syncedResourcesCount"
    TOUCHPOINTID = "touchpointId"
    UPDATEDAT = "updatedAt"
    VALUE_1 = "-id"
    VALUE_11 = "-allowKeywordsExtraction"
    VALUE_13 = "-keywordExtractionMethod"
    VALUE_15 = "-keywordExtractionCustomPrompt"
    VALUE_17 = "-keywordExtractionMaxKeywords"
    VALUE_19 = "-enabled"
    VALUE_21 = "-touchpointId"
    VALUE_23 = "-createdAt"
    VALUE_25 = "-updatedAt"
    VALUE_27 = "-syncedResourcesCount"
    VALUE_29 = "-rationalResourcesCount"
    VALUE_3 = "-name"
    VALUE_5 = "-description"
    VALUE_7 = "-chunker"
    VALUE_9 = "-allowAiSearch"

    def __str__(self) -> str:
        return str(self.value)
