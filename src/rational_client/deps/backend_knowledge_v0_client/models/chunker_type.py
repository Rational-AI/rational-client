from enum import Enum


class ChunkerType(str, Enum):
    SDPMCHUNKER = "sdpmChunker"
    SEMANTICCHUNKER = "semanticChunker"
    SENTENCECHUNKER = "sentenceChunker"
    TOKENCHUNKER = "tokenChunker"

    def __str__(self) -> str:
        return str(self.value)
