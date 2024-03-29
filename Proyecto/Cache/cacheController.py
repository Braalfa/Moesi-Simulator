import threading
from enum import Enum
from threading import Lock

from Enums.cpuActionEnum import CPUAction
from Enums.stateEnum import State
from Cache.cacheL1 import CacheLine
from Cache.cacheL1 import Cache
from Communication.messaging import Message
from Communication.messaging import MessageType
import time
import logging
from Timing.timing import Timing
from CPU.instruction import InstructionType, Instruction


class CPUOperationStatus(Enum):
    FINISHED = 0
    PROCESSING = 1


class CacheController:
    def __init__(self, cache: Cache, logger: logging.Logger, timing: Timing):
        self.cache = cache
        self.unexpected_messages_queue = []
        self.data_messages_queue = []
        self.send_messages_queue = []
        self.logger = logger
        self.timing = timing
        self.messages_received = 0
        self.messages_accepted = 0
        self.output_data = None
        self.next_cpu_operation: Instruction | None = None
        self.most_recent_instruction: Instruction | None = None
        self.cpu_operation_lock = Lock()
        self.current_instruction_type: InstructionType | None = None
        self.execute_cache_flag = True
        self.status = "Idle"

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()

    def get_most_recent_instruction_as_string(self):
        if self.most_recent_instruction is not None:
            return self.most_recent_instruction.as_string_instruction()
        else:
            return ''

    def return_next_send_message(self):
        try:
            return self.send_messages_queue.pop(0)
        except IndexError:
            return None

    def run(self):
        while self.execute_cache_flag:
            self.process_cpu_operation()
            self.process_pending_messages()
            self.status = "Idle"

    def process_cpu_operation(self):
        self.cpu_operation_lock.acquire()
        if self.next_cpu_operation is not None:
            self.most_recent_instruction = self.next_cpu_operation
            self.status = "Running CPU Instruction"
            self.logger.info("Instruction on processor: " + str(
                self.cache.cache_number) + " instruction: " + self.next_cpu_operation.__str__())
            if self.next_cpu_operation.instruction_type == InstructionType.WRITE:
                self.write_request(self.next_cpu_operation.address, self.next_cpu_operation.value)
            elif self.next_cpu_operation.instruction_type == InstructionType.READ:
                self.output_data = self.read_request(self.next_cpu_operation.address)
            self.next_cpu_operation = None
        self.cpu_operation_lock.release()

    def process_pending_messages(self):
        while len(self.unexpected_messages_queue) > 0:
            self.status = "Processing Bus Messages"
            message = self.unexpected_messages_queue.pop(0)
            line = self.cache.obtain_line_by_address_and_acquire_lock(message.address)
            if line is not None:
                self.logger.info(
                    "Transitioning on skipped message : " + message.__str__() + " Line " + str(line.get_address()))
                self.transition_by_bus(message, line)
                line.release_lock()
            else:
                self.logger.info(
                    "Skipped, message was irrelevant message : " + message.__str__())

    def write_request(self, address: int, new_value: str):
        line, state = self.cache.obtain_line_and_state_and_acquire_lock(address)
        self.current_instruction_type = InstructionType.WRITE
        if state != State.I:
            state = line.get_state()
        self.transition_by_cpu(state, line, CPUAction.WRITE, address, new_value)
        self.current_instruction_type = None
        line.release_lock()

    def read_request(self, address: int):
        line, state = self.cache.obtain_line_and_state_and_acquire_lock(address)
        self.current_instruction_type = InstructionType.READ
        if state != State.I:
            state = line.get_state()
        data = self.transition_by_cpu(state, line, CPUAction.READ, address)
        self.current_instruction_type = None
        line.release_lock()
        return data

    def transition_by_cpu(self, current_state: State, line: CacheLine,
                          action: CPUAction, address: int, new_value: str = None):
        self.logger.info("Transition by cpu; current state: " + str(current_state))
        self.timing.cache_wait()
        if current_state == State.I:
            return self.transition_by_cpu_from_I(action, line, address, new_value)
        elif current_state == State.S:
            return self.transition_by_cpu_from_S(action, line, address, new_value)
        elif current_state == State.E:
            return self.transition_by_cpu_from_E(action, line, new_value)
        elif current_state == State.O:
            return self.transition_by_cpu_from_O(action, line, address, new_value)
        elif current_state == State.M:
            return self.transition_by_cpu_from_M(action, line, new_value)

    def transition_by_cpu_from_I(self, action: CPUAction, line: CacheLine, address: int, new_value: str = None):
        if action == CPUAction.READ:
            self.data_messages_queue = []
            self.broadcast_read_miss(address)
            message = self.read_cache_response_from_bus(address)
            if message is None:
                self.logger.info("No sharers found")
                self.data_messages_queue = []
                self.read_from_memory(address, line)
            else:
                self.logger.info("Data found")
                next_state = State.S
                self.overwrite_existing_line(line, address, message.data, next_state)
                self.remove_write_miss_messages(address, message.origin, message.data)
            return line.get_data()
        elif action == CPUAction.WRITE:
            self.broadcast_write_miss(address, new_value)
            next_state = State.M
            self.overwrite_existing_line(line, address, new_value, next_state)
        self.logger.info("Transition by cpu; next_state: " + str(next_state))

    def read_from_memory(self, address, line):
        self.ask_data_from_memory(address)
        data = self.read_memory_response_from_bus(address)
        next_state = State.E
        self.overwrite_existing_line(line, address, data, next_state)
        self.broadcast_invalidate_shared(address, data)

    def overwrite_existing_line(self, line: CacheLine, address: int, data: str, state: State):
        self.evict(line)
        line.set_state(state)
        line.set_address(address)
        line.set_data(data)

    def remove_write_miss_messages(self, address: int, origin: int, acceptable_value: str):
        no_removed_messages = []
        # Sleep to make sure messages arrive
        time.sleep(1)
        for i in range(len(self.unexpected_messages_queue)):
            message = self.unexpected_messages_queue[i]
            if message.message_type == MessageType.WRITE_MISS \
                    and message.address == address \
                    and message.origin == origin \
                    and message.data == acceptable_value:
                pass
            else:
                no_removed_messages.append(message)
        self.unexpected_messages_queue = no_removed_messages

    def transition_by_cpu_from_S(self, action: CPUAction, line: CacheLine, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.S
            line.set_state(next_state)
            return line.get_data()
        elif action == CPUAction.WRITE:
            self.broadcast_write_miss(address, new_value)
            next_state = State.M
            line.set_state(next_state)
            line.set_data(new_value)

        self.logger.info("Transition by cpu; next_state: " + str(next_state))

    def transition_by_cpu_from_E(self, action: CPUAction, line: CacheLine, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.E
            line.set_state(next_state)
            return line.get_data()
        elif action == CPUAction.WRITE:
            next_state = State.M
            line.set_state(next_state)
            line.set_data(new_value)

        self.logger.info("Transition by cpu; next_state: " + str(next_state))

    def transition_by_cpu_from_O(self, action: CPUAction, line: CacheLine, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.O
            line.set_state(next_state)
            return line.get_data()
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.broadcast_write_miss(address, new_value)
            line.set_state(next_state)
            line.set_data(new_value)

        self.logger.info("Transition by cpu; next_state: " + str(next_state))

    def transition_by_cpu_from_M(self, action: CPUAction, line: CacheLine, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.M
            line.set_state(next_state)
            return line.get_data()
        elif action == CPUAction.WRITE:
            next_state = State.M
            line.set_state(next_state)
            line.set_data(new_value)

        self.logger.info("Transition by cpu; next_state: " + str(next_state))

    def receive_message_from_bus(self, message: Message):
        if message is not None:
            thread = threading.Thread(target=self.process_message_from_bus, args=(message,))
            thread.start()

    def process_message_from_bus(self, message: Message):
        self.logger.info("Message received from bus; message:" + message.__str__())
        if message.origin == self.cache.cache_number:
            return
        message_preprocessed = False
        if message.message_type == MessageType.READ_MISS:
            message_preprocessed = self.try_to_preprocess_read_miss(message)
        if message_preprocessed:
            pass
        elif message.message_type == MessageType.READ_MISS \
                or message.message_type == MessageType.WRITE_MISS \
                or message.message_type == MessageType.INVALIDATE_SHARED:
            self.unexpected_messages_queue.append(message)
        elif message.message_type == MessageType.MEMORY_DATA_RESPONSE:
            self.data_messages_queue.append(message)
        elif message.message_type == MessageType.CACHE_DATA_RESPONSE \
                and message.destination == self.cache.cache_number:
            self.data_messages_queue.append(message)

    def try_to_preprocess_read_miss(self, message: Message) -> bool:
        line = self.cache.obtain_line_by_address_and_acquire_lock(message.address)
        processed = False
        if line is not None:
            if line.state in [State.E, State.O, State.M]:
                self.logger.info("Preprocessing read miss; message:" + message.__str__())
                self.transition_by_bus(message, line)
                processed = True
            line.release_lock()
        return processed

    def transition_by_bus(self, message: Message, line: CacheLine):
        self.timing.cache_wait()
        current_state = line.get_state()
        self.logger.info("Transition by bus ; current state: " + str(current_state) + " Message : " + message.__str__()
                         + " Address " + str(line.get_address()))
        if current_state == State.I:
            self.logger.info("Transition by bus; next_state: " + str(State.I))
            pass
        elif current_state == State.S:
            return self.transition_by_bus_from_S(message, line)
        elif current_state == State.E:
            return self.transition_by_bus_from_E(message, line)
        elif current_state == State.O:
            return self.transition_by_bus_from_O_and_M(message, line)
        elif current_state == State.M:
            return self.transition_by_bus_from_O_and_M(message, line)

    def transition_by_bus_from_S(self, message: Message, line: CacheLine):
        if message.message_type == MessageType.READ_MISS:
            next_state = State.S
            line.set_state(next_state)
            self.logger.info("Transition by bus; next_state: " + str(next_state))
        elif message.message_type == MessageType.WRITE_MISS\
                or message.message_type == MessageType.INVALIDATE_SHARED:
            next_state = State.I
            line.set_state(next_state)
            self.logger.info("Transition by bus; next_state: " + str(next_state))

    def transition_by_bus_from_E(self, message: Message, line: CacheLine):
        if message.message_type == MessageType.READ_MISS:
            next_state = State.S
            line.set_state(next_state)
            self.supply_data_to_bus(message.address, line.get_data(), message.origin)
            self.logger.info("Transition by bus; next_state: " + str(next_state))
        elif message.message_type == MessageType.WRITE_MISS:
            next_state = State.I
            line.set_state(next_state)
            self.logger.info("Transition by bus; next_state: " + str(next_state))

    def transition_by_bus_from_O_and_M(self, message: Message, line: CacheLine):
        if message.message_type == MessageType.READ_MISS:
            next_state = State.O
            line.set_state(next_state)
            self.supply_data_to_bus(message.address, line.get_data(), message.origin)
            self.logger.info("Transition by bus; next_state: " + str(next_state))
        elif message.message_type == MessageType.WRITE_MISS:
            next_state = State.I
            line.set_state(next_state)
            self.logger.info("Transition by bus; next_state: " + str(next_state))

    def evict(self, line: CacheLine):
        self.logger.info("Evicting; line number: " + str(line.line_number) + " address: " + str(line.address))
        current_state = line.state
        if current_state == State.I:
            line.set_state(State.I)
        elif current_state == State.S:
            line.set_state(State.I)
        elif current_state == State.E:
            line.set_state(State.I)
        elif current_state == State.O:
            self.ask_write_back(line.get_address(), line.get_data())
            line.set_state(State.I)
        elif current_state == State.M:
            self.ask_write_back(line.get_address(), line.get_data())
            line.set_state(State.I)

    def broadcast_read_miss(self, address: int):
        self.send_message_to_bus(MessageType.READ_MISS, address)

    def broadcast_write_miss(self, address: int, data: str):
        self.send_message_to_bus(MessageType.WRITE_MISS, address, data=data)

    def broadcast_invalidate_shared(self, address: int, data: str):
        self.send_message_to_bus(MessageType.INVALIDATE_SHARED, address, data=data)

    def ask_data_from_memory(self, address: int):
        self.timing.memory_wait()
        self.send_message_to_bus(MessageType.REQUEST_FROM_MEMORY, address)

    def ask_write_back(self, address: int, new_value: str):
        self.timing.memory_wait()
        self.send_message_to_bus(MessageType.WRITE_BACK, address, data=new_value)

    def supply_data_to_bus(self, address: int, data: str, destination: int):
        self.send_message_to_bus(MessageType.CACHE_DATA_RESPONSE, address, data=data, destination=destination)

    def read_cache_response_from_bus(self, address: int) -> Message | None:
        message = self.await_message_from_bus(MessageType.CACHE_DATA_RESPONSE,
                                              address, max_time=self.timing.max_bus_data_timing)
        if message is not None:
            return message
        else:
            # Try to read from recent memory load
            self.logger.info("No data was received from the caches")
            message = self.find_recent_load_from_memory(address)
            if message is not None:
                self.logger.info("Data was obtained from recent memory load")
                return message
            else:
                self.logger.info("The data couldn't be loaded")
                return None

    def read_memory_response_from_bus(self, address: int) -> str | None:
        message = self.await_message_from_bus(MessageType.MEMORY_DATA_RESPONSE,
                                              address, max_time=self.timing.infinite_timing)
        if message is not None:
            return message.data
        else:
            self.logger.error("The memory didn't respond")
            return None

    def await_message_from_bus(self, message_type: MessageType,
                               address: int, max_time: float = 10) -> Message | None:
        start = time.time()
        while time.time() - start < max_time:
            for i in range(len(self.data_messages_queue)):
                message = self.data_messages_queue[i]
                if message.message_type == message_type \
                        and message.address == address \
                        and message.destination == self.cache.cache_number:
                    self.data_messages_queue.pop(i)
                    return message
        return None

    def find_recent_load_from_memory(self, address):
        for i in range(len(self.data_messages_queue)):
            message = self.data_messages_queue[i]
            if message.message_type == MessageType.MEMORY_DATA_RESPONSE and message.address == address:
                self.data_messages_queue.pop(i)
                return message
        return None

    def are_there_sharers(self, address: int):
        message = self.await_message_from_bus(MessageType.SHARED_RESPONSE, address,
                                              max_time=self.timing.await_sharers_timing)
        if message is not None:
            return True
        else:
            return False

    def return_shared_to_bus(self, address: int, destination: int):
        self.send_message_to_bus(MessageType.SHARED_RESPONSE, address, destination=destination)

    def send_message_to_bus(self, message_type: MessageType, address: int, destination=None, data=None):
        message = Message(message_type, self.cache.cache_number, destination=destination, address=address, data=data)
        self.logger.info("Message sent to bus; message: " + message.__str__())
        self.send_messages_queue.append(message)
