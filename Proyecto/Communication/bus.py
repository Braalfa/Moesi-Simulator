import logging

from Communication.messaging import Message
import threading


class Bus:
    def __init__(self, logger: logging.Logger):
        self.queue = []
        self.execute_flag = True
        self.logger = logger
        self.acknowledgements = 0
        self.currentMessage: Message | None = None
        self.lock = threading.Lock()
        self.queue_l = 0
        self.cache_controllers = None
        self.main_memory = None

    def initialize_environment(self, cache_controllers, main_memory):
        self.cache_controllers = cache_controllers
        self.main_memory = main_memory

    def send_message(self, message: Message):
        self.queue_l += 1
        for cache_controller in self.cache_controllers:
            cache_controller.receive_message_from_bus(message)
        self.main_memory.receive_message_from_bus(message)
        self.queue_l -= 1
        print(self.queue_l)
