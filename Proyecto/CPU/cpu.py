from CPU.instructionGenerator import InstructionGenerator
from CPU.instruction import Instruction
from CPU.instruction import InstructionType
from Cache.cacheController import CacheController
import time
import threading
import logging


# TODO: The cpu executes the instructions and talks to the cache via the cache controller
class CPU:
    def __init__(self, processor_number: int, cache_controller: CacheController, logger: logging.Logger,
                 number_of_memory_blocks: int = 8, block_width_hexadecimal: int = 4,
                 calculation_time: int = 1):
        self.processor_number = processor_number
        self.cache_controller = cache_controller
        self.instructions_generator = InstructionGenerator(self.processor_number,
                                                           number_of_memory_blocks=number_of_memory_blocks,
                                                           block_width_hexadecimal=block_width_hexadecimal)
        self.calculation_time = calculation_time
        self.logger = logger
        self.most_recent_instruction = ""
        self.execute_continually = False
        self.execute_once = False
        self.next_instruction = None

    def stop_execution(self):
        self.execute_continually = False

    def execute_once(self):
        self.execute_once = True

    def set_next_instruction(self, next_instruction):
        self.next_instruction = next_instruction

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
        return thread

    def run(self):
        while self.should_execute():
            self.logger.info("Running on processor " + str(self.processor_number))
            instruction = self.obtain_next_instruction()
            self.logger.info("Instruction on processor: " + str(self.processor_number) + " instruction: " + instruction.__str__())
            self.update_most_recent_instruction(instruction)
            self.execute_instruction(instruction)

    def should_execute(self):
        if self.execute_continually:
            return True
        elif self.execute_once:
            self.execute_once = False
            return True
        else:
            return False

    def update_most_recent_instruction(self, instruction):
        self.most_recent_instruction = instruction

    def obtain_next_instruction(self) -> Instruction:
        if self.next_instruction is not None:
            next_instruction = self.instructions_generator.generate_instruction()
        else:
            next_instruction = self.next_instruction
            self.next_instruction = None
        return next_instruction

    def execute_instruction(self, instruction: Instruction):
        if instruction.instruction_type == InstructionType.CALC:
            self.execute_calculation()
        elif instruction.instruction_type == InstructionType.READ:
            self.execute_read(instruction.address)
        elif instruction.instruction_type == InstructionType.WRITE:
            self.execute_write(instruction.address, instruction.value)

    def execute_calculation(self):
        time.sleep(self.calculation_time)

    def execute_read(self, address: int):
        self.cache_controller.read_request(address)

    def execute_write(self, address: int, new_value: str):
        self.cache_controller.write_request(address, new_value)
