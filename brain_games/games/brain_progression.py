"""
Brain-proression game logic.
...
"""

import random


def brain_prog(MIN_RAND, MAX_RAND):
    print('What number is missing in the progression?')
    begin = random.randint(MIN_RAND, MAX_RAND // 2)
    question = [begin]
    mult = random.randint(1,5)
    for i in range(1, 10):
        question.append(begin + mult*i)
    index = random.choice(range(0,9))
    new = ''
    c = 0
    while c < len(question):
        new += ' '
        if c == index:
            new += '..'
            correct = question[c]
        else:
            new += str(question[c])
        c += 1
    print(f'Question:{new}')
    return correct
