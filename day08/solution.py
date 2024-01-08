def parse():
    with open('input') as f:
        data = f.read()
    lines = data.split('\n')
    instructions = []
    for line in lines:
        operation, argument = line.split(' ')
        instructions.append(Instruction(operation, int(argument)))
    return instructions


class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument

def run(instructions):
    visited = set()
    accumulator = 0
    index = 0
    while True:
        if index in visited:
            return accumulator, False
        visited.add(index)
        if index >= len(instructions):
            return accumulator, True
        instruction = instructions[index]
        if instruction.operation == 'nop':
            index += 1
        elif instruction.operation == 'acc':
            accumulator += instruction.argument
            index += 1
        else:
            index += instruction.argument


def p1():
    instructions = parse()
    return run(instructions)


def p2():
    instructions = parse()
    for instruction in instructions:
        old = instruction.operation
        if old == 'nop':
            instruction.operation = 'jmp'
        elif old == 'jmp':
            instruction.operation = 'nop'
        else:
            continue

        accumulator, terminated = run(instructions)
        if terminated:
            return accumulator
        instruction.operation = old


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
