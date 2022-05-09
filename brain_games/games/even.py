import random
from brain_games.cli import MIN_RAND, MAX_RAND


def even():
    question = random.randint(MIN_RAND, MAX_RAND)
    if question % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    print(f'Question: {question}')
    return correct
