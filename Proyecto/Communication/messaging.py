from enum import Enum


class MessageType(Enum):
    READ_MISS = 0
    WRITE_MISS = 1
    WRITE_MISS_2 = 2
    WRITE_BACK = 3
    SHARED_RESPONSE = 4
    DATA_RESPONSE = 5
    REQUEST_FROM_MEMORY = 6


class Message:
    def __init__(self, message_type: MessageType, origin: int = None,
                 destination: int = None, address: int = None, data: str = None):
        self.message_type = message_type
        self.origin = origin
        self.destination = destination
        self.address = address
        self.data = data
