from instructionGenerator import InstructionGenerator
from instruction import Instruction
from instruction import InstructionType
from Cache.cacheController import CacheController
import time
import threading


# TODO: The cpu executes the instructions and talks to the cache via the cache controller
class CPU:
    def __init__(self, processor_number: int, cache_controller: CacheController,
                 number_of_memory_blocks: int = 8, block_width_hexadecimal: int = 4,
                 calculation_time: int = 1):
        self.processor_number = processor_number
        self.cache_controller = cache_controller
        self.instructions_generator = InstructionGenerator(self.processor_number,
                                                           number_of_memory_blocks=number_of_memory_blocks,
                                                           block_width_hexadecimal=block_width_hexadecimal)
        self.calculation_time = calculation_time
        self.execute_flag = True

    def start_execution(self):
        thread = threading.Thread(target=self.run, args=())
        thread.start()
        return thread

    def run(self):
        while self.execute_flag:
            instruction = self.obtain_next_instruction()
            self.execute_instruction(instruction)

    def obtain_next_instruction(self) -> Instruction:
        next_instruction = self.instructions_generator.generate_instruction()
        return next_instruction

    def execute_instruction(self, instruction: Instruction):
        if instruction.instruction_type == InstructionType.CALC:
            self.execute_calculation()
        elif instruction.instruction_type == InstructionType.READ:
            self.execute_read(instruction.address)
        elif instruction.instruction_type == InstructionType.WRITE:
            self.execute_write(instruction.address)

    def execute_calculation(self):
        time.sleep(self.calculation_time)

    def execute_read(self, address: int):
        self.cache_controller.read_request(address)

    def execute_write(self, address: int, new_value: str):
        self.cache_controller.write_request(address, new_value)
