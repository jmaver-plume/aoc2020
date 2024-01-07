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

    def get_row(self, row):
        return self.data[row]

    def get_value(self, position):
        return self.data[position.row][position.column]

    def set_value(self, position, value):
        self.data[position.row][position.column] = value

    @staticmethod
    def create(height, width):
        data = []
        for row in range(height):
            row_list = []
            for column in range(width):
                row_list.append(0)
            data.append(row_list)
        return Grid(data)


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def clone(self):
        return Position(self.row, self.column)