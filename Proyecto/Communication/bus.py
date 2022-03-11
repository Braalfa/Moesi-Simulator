from Communication.messaging import Message
from Communication.messaging import MessageType
from mainMemory import MainMemory


# TODO: READ MESSAGES FROM THE CACHES
class Bus:
    def __init__(self, caches, main_memory: MainMemory):
        self.queue = []
        self.caches = caches
        self.main_memory = main_memory

    def add_message(self, message: Message):
        self.queue.append(message)

    def process_next_message(self):
        message = self.queue.pop(0)
        if message.message_type == MessageType.REQUEST_FROM_MEMORY:
            self.deliver_data_from_memory(message)
        elif message.message_type == MessageType.WRITE_BACK:
            self.main_memory.write(message.address, message.data)
        else:
            self.deliver_message_to_caches(message)

    def deliver_data_from_memory(self, incoming_message):
        data = self.main_memory.read(incoming_message.address)
        response_message = Message(MessageType.DATA_RESPONSE,
                                   destination=incoming_message.origin,
                                   address=incoming_message.address,
                                   data=data)
        self.deliver_message_to_caches(response_message)

    def deliver_message_to_caches(self, message: Message):
        cache_destinations = self.obtain_cache_destinations(message)
        for cache_destination in cache_destinations:
            cache_destination.receive_message_from_bus(message)

    def obtain_cache_destinations(self, message: Message):
        if message.message_type == MessageType.READ_MISS \
                or message.message_type == MessageType.WRITE_MISS \
                or message.message_type == MessageType.WRITE_MISS_2:
            cache_destinations = [cache for cache in self.caches]
        else:
            cache_destinations = self.caches[message.destination]
        return cache_destinations
