def parse():
    with open('input') as f:
        data = f.read()
    return Grid([list(line) for line in data.split('\n')])


class GridIterator:
    def __init__(self, grid):
        self._grid = grid
        self._current_row = 0
        self._current_column = 0

    def __next__(self):
        if self._current_row >= self._grid.height:
            raise StopIteration

        value = self._grid.data[self._current_row][self._current_column]
        self._current_column += 1
        if self._current_column >= self._grid.width:
            self._current_column = 0
            self._current_row += 1

        return self._current_row, self._current_column, value


class Grid:
    def __init__(self, data):
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    def __iter__(self):
        return GridIterator(self)

    def get_value(self, position):
        return self.data[position.row][position.column]


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def clone(self):
        return Position(self.row, self.column)


def count_trees(grid, d_row, d_column):
    count = 0
    position = Position(0, 0)
    while position.row < grid.height:
        is_tree = grid.get_value(position) == '#'
        if is_tree:
            count += 1
        position.row += d_row
        position.column = (position.column + d_column) % grid.width
    return count


def p1():
    grid = parse()
    return count_trees(grid, 1, 3)


def p2():
    grid = parse()
    first = count_trees(grid, 1, 1)
    second = count_trees(grid, 1, 3)
    third = count_trees(grid, 1, 5)
    fourth = count_trees(grid, 1, 7)
    fifth = count_trees(grid, 2, 1)
    return first * second * third * fourth * fifth


def main():
    print(f'p2: {p1()}')
    print(f'p2: {p2()}')


main()
