from enum import Enum


class ChannelMode(str, Enum):
    AUTOMATIC = "automatic"
    DRAFT = "draft"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
