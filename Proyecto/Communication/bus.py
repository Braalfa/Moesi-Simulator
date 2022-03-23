import logging
import time

from Communication.messaging import Message
from Communication.messaging import MessageType
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

    def get_current_message(self):
        return self.currentMessage

    def acknowledge_message(self):
        self.acknowledgements += 1

    def send_message(self, message: Message):
        self.queue_l += 1
        self.lock.acquire()
        self.currentMessage = message
        while self.acknowledgements < 5:
            pass
        self.acknowledgements = 0
        self.queue_l -= 1
        print(self.queue_l)
        self.lock.release()
