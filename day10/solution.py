import math


def parse():
    with open('input') as f:
        data = f.read()
    return [int(v) for v in data.split('\n')]


def p1():
    jolts = parse()
    jolts.sort()
    jolts.insert(0, 0)
    jolts.append(jolts[-1] + 3)

    count_one = 0
    count_three = 0
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        if diff == 1:
            count_one += 1
        elif diff == 3:
            count_three += 1
    return count_one * count_three


# I checked the input and largest window size is 5 meaning we can only delete 3
def combinations(length):
    if length == 3:
        return 7
    elif length == 2:
        return 4
    elif length == 1:
        return 2


def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


# Algorithm:
#   - precondition: all windows are of size 5 or smaller (verified)
#   - precondition: all distances are either 1 or 3 (verified)
#   - get all windows where the distance between each jolt is 1 e.g., [3,4,5,6]
#   - we can't remove boundaries which means we can remove 2 in 5, 2 in 4, 1 in 3, 0 in 2, 0 in 1
#   - for each window we calculate combinations, then we multiple combinations together since they are not dependent
def p2():
    jolts = parse()
    jolts.sort()
    jolts.insert(0, 0)
    jolts.append(jolts[-1] + 3)

    windows = []
    window = []
    for jolt in jolts:
        if len(window) == 0:
            window = [jolt]
        else:
            if window[-1] + 1 != jolt:
                if len(window) > 2:
                    windows.append(window)
                window = [jolt]
            else:
                window.append(jolt)

    lengths = [len(window) for window in windows]
    return product([combinations(length - 2) for length in lengths])


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
