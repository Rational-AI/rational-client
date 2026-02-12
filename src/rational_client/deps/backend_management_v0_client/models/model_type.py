from enum import Enum


class ModelType(str, Enum):
    AWQ = "awq"
    BASE = "base"
    GGML = "ggml"
    GGUF = "gguf"

    def __str__(self) -> str:
        return str(self.value)
