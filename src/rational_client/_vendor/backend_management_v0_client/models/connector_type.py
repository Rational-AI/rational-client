from enum import Enum


class ConnectorType(str, Enum):
    ANTHROPIC = "anthropic"
    AWS = "aws"
    GOOGLE = "google"
    OPENAI = "openAI"
    OPENAICOMPATIBLE = "openAICompatible"
    OPENROUTER = "openRouter"

    def __str__(self) -> str:
        return str(self.value)
