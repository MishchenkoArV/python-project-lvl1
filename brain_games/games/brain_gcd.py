"""
Brain-GCD game loic.
...
"""

import random

def brain_gcd(MIN_RAND, MAX_RAND):
    print('Find the greatest commom divisor of given numbers.')
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
