from enum import Enum


class TemporalWorkflowStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    INPROGRESS = "inProgress"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
