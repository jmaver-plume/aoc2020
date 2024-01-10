def parse():
    with open('input') as f:
        data = f.read()
    return [list(l.replace(' ', '')) for l in data.split('\n')]


def get_equation(items, start):
    parenthesis = 0
    for i in range(start, len(items)):
        if items[i] == '(':
            parenthesis += 1
        elif items[i] == ')':
            parenthesis -= 1
        if parenthesis == 0:
            end = i
            break
    return start, end, items[start + 1:end]


class EquationP1:
    def __init__(self):
        self.left = None
        self.operator = None
        self.right = None

    def push(self, value):
        if self.left is None:
            self.left = int(value)
        elif self.operator is None:
            self.operator = value
        else:
            self.right = int(value)
            self.solve()

    def solve(self):
        if self.operator == '+':
            self.left += self.right
        elif self.operator == '*':
            self.left *= self.right
        self.operator = None
        self.right = None


def solve_p1(items):
    equation = EquationP1()
    i = 0
    while i < len(items):
        if items[i] != '(':
            equation.push(items[i])
            i += 1
        else:
            start, end, partial = get_equation(items, i)
            equation.push(solve_p1(partial))
            i = end + 1
    return equation.left


class EquationP2:
    def __init__(self):
        self.items = []

    def push(self, value):
        if value == '*' or value == '+':
            self.items.append(value)
        else:
            self.items.append(int(value))

    def product(self, numbers):
        result = 1
        for number in numbers:
            result *= number
        return result

    def solve(self):
        while '+' in self.items:
            i = self.items.index('+')
            replacement = self.items[i - 1] + self.items[i + 1]
            self.items[i - 1:i + 2] = [replacement]
        return self.product([n for n in self.items if n != '*'])


def solve_p2(items):
    equation = EquationP2()
    i = 0
    while i < len(items):
        if items[i] != '(':
            equation.push(items[i])
            i += 1
        else:
            start, end, partial = get_equation(items, i)
            equation.push(solve_p2(partial))
            i = end + 1
    return equation.solve()


def p1():
    equations = parse()
    solutions = [solve_p1(equation) for equation in equations]
    return sum(solutions)


def p2():
    equations = parse()
    solutions = [solve_p2(equation) for equation in equations]
    return sum(solutions)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
