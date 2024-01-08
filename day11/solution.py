from utilities.grid import Grid, Position


def parse():
    with open('input') as f:
        data = f.read()
    return Grid([list(line) for line in data.split('\n')])


def p1():
    grid = parse()
    temp = Grid.create(grid.height, grid.width)

    hashes = set()
    while True:
        for row in range(grid.height):
            for column in range(grid.width):
                position = Position(row, column)
                value = grid.get_value(position)
                neighbours = grid.neighbours(position, True)
                if value == '.':
                    continue
                elif value == 'L':
                    if all([grid.get_value(neighbour) != '#' for neighbour in neighbours]):
                        temp.set_value(position, '#')
                elif value == '#':
                    if len([neighbour for neighbour in neighbours if grid.get_value(neighbour) == '#']) >= 4:
                        temp.set_value(position, 'L')
        for row in range(temp.height):
            for column in range(temp.width):
                position = Position(row, column)
                value = temp.get_value(position)
                if value == '#' or value == 'L':
                    grid.set_value(position, value)
        temp.empty()
        hash = grid.hash()
        if hash in hashes:
            break
        else:
            hashes.add(hash)

    count = 0
    for row in range(grid.height):
        for column in range(grid.width):
            position = Position(row, column)
            value = grid.get_value(position)
            if value == '#':
                count += 1

    return count

def is_empty(value):
    return value == '.'

def p2():
    def get_seats(grid, position):
        row = position.row
        column = position.column
        seats = []

        while row != 0:
            candidate = Position(row - 1, column)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                row -= 1
        row = position.row

        while row != grid.height - 1:
            candidate = Position(row + 1, column)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                row += 1
        row = position.row

        while column != 0:
            candidate = Position(row, column - 1)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                column -= 1
        column = position.column

        while column != grid.width - 1:
            candidate = Position(row, column + 1)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                column += 1
        column = position.column

        # diagonals
        while row != 0 and column != 0:
            candidate = Position(row - 1, column - 1)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                row -= 1
                column -= 1
        row = position.row
        column = position.column

        while row != 0 and column != grid.width - 1:
            candidate = Position(row - 1, column + 1)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                row -= 1
                column += 1
        row = position.row
        column = position.column

        while row != grid.height - 1 and column != 0:
            candidate = Position(row + 1, column - 1)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                row += 1
                column -= 1
        row = position.row
        column = position.column

        while row != grid.height - 1 and column != grid.width - 1:
            candidate = Position(row + 1, column + 1)
            value = grid.get_value(candidate)
            if not is_empty(value):
                seats.append(candidate)
                break
            else:
                row += 1
                column += 1

        return seats

    grid = parse()
    temp = Grid.create(grid.height, grid.width)

    hashes = set()
    while True:
        for row in range(grid.height):
            for column in range(grid.width):
                position = Position(row, column)
                value = grid.get_value(position)
                seats = get_seats(grid, position)
                if value == '.':
                    continue
                elif value == 'L':
                    if all([grid.get_value(seat) != '#' for seat in seats]):
                        temp.set_value(position, '#')
                elif value == '#':
                    if len([seat for seat in seats if grid.get_value(seat) == '#']) >= 5:
                        temp.set_value(position, 'L')
        for row in range(temp.height):
            for column in range(temp.width):
                position = Position(row, column)
                value = temp.get_value(position)
                if value == '#' or value == 'L':
                    grid.set_value(position, value)
        temp.empty()
        hash = grid.hash()
        if hash in hashes:
            break
        else:
            hashes.add(hash)

    count = 0
    for row in range(grid.height):
        for column in range(grid.width):
            position = Position(row, column)
            value = grid.get_value(position)
            if value == '#':
                count += 1

    return count


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
