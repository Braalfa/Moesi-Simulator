from CPU.cpu import CPU
from Cache.cacheL1 import Cache, CacheLine
from mainMemory import MainMemory
from Communication.bus import Bus
from Cache.cacheController import CacheController
from CPU.instruction import Instruction
import logging

import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


class Simulation:
    def __init__(self):
        self.number_of_cpus = 4
        self.main_memory = MainMemory()
        self.cache_controllers = []
        self.cpus = []

        for i in range(self.number_of_cpus):
            logger = setup_logger(str(i) + "_logger", str(i) + '.log')

            cache: Cache = Cache(i)
            cache_controller: CacheController = CacheController(cache, logger)
            cpu = CPU(i, cache_controller, logger)

            self.cache_controllers.append(cache_controller)
            self.cpus.append(cpu)

        logger = setup_logger("bus_logger",  'bus.log')

        self.bus = Bus(self.cache_controllers, self.main_memory, logger)

    def get_memory_content(self) -> []:
        return self.main_memory.memory

    def get_cache_content(self, cache_number: int) -> [CacheLine]:
        return self.cache_controllers[cache_number].cache.obtain_content()

    def get_cache_status(self, cache_number: int) -> str:
        return self.cache_controllers[cache_number].current_process

    def get_cpu_instruction(self, cpu_number: int) -> Instruction:
        return self.cpus[cpu_number].most_recent_instruction

    def cpu_set_instruction(self, cpu_number: int, next_instruction: Instruction):
        self.cpus[cpu_number].set_next_instruction(next_instruction)

    def start_execution(self):
        for cpu in self.cpus:
            cpu.start_execution()

    def stop_execution(self):
        for cpu in self.cpus:
            cpu.stop_execution()

    def execute_once(self):
        for cpu in self.cpus:
            cpu.execute_once()

    def execute(self):
        self.bus.start_execution()
        for cpu in self.cpus:
            cpu.start_execution()

