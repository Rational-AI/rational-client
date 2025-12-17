from enum import Enum


class ModelArchitecture(str, Enum):
    BERT = "bert"
    BGE = "bge"
    DEEPSEEK = "deepSeek"
    E5 = "e5"
    GEMMA3 = "gemma3"
    GTE = "gte"
    INSTRUCTOR = "instructor"
    JINA = "jina"
    LLAMA = "llama"
    MISTRAL = "mistral"
    NOMIC = "nomic"
    PHI = "phi"
    QWEN = "qwen"
    QWENEMBEDDING = "qwenEmbedding"
    SENTENCETRANSFORMERS = "sentenceTransformers"

    def __str__(self) -> str:
        return str(self.value)
