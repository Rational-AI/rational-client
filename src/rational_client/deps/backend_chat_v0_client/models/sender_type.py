from enum import Enum


class SenderType(str, Enum):
    AGENT = "agent"
    OPERATOR = "operator"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
