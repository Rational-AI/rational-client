from enum import Enum


class ModelPurpose(str, Enum):
    EMBEDDING = "embedding"
    RERANKING = "reranking"
    TEXTGENERATION = "textGeneration"

    def __str__(self) -> str:
        return str(self.value)
