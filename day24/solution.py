import math


def parse():
    def parse_line(line):
        tile = []
        i = 0
        while i < len(line):
            if line[i] == 's' or line[i] == 'n':
                tile.append(f'{line[i]}{line[i + 1]}')
                i += 2
            else:
                tile.append(line[i])
                i += 1
        return tile

    with open('input') as f:
        data = f.read()

    return [parse_line(line) for line in data.split('\n')]


def get_position(tile):
    x = 0
    y = 0
    for movement in tile:
        if movement == 'e':
            x -= 1
        elif movement == 'w':
            x += 1
        elif movement == 'se':
            x -= 0.5
            y -= 1
        elif movement == 'sw':
            x += 0.5
            y -= 1
        elif movement == 'ne':
            x -= 0.5
            y += 1
        elif movement == 'nw':
            x += 0.5
            y += 1
    return float(x), int(y)


def get_positions(tiles):
    positions = [get_position(tile) for tile in tiles]
    positions.sort(key=lambda x: x)
    return positions


def p1():
    tiles = parse()
    positions = get_positions(tiles)
    black_positions = set()
    for position in positions:
        black_positions.remove(position) if position in black_positions else black_positions.add(position)

    return len(black_positions)


def get_neighbours(position):
    x, y = position
    return (
        (x - 1, y),
        (x + 1, y),
        (x - 0.5, y + 1),
        (x + 0.5, y + 1),
        (x - 0.5, y - 1),
        (x + 0.5, y - 1),
    )


def p2():
    tiles = parse()
    positions = get_positions(tiles)

    # Compute black tiles
    black_positions = set()
    for position in positions:
        black_positions.remove(position) if position in black_positions else black_positions.add(position)

    for i in range(1, 101):
        min_x = min([t[0] for t in black_positions]) - 1
        max_x = max([t[0] for t in black_positions]) + 1
        min_y = min([t[1] for t in black_positions]) - 1
        max_y = max([t[1] for t in black_positions]) + 1
        new_black_positions = set()

        for y in (i for i in range(min_y, max_y + 1) if i % 2 == 0):
            # x is int when y is even
            for x in range(math.floor(min_x), math.ceil(max_x + 1)):
                position = (x, y)
                black_neighbours = len(
                    [neighbour for neighbour in get_neighbours(position) if neighbour in black_positions]
                )
                if position in black_positions and 0 < black_neighbours <= 2:
                    new_black_positions.add(position)
                elif position not in black_positions and black_neighbours == 2:
                    new_black_positions.add(position)

        # x is float when y is even so let's make min_x and max_x also float
        if math.ceil(min_x) == min_x:
            min_x -= 0.5
        if math.ceil(max_x) == max_x:
            max_x += 0.5
        for y in (i for i in range(min_y, max_y + 1) if i % 2 == 1):
            x = min_x
            while x <= max_x:
                position = (x, y)
                black_neighbours = len(
                    [neighbour for neighbour in get_neighbours(position) if neighbour in black_positions]
                )
                if position in black_positions and 0 < black_neighbours <= 2:
                    new_black_positions.add(position)
                elif position not in black_positions and black_neighbours == 2:
                    new_black_positions.add(position)
                x += 1

        black_positions = new_black_positions

    return len(black_positions)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
