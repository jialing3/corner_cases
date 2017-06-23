#!/usr/local/bin/python3
'''
solve via simulation
food for thoughts: would markov chain work?
'''

from random import shuffle, seed, randint
import numpy as np

squares = list(map(lambda x: str(x).zfill(2), range(40)))
squares[0] = 'GO'
squares[2] = 'CC1'
squares[5] = 'R1'
squares[7] = 'CH1'
squares[10] = 'JAIL'
squares[11] = 'C1'
squares[12] = 'U1'
squares[15] = 'R2'
squares[17] = 'CC2'
squares[22] = 'CH2'
squares[24] = 'E3'
squares[25] = 'R3'
squares[28] = 'U2'
squares[30] = 'G2J'
squares[33] = 'CC3'
squares[35] = 'R4'
squares[36] = 'CH3'
squares[39] = 'H2'
reverse_map = {name: ind for ind, name in enumerate(squares)}


CC_cards = ['GO', 'JAIL'] + ['Nothing'] * 14
CH_cards = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'nextR', 'nextR', 'nextU',
               'minusThree'] + ['Nothing'] * 6


def upon_CC_or_CH(cards, current):
    card = cards.pop(0)
    cards.append(card)
    if card == 'Nothing':
        return current
    if card in ('GO', 'JAIL', 'C1', 'E3', 'H2', 'R1'):
        return reverse_map.get(card)
    if card == 'nextR':
        return min([reverse_map.get(r) for r in ['R1', 'R2', 'R3', 'R4']
                            if (current + 5) % 40 < reverse_map.get(r) + 5])
    if card == 'nextU':
        if reverse_map.get('U1') <= current < reverse_map.get('U2'):
            return reverse_map.get('U2')
        else:
            return reverse_map.get('U1')
    if card == 'minusThree':
        if current < 3:
            return current + 40 - 3
        else:
            return current - 3


def roll_the_dice(sidedness):
    first = randint(1, sidedness)
    second = randint(1, sidedness)
    return first, second


def move(current, roll, num_of_consecutive_doubles):
    if roll[0] == roll[1]:
        num_of_consecutive_doubles += 1
    else:
        num_of_consecutive_doubles = 0
    roll_sum = roll[0] + roll[1]
    current = (current + roll_sum) % 40

    if num_of_consecutive_doubles == 3:
        current = reverse_map.get('JAIL')
        num_of_consecutive_doubles = 0
    elif squares[current] == 'G2J':
        current = reverse_map.get('JAIL')
    elif squares[current][:2] == 'CC':
        current = upon_CC_or_CH(CC_cards, current)
    elif squares[current][:2] == 'CH':
        current = upon_CC_or_CH(CH_cards, current)

    return current, num_of_consecutive_doubles

def run_simulation(curr_seed, seed_for_card_shuffle, sidedness, num_iter=10000):
    seed(seed_for_card_shuffle)
    shuffle(CC_cards)
    shuffle(CH_cards)

    seed(curr_seed)
    current = 0
    num_of_consecutive_doubles = 0
    cnts = [0 for _ in range(40)]
    for _ in range(num_iter):
        roll = roll_the_dice(sidedness)
        current, num_of_consecutive_doubles = move(current, roll,
                                                     num_of_consecutive_doubles)
        cnts[current] += 1
    return cnts


def add_list(a, b):
    return list(map(lambda x: x[0] + x[1], zip(a, b)))


def find_most_popular_squares(sidedness):
    np.random.seed(0)
    seeds_for_tossing = np.random.randint(10000, size=10000)
    seeds_for_shuffle = np.random.randint(10000, size=10000)
    cnts = [0 for _ in range(40)]
    for curr_seed, seed_for_card_shuffle in zip(seeds_for_tossing, seeds_for_shuffle):
        cnts = add_list(cnts, run_simulation(curr_seed, seed_for_card_shuffle, sidedness))

    sorted_cnts = sorted([(c, ind) for ind, c in enumerate(cnts)], reverse=True)
    sum_cnts = sum(cnts)
    sorted_prob = list(map(lambda x: (x[0] / sum_cnts, x[1]), sorted_cnts))
    return sorted_prob[:3]


print(find_most_popular_squares(6))
print(find_most_popular_squares(4))
