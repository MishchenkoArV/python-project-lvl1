#!/usr/bin/env python
"""
Brain-calc game logic.
...
"""

# Standart library imports
import random
import prompt


# Welcome masage
print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')


def main():
    # Print the rules
    print('What is the result of the exprasson?')

    # Game settings
    MAX_SCORE = 3   # Number of rounds to win
    MAX_RAND = 50   # Maximum number for randon number generator
    MIN_RAND = 1    # Minumun number for randon number generator

    score = 0
    while score < MAX_SCORE:
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

        answer = prompt.string('Your answer: ')

        # If answer is correct
        if answer == str(correct):
            print('Correct!')
            score += 1
        # If answer is wrong
        else:
            print(f"\n'{answer}' is wrong answer ;(.\
 Correct answer was '{correct}'")
            print(f'Let\'s try again, {name}!')
            return 0

    # If player wins
    print(f'Congratulations, {name}!')
    return 0


if __name__ == '__main__':
    main()
