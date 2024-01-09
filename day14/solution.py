import math
import re
from itertools import product


def parse():
    with open('input') as f:
        data = f.read()
    instructions = []
    lines = data.split('\n')
    for line in lines:
        if line.startswith('mask'):
            mask = re.match(r"mask = (.*)", line).groups()[0]
            instructions.append(MaskInstruction(mask))
        else:
            address, value = re.match(r"mem\[(\d+)] = (\d+)", line).groups()
            instructions.append(MemoryInstruction(int(address), int(value)))
    return instructions


class MaskInstruction:
    def __init__(self, mask):
        self.mask = mask


class MemoryInstruction:
    def __init__(self, address, value):
        self.address = address
        self.value = value


def to_decimal(binary):
    return int(binary, 2)


def to_binary(decimal):
    return format(decimal, '036b')


def p1():
    memory = {}
    for instruction in parse():
        if isinstance(instruction, MaskInstruction):
            mask = instruction.mask
        else:
            memory[instruction.address] = to_decimal(''.join([b if m == 'X' else m for b, m in zip(to_binary(instruction.value), mask)]))
    return sum(memory.values())


def p2():
    def generate_combinations(mask, address):
        result = ''.join([b if m == '0' else m for b, m in zip(address, mask)])
        num_x = result.count('X')
        replacements = product('01', repeat=num_x)
        combinations = []
        for replacement in replacements:
            temp_s = result
            for r in replacement:
                temp_s = temp_s.replace('X', r, 1)
            combinations.append(temp_s)
        return combinations

    memory = {}
    for instruction in parse():
        if isinstance(instruction, MaskInstruction):
            mask = instruction.mask
        else:
            addresses = generate_combinations(mask, to_binary(instruction.address))
            for address in addresses:
                memory[to_decimal(address)] = instruction.value

    return sum(memory.values())


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
