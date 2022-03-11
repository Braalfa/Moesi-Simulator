import time
from random import randint
from Enums.stateEnum import State


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

    def read_from_cache(self, address, next_state):
        block = self.find_line_in_cache(address)
        block.state = next_state
        return block.data

    def write_to_cache(self, address: int, new_value: str, next_state):
        self.delay()
        line = self.find_line_in_cache(address)
        line.data = new_value
        line.state = next_state

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
