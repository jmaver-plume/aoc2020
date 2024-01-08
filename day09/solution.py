from queue import Queue


def parse():
    with open('input') as f:
        data = f.read()
    return [int(value) for value in data.split('\n')]


def find_number(numbers):
    window_size = 25
    window_numbers = set()
    window = Queue(maxsize=window_size)
    for number in numbers[:window_size]:
        window.put_nowait(number)
        window_numbers.add(number)

    for number in numbers[window_size:]:
        exists = False
        for window_number in window_numbers:
            if number - window_number in window_numbers:
                exists = True
                break
        if not exists:
            return number
        window_numbers.remove(window.get_nowait())
        window.put_nowait(number)
        window_numbers.add(number)


def p1():
    numbers = parse()
    return find_number(numbers)


def p2():
    numbers = parse()
    number = find_number(numbers)
    index = numbers.index(number)
    # Sliding window
    start = 0
    end = 1
    while end < index:
        window = numbers[start:end+1]
        window_sum = sum(window)
        if window_sum == number:
            return min(window) + max(window)
        elif window_sum > number:
            start += 1
        elif window_sum < number:
            end += 1


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
