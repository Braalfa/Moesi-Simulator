from Communication.messaging import Message
from Communication.messaging import MessageType
from mainMemory import MainMemory
from Cache.cacheController import CacheController
import threading


class Bus:
    def __init__(self, cache_controllers: [CacheController], main_memory: MainMemory):
        self.queue = []
        self.cache_controllers = cache_controllers
        self.main_memory = main_memory
        self.execute_flag = True

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
        return thread

    def run(self):
        while self.execute_flag:
            self.obtain_messages()
            self.process_next_message()

    def process_next_message(self):
        message = self.get_next_message()
        if message is None:
            pass
        elif message.message_type == MessageType.REQUEST_FROM_MEMORY:
            self.deliver_data_from_memory(message)
        elif message.message_type == MessageType.WRITE_BACK:
            self.main_memory.write(message.address, message.data)
        else:
            self.deliver_message_to_caches(message)

    def obtain_messages(self):
        for cache_controller in self.cache_controllers:
            message = cache_controller.return_next_send_message()
            if message is not None:
                self.add_message(message)

    def add_message(self, message: Message):
        self.queue.append(message)

    def get_next_message(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            return None

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
                or message.message_type == MessageType.WRITE_MISS:
            cache_destinations = [cache for cache in self.cache_controllers]
        else:
            cache_destinations = self.cache_controllers[message.destination]
        return cache_destinations
