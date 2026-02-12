from enum import Enum


class AssigneeType(str, Enum):
    AGENT = "agent"
    NONE = "none"
    OPERATOR = "operator"

    def __str__(self) -> str:
        return str(self.value)
