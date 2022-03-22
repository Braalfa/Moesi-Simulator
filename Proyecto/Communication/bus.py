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
        self.acknowledgements = 0
        self.currentMessage: Message | None = None
        self.lock = threading.Lock()

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
        return thread

    def run(self):
        while self.execute_flag:
            for i in range(len(self.cache_controllers)):
                self.obtain_message_and_deliver(self.cache_controllers[i])
            self.obtain_message_and_deliver(self.main_memory)

    def obtain_message_and_deliver(self, source):
        message = source.return_next_send_message()
        self.deliver_message(message)

    def deliver_message(self, message: Message):
        for i in range(len(self.cache_controllers)):
            self.cache_controllers[i].receive_message_from_bus(message)
        self.main_memory.receive_message(message)
