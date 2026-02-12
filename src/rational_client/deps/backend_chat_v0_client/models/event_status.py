from enum import Enum


class EventStatus(str, Enum):
    ABORTED = "aborted"
    COMPLETED = "completed"
    ERROR = "error"
    INPROGRESS = "inProgress"

    def __str__(self) -> str:
        return str(self.value)
