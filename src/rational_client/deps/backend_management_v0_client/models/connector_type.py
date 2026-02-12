from enum import Enum


class ConnectorType(str, Enum):
    ANTHROPIC = "anthropic"
    AWS = "aws"
    AZURECLIENTCREDENTIALS = "azureClientCredentials"
    BRAVEAPIKEY = "braveApiKey"
    GOOGLE = "google"
    GOOGLESERVICEACCOUNTKEY = "googleServiceAccountKey"
    OPENAI = "openAI"
    OPENAICOMPATIBLE = "openAICompatible"
    OPENROUTER = "openRouter"
    RATIONAL = "rational"

    def __str__(self) -> str:
        return str(self.value)
