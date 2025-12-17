from enum import Enum


class SourceType(str, Enum):
    AWSS3 = "awsS3"
    FILESYSTEM = "fileSystem"
    GOOGLEDRIVE = "googleDrive"

    def __str__(self) -> str:
        return str(self.value)
