"""
Brain-even game logic.
...
"""

import random
import prompt


def brain_even():
    # Ask for player's name
    name = prompt.string('May I have your name? ')

    # Print the ruels
    print('Answer "yes if the number is even, otherwise answer "no".')

    # Game settings
    MIN_NUM = 1
    MAX_NUM = 25
    MAX_SCORE = 3

    # Game loop
    score = 0
    while score < MAX_SCORE:
        # Generate question
        question = random.randint(MIN_NUM, MAX_NUM)
        # Generate correct answer
        if question % 2 == 0:
            correct = 'yes'
        else:
            correct = 'no'
        # Ask question
        print(f'Question: {question}')

        # Get player's answer
        ans = prompt.string('Your answer: ')

        # If answer is correct
        if ans == correct:
            print('Correct!')
            score += 1
        # If answer is wrong
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was\
 '{correct}'.")
            print(f'Let\'s try again, {name}!')
            return 0

    # If player wins
    print(f'Congratulations, {name}!')
    return 0


def main():
    print('Welcome to the Brain Games!')
    brain_even()


if __name__ == '__main__':
    main()
