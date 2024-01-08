import re


def parse():
    with open('input') as f:
        data = f.read()
    lines = data.split('\n')
    parsed_lines = []
    for line in lines:
        raw_policy, raw_password = line.split(':')
        raw_min, raw_max, value = re.split('[- ]', raw_policy)
        policy = Policy(int(raw_min), int(raw_max), value)
        password = raw_password.strip()
        parsed_lines.append(Line(policy, password))
    return parsed_lines


class Line:
    def __init__(self, policy, password):
        self.policy = policy
        self.password = password

    def is_valid_p1(self):
        count = 0
        for element in self.password:
            if element == self.policy.value:
                count += 1
        return self.policy.min <= count <= self.policy.max

    def is_valid_p2(self):
        first = self.password[self.policy.min - 1]
        second = self.password[self.policy.max - 1]
        if first == second:
            return False

        if first == self.policy.value or second == self.policy.value:
            return True

        return False


class Policy:
    def __init__(self, min, max, value):
        self.min = min
        self.max = max
        self.value = value


def p1():
    lines = parse()
    valid = [line for line in lines if line.is_valid_p1()]
    return len(valid)


def p2():
    lines = parse()
    valid = [line for line in lines if line.is_valid_p2()]
    return len(valid)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
