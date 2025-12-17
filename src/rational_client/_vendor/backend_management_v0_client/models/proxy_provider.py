from enum import Enum


class ProxyProvider(str, Enum):
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    OPENAI = "openAI"
    OPENAICOMPATIBLE = "openAICompatible"
    OPENROUTER = "openRouter"
    RATIONALAI = "rationalAI"

    def __str__(self) -> str:
        return str(self.value)
