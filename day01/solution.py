def parse():
    with open('input') as f:
        data = f.read()
    numbers = [int(v) for v in data.split('\n')]
    return numbers


def p1():
    numbers = parse()
    set_of_numbers = set(numbers)
    for number in numbers:
        wanted = 2020 - number
        if wanted in set_of_numbers:
            return wanted * number


def p2():
    numbers = parse()
    map_of_partial_sums = {}
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            partial = numbers[i] + numbers[j]
            map_of_partial_sums[partial] = (numbers[i], numbers[j])

    for number in numbers:
        wanted = 2020 - number
        if wanted in map_of_partial_sums and number not in map_of_partial_sums[wanted]:
            a, b = map_of_partial_sums[wanted]
            return a * b * number


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
