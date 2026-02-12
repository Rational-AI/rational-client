from enum import Enum


class DeploymentStatus(str, Enum):
    CREATING = "creating"
    FAILED = "failed"
    INITIALIZING = "initializing"
    READY = "ready"
    SCALEDTOZERO = "scaledToZero"
    SCALING = "scaling"
    TERMINATED = "terminated"
    TERMINATING = "terminating"
    WAITINGFORCHAT = "waitingForChat"

    def __str__(self) -> str:
        return str(self.value)
