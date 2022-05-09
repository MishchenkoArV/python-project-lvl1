import random
from brain_games.cli import MIN_RAND, MAX_RAND
from brain_games.cli import is_prime


def prime():
    num = random.randint(MIN_RAND, MAX_RAND)
    if is_prime(num):
        correct = 'yes'
    else:
        correct = 'no'
    print(f'Question: {num}')
    return correct
