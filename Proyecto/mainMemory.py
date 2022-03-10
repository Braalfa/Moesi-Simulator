import time


class MainMemory:
    def __init__(self, delay_time: int = 10):
        self.capacity = 8
        self.delay_time = delay_time
        self.memory = ["0x0000" for _ in range(self.capacity)]

    def write(self, address: int, new_value: str):
        self.delay()
        if address < self.capacity:
            self.memory[address] = new_value

    def read(self, address: int) -> str:
        self.delay()
        if address < self.capacity:
            return self.memory[address]

    def obtain_content(self) -> []:
        return self.memory

    def delay(self):
        time.sleep(self.delay_time)
