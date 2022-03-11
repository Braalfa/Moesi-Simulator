from CPU.cpu import CPU
from Cache.cacheL1 import Cache
from mainMemory import MainMemory
from Communication.bus import Bus
from Cache.cacheController import CacheController


class Simulation:
    def __init__(self):
        self.number_of_cpus = 4
        self.main_memory = MainMemory()
        self.cache_controllers = []
        self.cpus = []

        for i in range(self.number_of_cpus):
            cache: Cache = Cache(i)
            cache_controller: CacheController = CacheController(cache)
            cpu = CPU(i, cache_controller)

            self.cache_controllers.append(cache_controller)
            self.cpus.append(cpu)

        self.bus = Bus(self.cache_controllers, self.main_memory)

    def execute(self):
        self.bus.start_execution()
        for cpu in self.cpus:
            cpu.start_execution()

