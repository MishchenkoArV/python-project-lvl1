import random
from brain_games.cli import MIN_RAND, MAX_RAND


def gcd():
    num_1 = random.randint(MIN_RAND, MAX_RAND)
    num_2 = random.randint(MIN_RAND, MAX_RAND)
    count = min(num_1, num_2)
    while count > 0:
        if num_1 % count == 0 and num_2 % count == 0:
            correct = count
            break
        count -= 1
    print(f'Question: {num_1} {num_2}')
    return correct
