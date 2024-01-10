def parse_p1():
    with open('input') as f:
        data = f.read()
    grid = [list(line) for line in data.split('\n')]

    active = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.':
                continue
            active.add((x, y, 0))
    return active


def parse_p2():
    with open('input') as f:
        data = f.read()
    grid = [list(line) for line in data.split('\n')]

    active = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.':
                continue
            active.add((x, y, 0, 0))
    return active


def get_neighbours_p1(position):
    x, y, z = position
    neighbours = set()
    for i_x in range(-1, 2):
        for i_y in range(-1, 2):
            for i_z in range(-1, 2):
                if i_x == 0 and i_y == 0 and i_z == 0:
                    continue
                neighbours.add((x + i_x, y + i_y, z + i_z))
    return neighbours


def get_neighbours_p2(position):
    x, y, z, w = position
    neighbours = set()
    for i_x in range(-1, 2):
        for i_y in range(-1, 2):
            for i_z in range(-1, 2):
                for i_w in range(-1, 2):
                    if i_x == 0 and i_y == 0 and i_z == 0 and i_w == 0:
                        continue
                    neighbours.add((x + i_x, y + i_y, z + i_z, w + i_w))
    return neighbours


def cycle(active_cubes, get_neighbours):
    new_active = set()
    all_neighbours = set().union(*[get_neighbours(cube) for cube in active_cubes])
    for cube in all_neighbours:
        neighbours = get_neighbours(cube)
        if cube in active_cubes:
            active_neighbours = [n for n in neighbours if n in active_cubes]
            if len(active_neighbours) == 2 or len(active_neighbours) == 3:
                new_active.add(cube)
        else:
            active_neighbours = [n for n in neighbours if n in active_cubes]
            if len(active_neighbours) == 3:
                new_active.add(cube)

    return new_active


def p1():
    active = parse_p1()
    for i in range(6):
        active = cycle(active, get_neighbours_p1)
    return len(active)


def p2():
    active = parse_p2()
    for i in range(6):
        active = cycle(active, get_neighbours_p2)
    return len(active)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
