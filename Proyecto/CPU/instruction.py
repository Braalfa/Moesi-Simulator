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

    @staticmethod
    def parse_from_string(instruction_string: str) -> any:
        instruction_components = instruction_string.split(" ")
        iterator = iter(instruction_components)

        processor_string = next(iterator)
        processor_number = int(processor_string[2:])
        instruction_type_string = next(iterator)
        instruction_type = InstructionType[instruction_type_string]

        instruction = None
        if instruction_type == InstructionType.CALC:
            instruction = Instruction(instruction_type, processor_number)
        elif instruction_type == InstructionType.READ:
            address_string = next(iterator)
            address = Instruction.parse_address(address_string)
            instruction = Instruction(instruction_type, processor_number, address=address)
        elif instruction_type == InstructionType.WRITE:
            address_string = next(iterator)
            address = Instruction.parse_address(address_string)
            value = next(iterator)
            instruction = Instruction(instruction_type, processor_number, address=address, value=value)
        return instruction

    @staticmethod
    def parse_address(address_string: str) -> int:
        address = int(address_string, 2)
        return address

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
