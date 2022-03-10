import time


class MainMemory:
    def __init__(self, delay_time: int = 10):
        self.capacity = 8
        self.delay_time = delay_time
        self.memory = ["0x0000" for _ in range(self.capacity)]

    def write(self, block_number: int, new_value: str):
        self.delay()
        if block_number < self.capacity:
            self.memory[block_number] = new_value

    def read(self, block_number: int) -> str:
        self.delay()
        if block_number < self.capacity:
            return self.memory[block_number]

    def obtain_content(self) -> []:
        return self.memory

    def delay(self):
        time.sleep(self.delay_time)
