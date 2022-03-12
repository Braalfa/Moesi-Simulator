from CPU.cpu import CPU
from Cache.cacheL1 import Cache
from mainMemory import MainMemory
from Communication.bus import Bus
from Cache.cacheController import CacheController
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

    def execute(self):
        self.bus.start_execution()
        for cpu in self.cpus:
            cpu.start_execution()

