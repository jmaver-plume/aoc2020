def parse():
    with open('input') as f:
        data = f.read()
    raw_groups = [group.split('\n') for group in data.split('\n\n')]

    groups = []
    for raw_group in raw_groups:
        persons = []
        for answers in raw_group:
            persons.append(Person(list(answers)))
        groups.append(Group(persons))
    return groups


class Person:
    def __init__(self, answers):
        self.answers = answers


class Group:
    def __init__(self, persons):
        self.persons = persons

    def count_unique_answers(self):
        answers = set()
        for person in self.persons:
            for answer in person.answers:
                answers.add(answer)
        return len(answers)

    def count_common_answers(self):
        answers = set()
        for answer in self.persons[0].answers:
            answers.add(answer)

        for person in self.persons[1:]:
            answers = answers.intersection(set(person.answers))

        return len(answers)


def p1():
    groups = parse()
    return sum([group.count_unique_answers() for group in groups])


def p2():
    groups = parse()
    return sum([group.count_common_answers() for group in groups])


def main():
    print(f'p2: {p1()}')
    print(f'p2: {p2()}')


main()
