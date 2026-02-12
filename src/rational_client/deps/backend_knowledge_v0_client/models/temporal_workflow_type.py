from enum import Enum


class TemporalWorkflowType(str, Enum):
    RESOURCEPROCESS = "resourceProcess"
    SOURCESYNC = "sourceSync"

    def __str__(self) -> str:
        return str(self.value)
