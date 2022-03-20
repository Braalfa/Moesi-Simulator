import time
from enum import Enum
from random import randint
from threading import Lock

from Enums.stateEnum import State
from Timing.timing import Timing


class CacheLine:
    def __init__(self, line_number: int, state: State, address: int, data: str):
        self.line_number = line_number
        self.state = state
        self.address = address
        self.data = data
        self.lock = Lock()

    def is_locked(self):
        self.lock.locked()

    def acquire_lock(self):
        self.lock.acquire()

    def release_lock(self):
        self.lock.release()

    def set_state(self, state: State):
        self.state = state

    def set_address(self, address: int):
        self.address = address

    def set_data(self, data: str):
        self.data = data

    def get_state(self) -> State:
        return self.state

    def get_address(self) -> int:
        return self.address

    def get_data(self) -> str:
        return self.data

    def get_state_as_string(self):
        return self.state.name

    def get_address_as_3_bits(self) -> str:
        binary_string = bin(self.address)
        binary_string_3_bits = ''.join(['0' for i in range(3 - len(binary_string[2:]))]) + binary_string[2:]
        return binary_string_3_bits


class Cache:
    def __init__(self, cache_number):
        self.cache_number = cache_number
        self.capacity = 4
        self.memory = [
            CacheLine(i, State.I, 0, "0000") for i in range(self.capacity)
        ]

    def read(self, address: int):
        line = self.find_line_in_cache(address)
        return line.data

    def read_and_update_state(self, address: int, next_state: State):
        line = self.find_line_in_cache(address)
        line.set_state(next_state)
        return line.data

    def write(self, address: int, new_value: str, next_state: State):
        line = self.find_line_in_cache(address)
        line.set_data(new_value)
        line.set_state(next_state)

    def write_state(self, address: int, next_state: State):
        line = self.find_line_in_cache(address)
        line.set_state(next_state)

    def obtain_line_and_state(self, address) -> (CacheLine, State):
        line = self.obtain_line_by_address(address)
        if line is None:
            line = self.select_line_to_overwrite(address)
            state = State.I
        else:
            state = line.get_state()
        return line, state

    def obtain_line_by_address(self, address: int):
        line = self.find_line_in_cache(address)
        return line

    def obtain_line_by_address_and_acquire_lock(self, address: int):
        line = self.find_line_in_cache_and_acquire_lock(address)
        return line

    def select_line_to_overwrite(self, address: int):
        set_number = address % 2
        memory_by_set = [line for line in self.memory if line.line_number // 2 == set_number]
        if memory_by_set[0].state == State.I:
            memory_index = 0
        elif memory_by_set[1].state == State.I:
            memory_index = 1
        else:
            memory_index = randint(0, 1)
        selected_line = memory_by_set[memory_index]
        return selected_line

    def find_line_in_cache(self, address: int):
        filtered_memory = [line for line in self.memory if line.address == address]
        if len(filtered_memory) > 0:
            return filtered_memory[0]
        else:
            return None

    def find_line_in_cache_and_acquire_lock(self, address: int):
        for line in self.memory:
            line.acquire_lock()
            if line.address == address:
                return line
            else:
                line.release_lock()
        return None

    def obtain_content(self) -> []:
        return self.memory