from enum import Enum


class GetKnowledgeV0KnowledgeKnowledgeIdKnowledgeSyncJobSortingItem(str, Enum):
    COMPLETEDAT = "completedAt"
    CREATEDAT = "createdAt"
    ID = "id"
    KNOWLEDGEID = "knowledgeId"
    LASTERROR = "lastError"
    TEMPORALRUNID = "temporalRunId"
    TEMPORALWORKFLOWID = "temporalWorkflowId"
    TRIES = "tries"
    VALUE_1 = "-id"
    VALUE_11 = "-workflowStatus"
    VALUE_13 = "-lastError"
    VALUE_15 = "-tries"
    VALUE_17 = "-createdAt"
    VALUE_19 = "-completedAt"
    VALUE_3 = "-knowledgeId"
    VALUE_5 = "-temporalWorkflowId"
    VALUE_7 = "-temporalRunId"
    VALUE_9 = "-workflowType"
    WORKFLOWSTATUS = "workflowStatus"
    WORKFLOWTYPE = "workflowType"

    def __str__(self) -> str:
        return str(self.value)
