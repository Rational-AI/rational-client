from enum import Enum


class ExtensionChannelType(str, Enum):
    NONE = "none"
    OPENAIAPI = "openAIApi"
    RATIONALAI = "rationalAI"
    TELEGRAM = "telegram"

    def __str__(self) -> str:
        return str(self.value)
