import time
from Timing.timing import Timing


class MainMemory:
    def __init__(self, timing: Timing, delay_time: int = 2):
        self.capacity = 8
        self.timing = timing
        self.delay_time = delay_time
        self.memory = ["0000" for _ in range(self.capacity)]

    def write(self, address: int, new_value: str):
        if address < self.capacity:
            self.memory[address] = new_value

    def read(self, address: int) -> str:
        if address < self.capacity:
            return self.memory[address]

    def obtain_content(self) -> []:
        return self.memory
