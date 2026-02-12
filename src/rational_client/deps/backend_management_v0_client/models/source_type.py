from enum import Enum


class SourceType(str, Enum):
    AWSS3 = "awsS3"
    AZUREBLOBSTORAGE = "azureBlobStorage"
    FILESYSTEM = "fileSystem"
    GOOGLECLOUDSTORAGE = "googleCloudStorage"
    GOOGLEDRIVE = "googleDrive"
    HTTP = "http"

    def __str__(self) -> str:
        return str(self.value)
