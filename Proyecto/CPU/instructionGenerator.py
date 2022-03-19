import random

import numpy as np
import math
from CPU.instruction import InstructionType
from CPU.instruction import Instruction
import scipy.integrate as integrate


class NormalDistribution:
    def __init__(self, mean=0, standard_deviation=1, linspace_range=1.5):
        self.mean = mean
        self.standard_deviation = standard_deviation
        self.linspace_range = linspace_range
        self.f = self.obtain_inverse_function()

    def obtain_probability_density(self, value):
        denominator = (2 * math.pi * self.standard_deviation ** 2) ** .5
        numerator = math.exp(-(float(value) - float(self.mean)) ** 2 / (2 * self.standard_deviation ** 2))
        return numerator / denominator

    def cumulative_distribution(self, value):
        return integrate.quad(self.obtain_probability_density, float('-inf'), value)

    def obtain_inverse_function(self):
        function = [(self.cumulative_distribution(val)[0], val) for val in
                    np.linspace(-self.linspace_range, self.linspace_range, 200)]
        return function

    def obtain_single_sample(self, probability):
        if probability < self.f[0][0]:
            return self.f[0][1]
        elif probability > self.f[-1][0]:
            return self.f[-1][1]
        for f_item in self.f:
            if probability < f_item[0]:
                return f_item[1]

    def obtain_samples(self, quantity):
        return [self.obtain_single_sample(random.random()) for _ in range(quantity)]

    def obtain_number(self, minimum: int, maximum: int):
        sample = self.obtain_samples(1)[0]
        sample += self.linspace_range
        number = sample*(maximum-minimum+0.98)/(2*self.linspace_range) + minimum-0.49
        return round(number)

    def number_probability(self, number, minimum, maximum):
        small = (number-0.49 - (minimum-0.49))*(2*1.5)/(maximum-minimum+0.98)-1.5
        big = (number+0.49 - (minimum - 0.49)) * (2 * 1.5) / (maximum - minimum +0.98) - 1.5
        return integrate.quad(self.obtain_probability_density, small, big)[0]

# TODO: Replace the random generators
class InstructionGenerator:
    def __init__(self, processor_number: int,
                 number_of_memory_blocks: int = 8, block_width_hexadecimal: int = 4):
        self.processor_number = processor_number
        self.operations = [InstructionType.CALC, InstructionType.READ, InstructionType.WRITE]
        self.number_of_operations = len(self.operations)
        self.block_width_hexadecimal = block_width_hexadecimal
        self.blocks_bits = math.ceil(math.log(number_of_memory_blocks, 2))
        self.normal_distribution = NormalDistribution()

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
        if self.processor_number == 0:
            instruction = Instruction(InstructionType.READ, self.processor_number, 0, None)
        elif self.processor_number == 1:
            instruction = Instruction(InstructionType.WRITE, self.processor_number, 0, "abcd")
        else:
            instruction = Instruction(operation, self.processor_number, address, value)
        return instruction

    def select_instruction(self) -> InstructionType:
        sample = self.normal_distribution.obtain_number(0, self.number_of_operations-1)
        operation_index = sample
        return self.operations[operation_index]

    def select_address(self) -> int:
        sample = self.normal_distribution.obtain_number(0, 2 ** self.blocks_bits-1)
        address = sample
        return address

    def select_new_value(self) -> str:
        sample = [self.normal_distribution.obtain_number(0, 15) for _ in range(self.block_width_hexadecimal)]
        value = ''.join([hex(int(i))[2:] for i in sample])
        return value
sle