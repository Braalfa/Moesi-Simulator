import time
from random import randint
from Enums.stateEnum import State


class CacheLine:
    def __init__(self, block_number: int, state: State, address: int, data: str):
        self.block_number = block_number
        self.state = state
        self.address = address
        self.data = data

    def set_state(self, state: State):
        self.state = state

    def set_address(self, address: int):
        self.address = address

    def set_data(self, data: str):
        self.data = data

class Cache:
    def __init__(self, cache_number, delay_time: int = 1):
        self.cache_number = cache_number
        self.capacity = 8
        self.delay_time = delay_time
        self.memory = [
            CacheLine(i, State.I, 0, "0000") for i in range(self.capacity)
        ]

    def read(self, address: int):
        block = self.find_line_in_cache(address)
        return block.data

    def read_and_update_state(self, address: int, next_state: State):
        block = self.find_line_in_cache(address)
        block.set_state(next_state)
        return block.data

    def write(self, address: int, new_value: str, next_state: State):
        line = self.find_line_in_cache(address)
        line.set_data(new_value)
        line.set_state(next_state)

    def write_state(self, address: int, next_state: State):
        block = self.find_line_in_cache(address)
        block.set_state(next_state)

    def obtain_address_state(self, address: int):
        line = self.find_line_in_cache(address)
        if line is None:
            state = State.I
        else:
            state = line.state
        return state

    def select_block_to_overwrite(self, address: int):
        set_number = address % 2
        memory_by_set = [line for line in self.memory if line.block_number // 2 == set_number]
        memory_index = randint(0, 1)
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
