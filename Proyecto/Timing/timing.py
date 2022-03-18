import time


class Timing:
    def __init__(self, base_timing: float = 0.25):
        self.base_timing = base_timing
        self.execute_timing = self.base_timing
        self.memory_timing = self.base_timing*10
        self.cache_timing = self.base_timing*2
        self.max_bus_data_timing = self.memory_timing
        self.await_sharers_timing = self.memory_timing*1.5
        self.infinite_timing = 1000

    def cache_wait(self):
        time.sleep(self.cache_timing)

    def memory_wait(self):
        time.sleep(self.memory_timing)

    def execute_wait(self):
        time.sleep(self.execute_timing)
