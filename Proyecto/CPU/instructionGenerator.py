import numpy as np
import math
from CPU.instruction import InstructionType
from CPU.instruction import Instruction


# TODO: Replace the random generators
class InstructionGenerator:
    def __init__(self, processor_number: int,
                 number_of_memory_blocks: int = 8, block_width_hexadecimal: int = 4):
        self.processor_number = processor_number
        self.operations = [InstructionType.CALC, InstructionType.READ, InstructionType.WRITE]
        self.number_of_operations = len(self.operations)
        self.block_width_hexadecimal = block_width_hexadecimal
        self.blocks_bits = math.ceil(math.log(number_of_memory_blocks, 2))

    def generate_instruction(self) -> Instruction:
        operation = self.select_instruction()
        address: int | None = None
        value: str | None = None
        if operation == InstructionType.CALC:
            pass
        elif operation == InstructionType.READ:
            address = self.select_address()
        elif operation == InstructionType.WRITE:
            address = self.select_address()
            value = self.select_new_value()
        instruction = Instruction(operation, self.processor_number, address, value)
        return instruction

    def select_instruction(self) -> InstructionType:
        sample = np.random.uniform(low=0, high=self.number_of_operations)
        operation_index = 2
        return self.operations[operation_index]

    def select_address(self) -> int:
        sample = np.random.uniform(low=0, high=2**self.blocks_bits)
        address = 0
        return address

    def select_new_value(self) -> str:
        sample = np.random.uniform(low=0, high=16, size=self.block_width_hexadecimal)
        value = ''.join([hex(int(i))[2:] for i in sample])
        return value
