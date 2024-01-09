import math


def parse():
    with open('input') as f:
        data = f.read()
    return [Movement(line[0], int(line[1:])) for line in data.split('\n')]


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def log(self):
        x_name = 'west' if self.x > 0 else 'east'
        y_name = 'north' if self.y > 0 else 'south'
        print(f'{x_name} {abs(self.x)}, {y_name} {abs(self.y)}')


class Movement:
    def __init__(self, action, amount):
        self.action = action
        self.amount = amount


class Ship:
    def __init__(self):
        self.position = Position(0, 0)
        self.direction = 'E'


def move_ship_p1(ship, movement):
    def rotate(angle):
        directions = ('N', 'E', 'S', 'W')
        index = directions.index(ship.direction)
        rotations = int(angle / 90)
        for i in range(rotations):
            if index == 0:
                index = 3
            else:
                index -= 1
        ship.direction = directions[index]

    if movement.action == 'N':
        ship.position.y += movement.amount
    elif movement.action == 'S':
        ship.position.y -= movement.amount
    elif movement.action == 'E':
        ship.position.x -= movement.amount
    elif movement.action == 'W':
        ship.position.x += movement.amount
    elif movement.action == 'L':
        return rotate(movement.amount)
    elif movement.action == 'R':
        return rotate(360 - movement.amount)
    elif movement.action == 'F':
        if ship.direction == 'N':
            ship.position.y += movement.amount
        elif ship.direction == 'S':
            ship.position.y -= movement.amount
        elif ship.direction == 'E':
            ship.position.x -= movement.amount
        elif ship.direction == 'W':
            ship.position.x += movement.amount


def move_ship_p2(ship, waypoint, movement):
    ship.position.y += (waypoint.position.y * movement.amount)
    ship.position.x += (waypoint.position.x * movement.amount)


class Waypoint:
    def __init__(self, position):
        self.position = position


def move_waypoint(waypoint, movement):
    def rotate(angle):
        radians = math.radians(angle)
        new_x = round(math.cos(radians) * waypoint.position.x - math.sin(radians) * waypoint.position.y)
        new_y = round(math.sin(radians) * waypoint.position.x + math.cos(radians) * waypoint.position.y)
        waypoint.position.x = new_x
        waypoint.position.y = new_y

    if movement.action == 'N':
        waypoint.position.y += movement.amount
    elif movement.action == 'S':
        waypoint.position.y -= movement.amount
    elif movement.action == 'E':
        waypoint.position.x -= movement.amount
    elif movement.action == 'W':
        waypoint.position.x += movement.amount
    elif movement.action == 'L':
        rotate(360 - movement.amount)
    elif movement.action == 'R':
        rotate(movement.amount)


def p1():
    movements = parse()
    ship = Ship()
    for movement in movements:
        move_ship_p1(ship, movement)
    return abs(ship.position.y) + abs(ship.position.x)


def p2():
    movements = parse()
    ship = Ship()
    waypoint = Waypoint(Position(-10, 1))
    for movement in movements:
        if movement.action == 'F':
            move_ship_p2(ship, waypoint, movement)
        else:
            move_waypoint(waypoint, movement)

    return abs(ship.position.y) + abs(ship.position.x)


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
