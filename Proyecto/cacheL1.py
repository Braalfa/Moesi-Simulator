import time
from enum import Enum
from random import randint
from messaging import Message
from messaging import MessageType


class CPUAction(Enum):
    READ = 0
    WRITE = 1


class State(Enum):
    M = 0
    O = 1
    E = 2
    S = 3
    I = 4


class CacheLine:
    def __init__(self, block_number: int, state: State, address: int, data: str):
        self.block_number = block_number
        self.state = state
        self.address = address
        self.data = data


class Cache:
    def __init__(self, cache_number, delay_time: int = 1):
        self.cache_number = cache_number
        self.capacity = 8
        self.delay_time = delay_time
        self.memory = [
            CacheLine(i, State.I, 0, "0000") for i in range(self.capacity)
        ]
        self.received_messages_queue = []
        self.send_messages_queue = []

    def write_request(self, address: int, new_value: str):
        state = self.obtain_address_state(address)
        self.transition_by_cpu(state, CPUAction.WRITE, address, new_value)

    def read_request(self, address):
        state = self.obtain_address_state(address)
        data = self.transition_by_cpu(state, CPUAction.READ, address)
        return data

    def transition_by_cpu(self, currentState: State,
                          action: CPUAction, address: int, new_value: str = None):
        if currentState == State.I:
            return self.transition_from_I(action, address, new_value)
        elif currentState == State.S:
            return self.transition_from_S(action, address, new_value)
        elif currentState == State.E:
            return self.transition_from_E(action, address, new_value)
        elif currentState == State.O:
            return self.transition_from_O(action, address, new_value)
        elif currentState == State.M:
            return self.transition_from_M(action, address, new_value)

    def transition_from_I(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            block = self.select_block_to_overwrite(address)
            self.broadcast_read_miss(address)
            sharers_found = self.are_there_sharers(address)
            if not sharers_found:
                self.ask_data_from_memory(address)
                self.obtain_data_and_overwrite_existing_block(block, address)
                block.state = State.E
            else:
                self.obtain_data_and_overwrite_existing_block(block, address)
                block.state = State.S
            return block.data
        elif action == CPUAction.WRITE:
            self.broadcast_write_miss(address)
            next_state = State.M
            self.write_to_cache(address, new_value, next_state)

    def transition_from_S(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.S
            return self.read_from_cache(address, next_state)
        elif action == CPUAction.WRITE:
            self.broadcast_write_miss_2(address)
            next_state = State.M
            self.write_to_cache(address, new_value, next_state)

    def transition_from_E(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.E
            return self.read_from_cache(address, next_state)
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.write_to_cache(address, new_value, next_state)

    def transition_from_O(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.O
            return self.read_from_cache(address, next_state)
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.broadcast_write_miss_2(address)
            self.write_to_cache(address, new_value, next_state)

    def transition_from_M(self, action: CPUAction, address: int, new_value: str = None):
        if action == CPUAction.READ:
            next_state = State.M
            return self.read_from_cache(address, next_state)
        elif action == CPUAction.WRITE:
            next_state = State.M
            self.write_to_cache(address, new_value, next_state)

    def read_from_cache(self, address, next_state):
        block = self.find_line_in_cache(address)
        block.state = next_state
        return block.data

    def write_to_cache(self, address: int, new_value: str, next_state):
        self.delay()
        line = self.find_line_in_cache(address)
        line.data = new_value
        line.state = next_state

    def broadcast_read_miss(self, address: int):
        self.send_message_to_bus(MessageType.READ_MISS, address)

    def broadcast_write_miss(self, address: int):
        self.send_message_to_bus(MessageType.WRITE_MISS, address)

    def broadcast_write_miss_2(self, address: int):
        self.send_message_to_bus(MessageType.WRITE_MISS_2, address)

    def ask_data_from_memory(self, address: int):
        self.send_message_to_bus(MessageType.REQUEST_FROM_MEMORY, address)

    def receive_message_from_bus(self, message: Message):
        self.received_messages_queue.append(message)

    def are_there_sharers(self, address: int):
        message = self.await_message_from_bus(MessageType.SHARED_RESPONSE, address)
        if message is not None:
            return True
        else:
            return False

    def obtain_data_and_overwrite_existing_block(self, block: CacheLine, address: int):
        data = self.read_data_from_bus(address)
        self.overwrite_block(data, address, block)

    def read_data_from_bus(self, address: int):
        message = self.await_message_from_bus(MessageType.DATA_RESPONSE, address)
        return message.data

    # TODO: Adjust time
    def await_message_from_bus(self, message_type: MessageType,
                               address: int, max_time: int = 10000) -> Message | None:
        start = time.time()
        while time.time() - start < max_time:
            for i in range(len(self.received_messages_queue)):
                message = self.received_messages_queue[i]
                if message.message_type == message_type and message.address == address:
                    self.received_messages_queue.pop(i)
                    return message
        return None

    def send_message_to_bus(self, message_type: MessageType, address: int, destinations=None, data=None):
        message = Message(message_type, self.cache_number, destinations, address, data)
        self.send_messages_queue.append(message)

    def obtain_address_state(self, address):
        line = self.find_line_in_cache(address)
        if line is None:
            state = State.I
        else:
            state = line.state
        return state

    def overwrite_block(self, data: str, address: int, line_to_overwrite: CacheLine):
        line_to_overwrite.address = address
        line_to_overwrite.data = data

    def select_block_to_overwrite(self, address: int):
        set_number = address % 2
        memory_by_set = [line for line in self.memory if line.block_number // 2 == set_number]
        memory_index = randint(0, 2)
        selected_block = memory_by_set[memory_index]
        return selected_block

    def find_line_in_cache(self, address: int):
        filtered_memory = [line for line in self.memory if line.address == address]
        if len(filtered_memory) > 0:
            return filtered_memory[0]
        else:
            return None

    def obtain_content(self) -> []:
        return self.memory

    def delay(self):
        time.sleep(self.delay_time)
