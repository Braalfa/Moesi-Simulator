from enum import Enum


class MessageType(Enum):
    READ_MISS = 0
    WRITE_MISS = 1
    WRITE_BACK = 2
    SHARED_RESPONSE = 3
    DATA_RESPONSE = 4
    REQUEST_FROM_MEMORY = 5


class Message:
    def __init__(self, message_type: MessageType, origin: int = None,
                 destination: int = None, address: int = None, data: str = None):
        self.message_type = message_type
        self.origin = origin
        self.destination = destination
        self.address = address
        self.data = data

    def __str__(self):
        string = str(self.message_type)
        if self.origin is not None:
            string += " origin:" + str(self.origin)
        if self.destination is not None:
            string += " destination:" + str(self.destination)
        if self.data is not None:
            string += " data:" + self.data
        if self.address is not None:
            string += " address:" + str(self.address)
        return string

