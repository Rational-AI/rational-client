from enum import Enum


class AnnotationType(str, Enum):
    CHUNK = "chunk"
    COMMENT = "comment"
    FREETEXT = "freeText"
    IMAGE = "image"
    PATH = "path"
    SHAPE = "shape"
    TABLE = "table"
    TEXTMARKUP = "textMarkup"

    def __str__(self) -> str:
        return str(self.value)
