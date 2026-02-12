from enum import Enum


class KeywordExtractionMethod(str, Enum):
    LLM = "llm"
    RULEBASED = "ruleBased"

    def __str__(self) -> str:
        return str(self.value)
