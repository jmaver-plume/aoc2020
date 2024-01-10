from tqdm import tqdm

def parse():
    with open('input') as f:
        data = f.read()
    return [int(v) for v in data.split(',')]


class Window:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def push(self, value):
        if self.first is None:
            self.first = value
        elif self.last is None:
            self.last = value
        else:
            self.first = self.last
            self.last = value

    def is_full(self):
        return self.first is not None and self.last is not None


class Game:
    def __init__(self, starting_numbers):
        self.starting_numbers = starting_numbers
        self.map = {}

    def play(self, number_of_turns):
        for i in range(number_of_turns):
            if i < len(self.starting_numbers):
                last = self.starting_numbers[i]
                self.map[last] = Window(i)
            else:
                next = self.map[last].last - self.map[last].first if self.map[last].is_full() else 0
                if next in self.map:
                    self.map[next].push(i)
                else:
                    self.map[next] = Window(i)
                last = next
        return last


def p1():
    return Game(parse()).play(2020)


def p2():
    return Game(parse()).play(30000000)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
