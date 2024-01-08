import math

from utilities.grid import Grid, Position


def parse():
    with open('input') as f:
        data = f.read()
    return [list(line) for line in data.split('\n')]


def get_row(seat):
    left = 0
    right = 127
    for char in seat[:7]:
        if char == 'F':
            right = math.floor((right + left) / 2)
        elif char == 'B':
            left = math.ceil((right + left) / 2)
    return left


def get_column(seat):
    left = 0
    right = 7
    for char in seat[7:]:
        if char == 'L':
            right = math.floor((right + left) / 2)
        elif char == 'R':
            left = math.ceil((right + left) / 2)
    return left


def get_position(seat):
    row = get_row(seat)
    column = get_column(seat)
    return Position(row, column)


def get_id(position):
    return position.row * 8 + position.column


def p1():
    seats = parse()
    return max([get_id(get_position(seat)) for seat in seats])


def p2():
    seats = parse()

    grid = Grid.create(128, 8)
    for seat in seats:
        position = get_position(seat)
        grid.set_value(position, 1)

    for i in range(128):
        row = grid.get_row(i)
        if row.count(0) == 1:
            position = Position(i, row.index(0))
            return get_id(position)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
