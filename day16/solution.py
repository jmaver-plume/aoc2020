import re


def parse():
    def parse_interval(raw):
        return tuple(map(int, re.match(r"(\d+)-(\d+)", raw).groups()))

    with open('input') as f:
        data = f.read()
    raw_rules, raw_your_ticket, raw_nearby_tickets = data.split('\n\n')
    rules = []
    for raw_rule in raw_rules.split('\n'):
        groups = re.match(r"(.*): (.*) or (.*)", raw_rule).groups()
        rules.append((groups[0], parse_interval(groups[1]), parse_interval(groups[2])))
    your_ticket = [int(v) for v in raw_your_ticket.split('\n')[1].split(',')]
    nearby_tickets = [tuple(list(map(int, lines.split(',')))) for lines in raw_nearby_tickets.split('\n')[1:]]
    return rules, your_ticket, nearby_tickets


def in_interval(value, interval):
    return interval[0] <= value <= interval[1]


def is_valid_value(value, rules):
    return any([is_valid_value_for_rule(value, rule) for rule in rules])


def is_valid_value_for_rule(value, rule):
    return in_interval(value, rule[1]) or in_interval(value, rule[2])


def is_valid_ticket(ticket, rules):
    for value in ticket:
        if not is_valid_value(value, rules):
            return False, value
    return True, None


def get_valid_rules(value, rules):
    return set([rule for rule in rules if is_valid_value_for_rule(value, rule)])


def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def p1():
    rules, your_ticket, nearby_tickets = parse()
    not_in = []
    for ticket in nearby_tickets:
        is_valid, value = is_valid_ticket(ticket, rules)
        if not is_valid:
            not_in.append(value)
    return sum(not_in)


def p2():
    rules, your_ticket, nearby_tickets = parse()
    valid_nearby_tickets = set([ticket for ticket in nearby_tickets if is_valid_ticket(ticket, rules)[0]])

    size = len(nearby_tickets[0])
    positions = [None for i in range(size)]
    while len(rules) != 0:
        for i in range(size):
            valid_rules = set.intersection(*[get_valid_rules(ticket[i], rules) for ticket in valid_nearby_tickets])
            if len(valid_rules) == 1:
                positions[i] = list(valid_rules)[0]
                rules.remove(list(valid_rules)[0])

    return product([your_ticket[i] for i in range(size) if positions[i][0].startswith('departure')])


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
