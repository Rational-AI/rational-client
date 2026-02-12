from enum import Enum


class OverrideDiscriminator(str, Enum):
    CLEAR = "clear"
    DEFAULT = "default"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
