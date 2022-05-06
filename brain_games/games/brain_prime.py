"""
Brain-prime game logic.
...
"""

import random


def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def brain_prime(MIN_RAND, MAX_RAND):
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    num = random.randint(MIN_RAND, MAX_RAND)
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    print(f'Question: {num}')
    return answer
