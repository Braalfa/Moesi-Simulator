from CPU.instructionGenerator import InstructionGenerator
from CPU.instruction import Instruction
from CPU.instruction import InstructionType
from Cache.cacheController import CacheController, CPUOperationStatus
import time
import threading
import logging
from Timing.timing import Timing


# TODO: The cpu executes the instructions and talks to the cache via the cache controller
class CPU:
    def __init__(self, processor_number: int, cache_controller: CacheController, logger: logging.Logger, timing: Timing,
                 number_of_memory_blocks: int = 8, block_width_hexadecimal: int = 4,
                 calculation_time: int = 1):
        self.processor_number = processor_number
        self.cache_controller = cache_controller
        self.instructions_generator = InstructionGenerator(self.processor_number,
                                                           number_of_memory_blocks=number_of_memory_blocks,
                                                           block_width_hexadecimal=block_width_hexadecimal)
        self.calculation_time = calculation_time
        self.logger = logger
        self.timing = timing
        self.execute_continually = False
        self.execute_once = False
        self.next_instruction = None
        self.continue_working = True
        self.current_status = "Waiting"

    def stop_execution(self):
        self.execute_continually = False

    def step_execution(self):
        self.execute_once = True

    def continue_execution(self):
        self.execute_continually = True

    def set_next_instruction(self, next_instruction):
        self.next_instruction = next_instruction

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
        return thread

    def run(self):
        while self.continue_working:
            if self.should_execute():
                self.current_status = "Running"
                instruction = self.obtain_next_instruction()
                self.execute_instruction(instruction)
            else:
                self.current_status = "Waiting"

    def should_execute(self):
        if self.execute_continually:
            return True
        elif self.execute_once:
            self.execute_once = False
            return True
        else:
            return False

    def obtain_next_instruction(self) -> Instruction:
        if self.next_instruction is None:
            next_instruction = self.instructions_generator.generate_instruction()
        else:
            next_instruction = self.next_instruction
            self.next_instruction = None
        return next_instruction

    def execute_instruction(self, instruction: Instruction):
        if instruction.instruction_type == InstructionType.CALC:
            self.execute_calculation()
        else:
            self.assign_next_operation_to_cache(instruction)

    def assign_next_operation_to_cache(self, instruction: Instruction):
        while self.cache_controller.next_cpu_operation is not None:
            pass
        self.cache_controller.cpu_operation_lock.acquire()
        self.cache_controller.next_cpu_operation = instruction
        self.cache_controller.cpu_operation_lock.release()

    def execute_calculation(self):
        self.timing.execute_wait()

    def execute_read(self, address: int):
        self.timing.execute_wait()
        self.cache_controller.read_request(address)

    def execute_write(self, address: int, new_value: str):
        self.timing.execute_wait()
        self.cache_controller.write_request(address, new_value)

        