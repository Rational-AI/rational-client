from enum import Enum


class EventType(str, Enum):
    CUSTOMTYPE = "customType"
    EXITROOM = "exitRoom"
    FEEDBACK = "feedback"
    MESSAGE = "message"
    SENTIMENT = "sentiment"
    SETCONTEXT = "setContext"
    TITLE = "title"
    TOOLREQUEST = "toolRequest"
    TOOLRESPONSE = "toolResponse"
    TOPIC = "topic"

    def __str__(self) -> str:
        return str(self.value)
