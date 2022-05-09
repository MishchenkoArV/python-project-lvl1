import random
from brain_games.cli import MIN_RAND, MAX_RAND


def calc():
    num_1 = random.randint(MIN_RAND, MAX_RAND)
    num_2 = random.randint(MIN_RAND, MAX_RAND)
    operation = random.choice('+-*')
    if operation == '+':
        correct = num_1 + num_2
    if operation == '-':
        correct = num_1 - num_2
    if operation == '*':
        correct = num_1 * num_2
    print(f'Question: {num_1} {operation} {num_2}')
    return correct
