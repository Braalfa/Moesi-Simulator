import numpy as np
import math


# TODO: Replace the random generators
class InstructionGenerator:
    def __init__(self, number_of_processors: int = 4,
                 number_of_memory_blocks: int = 8, block_width_hexadecimal: int = 4):
        self.operations = ["CALC", "WRITE", "READ"]
        self.number_of_operations = len(self.operations)
        self.block_width_hexadecimal = block_width_hexadecimal
        self.number_of_processors = number_of_processors
        self.blocks_bits = math.ceil(math.log(number_of_memory_blocks, 2))

    def generate_instruction(self) -> str:
        operation = self.select_instruction()
        processor = self.select_processor()
        if operation == "CALC":
            instruction = processor + " " + operation
        elif operation == "READ":
            address = self.select_address()
            instruction = processor + " " + operation + " " + address
        elif operation == "WRITE":
            address = self.select_address()
            value = self.select_new_value()
            instruction = processor + " " + operation + " " + address + " " + value
        else:
            instruction = ""
        return instruction

    def select_instruction(self) -> str:
        sample = np.random.uniform(low=0, high=self.number_of_operations)
        operation_index = int(sample)
        return self.operations[operation_index]

    def select_address(self) -> str:
        sample = np.random.uniform(low=0, high=2, size=self.blocks_bits)
        address = ''.join([str(int(i)) for i in sample])
        return address

    def select_new_value(self) -> str:
        sample = np.random.uniform(low=0, high=16, size=self.block_width_hexadecimal)
        value = ''.join([hex(int(i))[2:] for i in sample])
        return value

    def select_processor(self) -> str:
        sample = np.random.uniform(low=0, high=self.number_of_processors)
        processor_number = int(sample)
        return "P"+str(processor_number)
