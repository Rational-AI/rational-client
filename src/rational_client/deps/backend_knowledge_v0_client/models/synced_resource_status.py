from enum import Enum


class SyncedResourceStatus(str, Enum):
    ERROR = "error"
    PENDING = "pending"
    PROCESSED = "processed"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
