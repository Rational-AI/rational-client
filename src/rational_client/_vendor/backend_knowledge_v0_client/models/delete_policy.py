from enum import Enum


class DeletePolicy(str, Enum):
    DELETE = "delete"
    KEEP = "keep"

    def __str__(self) -> str:
        return str(self.value)
