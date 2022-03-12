from enum import Enum


class InstructionType(Enum):
    CALC = 0
    READ = 1
    WRITE = 2


class Instruction:
    def __init__(self, instruction_type: InstructionType,
                 processor_number: int, address: int = None, value: str = None):
        self.instruction_type = instruction_type
        self.processor_number = processor_number
        self.address = address
        self.value = value

    def __str__(self):
        string = "P" + str(self.processor_number)
        string += " instruction type: " + str(self.instruction_type)
        if self.instruction_type == InstructionType.CALC:
            pass
        elif self.instruction_type == InstructionType.READ:
            string += " address: " + str(self.address)
        elif self.instruction_type == InstructionType.WRITE:
            string += " address: " + str(self.address)
            string += " value: " + self.value
        return string
