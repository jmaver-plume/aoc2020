def parse():
    with open('input') as f:
        data = f.read()
    raw_player_1, raw_player_2 = data.split('\n\n')
    player_1 = Player(1, list(map(int, raw_player_1.split('\n')[1:])))
    player_2 = Player(2, list(map(int, raw_player_2.split('\n')[1:])))
    return player_1, player_2


class Player:
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards

    def is_empty(self):
        return len(self.cards) == 0

    def pop(self):
        return self.cards.pop(0)

    def append(self, first, second):
        self.cards.append(first)
        self.cards.append(second)

    def score(self):
        return sum([c * (len(self.cards) - i) for i, c in enumerate(self.cards)])

    def get_hash(self):
        return hash(tuple(self.cards))


def play_regular_combat(player_1, player_2):
    while not player_1.is_empty() and not player_2.is_empty():
        player_1_card = player_1.pop()
        player_2_card = player_2.pop()
        if player_1_card > player_2_card:
            player_1.append(player_1_card, player_2_card)
        else:
            player_2.append(player_2_card, player_1_card)
    return player_2 if player_1.is_empty() else player_1


def play_recursive_combat(player_1, player_2, player_1_history, player_2_history):
    while not player_1.is_empty() and not player_2.is_empty():
        player_1_hash = player_1.get_hash()
        player_2_hash = player_2.get_hash()
        if player_1_hash in player_1_history and player_2_hash in player_2_history:
            return player_1
        else:
            player_1_history.add(player_1_hash)
            player_2_history.add(player_2_hash)

        player_1_card = player_1.pop()
        player_2_card = player_2.pop()
        if player_1_card > len(player_1.cards) or player_2_card > len(player_2.cards):
            # Regular combat
            if player_1_card > player_2_card:
                player_1.append(player_1_card, player_2_card)
            else:
                player_2.append(player_2_card, player_1_card)
        else:
            # Recursive combat
            new_player_1 = Player(player_1.id, player_1.cards[:player_1_card])
            new_player_2 = Player(player_2.id, player_2.cards[:player_2_card])
            winner = play_recursive_combat(new_player_1, new_player_2, set(), set())
            if winner.id == player_1.id:
                player_1.append(player_1_card, player_2_card)
            else:
                player_2.append(player_2_card, player_1_card)
    return player_2 if player_1.is_empty() else player_1


def p1():
    player_1, player_2 = parse()
    winner = play_regular_combat(player_1, player_2)
    return winner.score()


def p2():
    player_1, player_2 = parse()
    winner = play_recursive_combat(player_1, player_2, set(), set())
    return winner.score()


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
