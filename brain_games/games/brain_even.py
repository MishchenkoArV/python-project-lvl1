"""
Brain-even game logic.
...
"""

import random


def brain_even(MIN_RAND, MAX_RAND):
    print('Answer "yes" if the number is even, otherwise "no".')
    question = random.randint(MIN_RAND, MAX_RAND)
    if question % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'
    print(f'Question: {question}')
    return correct
