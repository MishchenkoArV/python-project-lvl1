"""
Brain-calc game logic.
...
"""

import random
import prompt


def brain_calc(MIN_RAND, MAX_RAND):
    # Print the rules
    print('\nWhat is the result of the exprasson?')

    # Generate question
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
