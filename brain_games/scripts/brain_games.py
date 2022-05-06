"""
Brain Games Main Module.
...
"""

import prompt

from brain_games.games.brain_calc import brain_calc
from brain_games.games.brain_even import brain_even


def main():
    # Game settings
    MAX_SCORE = 3
    MAX_RAND = 25
    MIN_RAND = 1

    # Welcome masage
    print('Welcome to the Brain Games!')

    # Get player's name
    name = prompt.string('May I have your name? ')

    # Show avaliable games
    games = """
            Games
    1. Is number even?
    2. What is the result?
    """
    print(games) 

    # Chose the game to play
    game = prompt.string('Chose the game: ')
    
    # Main game loop
    score = 0
    while score < MAX_SCORE:
        if game == '1':
            correct = brain_even(MIN_RAND, MAX_RAND)
        elif game == '2':
            correct = brain_calc(MIN_RAND, MAX_RAND)
        else:
            print('That game doesn\'t exist!')
            return 0

        # Get player's answer
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
