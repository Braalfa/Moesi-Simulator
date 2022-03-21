import logging
from Communication.messaging import Message
from Communication.messaging import MessageType
from mainMemory import MainMemory
from Cache.cacheController import CacheController
import threading


class Bus:
    def __init__(self, cache_controllers: [CacheController], main_memory: MainMemory, logger: logging.Logger):
        self.queue = []
        self.cache_controllers = cache_controllers
        self.main_memory = main_memory
        self.execute_flag = True
        self.logger = logger

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
            return
        if message.message_type == MessageType.REQUEST_FROM_MEMORY \
                or message.message_type == MessageType.WRITE_BACK:
            self.deliver_message_to_memory(message)
        else:
            self.deliver_message_to_caches(message)

    def obtain_messages(self):
        message = self.main_memory.return_next_send_messages()
        while message is not None:
            self.add_message_to_queue(message)
            message = self.main_memory.return_next_send_messages()
        for cache_controller in self.cache_controllers:
            message = cache_controller.return_next_send_message()
            self.add_message_to_queue(message)

    def add_message_to_queue(self, message):
        if message is not None:
            self.queue.append(message)

    def get_next_message(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            return None

    def deliver_message_to_memory(self, message):
        self.main_memory.receive_message(message)

    def deliver_message_to_caches(self, message: Message):
        cache_destinations = self.obtain_cache_destinations(message)
        for cache_destination in cache_destinations:
            thread = threading.Thread(target=cache_destination.receive_message_from_bus, args=(message,))
            thread.start()
            self.logger.info("Sent message to cache: " + str(cache_destination.cache.cache_number)
                             + " message: " + message.__str__())

    def obtain_cache_destinations(self, message: Message):
        if message.message_type == MessageType.READ_MISS \
                or message.message_type == MessageType.WRITE_MISS\
                or message.message_type == MessageType.MEMORY_DATA_RESPONSE:
            cache_destinations = [cache_controller for cache_controller in self.cache_controllers
                                  if cache_controller.cache.cache_number != message.origin]
        else:
            cache_destinations = [self.cache_controllers[message.destination]]
        return cache_destinations
