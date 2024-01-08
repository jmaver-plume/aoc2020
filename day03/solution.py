from utilities.grid import Grid, Position


def parse():
    with open('input') as f:
        data = f.read()
    return Grid([list(line) for line in data.split('\n')])


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
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
