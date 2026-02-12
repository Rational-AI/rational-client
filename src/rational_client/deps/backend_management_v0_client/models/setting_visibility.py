from enum import Enum


class SettingVisibility(str, Enum):
    GLOBAL = "global"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
