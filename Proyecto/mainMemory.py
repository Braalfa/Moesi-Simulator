import threading
import time

from Communication.bus import Bus
from Communication.messaging import Message, MessageType
from Timing.timing import Timing


class MainMemory:
    def __init__(self, timing: Timing, bus: Bus, delay_time: int = 2):
        self.capacity = 8
        self.timing = timing
        self.delay_time = delay_time
        self.memory = ["0000" for _ in range(self.capacity)]
        self.send_messages_queue = []
        self.received_messages_queue = []
        self.run_flag = True
        self.bus = bus

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
        thread = threading.Thread(target=self.send_bus_message_loop, args=())
        thread.start()

    def receive_message_from_bus(self, message: Message):
        self.received_messages_queue.append(message)

    def send_bus_message_loop(self):
        while self.run_flag:
            if len(self.send_messages_queue) > 0:
                message = self.send_messages_queue.pop(0)
                self.bus.send_message(message)

    def run(self):
        while self.run_flag:
            if len(self.received_messages_queue) > 0:
                message: Message = self.received_messages_queue.pop(0)
                if message.message_type == MessageType.WRITE_BACK:
                    self.handle_data_write(message)
                elif message.message_type == MessageType.REQUEST_FROM_MEMORY:
                    self.handle_data_read(message)

    def handle_data_write(self, message: Message):
        self.write(message.address, message.data)

    def handle_data_read(self, message: Message):
        data = self.read(message.address)
        response_message = Message(MessageType.MEMORY_DATA_RESPONSE,
                                   destination=message.origin,
                                   address=message.address,
                                   data=data)
        self.send_messages_queue.append(response_message)

    def receive_message(self, message: Message):
        self.received_messages_queue.append(message)

    def return_next_send_messages(self):
        if len(self.send_messages_queue) > 0:
            return self.send_messages_queue.pop(0)
        else:
            return None

    def write(self, address: int, new_value: str):
        self.timing.memory_wait()
        if address < self.capacity:
            self.memory[address] = new_value

    def read(self, address: int) -> str:
        self.timing.memory_wait()
        if address < self.capacity:
            return self.memory[address]

    def obtain_content(self) -> []:
        return self.memory
