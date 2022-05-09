#!/usr/bin/env python


from brain_games.cli import get_answer, is_correct, welcome_user
from brain_games.cli import MAX_SCORE
from brain_games.games.prime import prime


name = welcome_user()


def main():
    # Print the rules
    print('Answer "yes" if given number is prime. Otherwise answer "no"')

    for scrore in range(0, MAX_SCORE):
        correct = prime()
        answer = get_answer()
        if not is_correct(answer, correct, name):
            return 0
    print(f'Congratulations, {name}!')
    return 0


if __name__ == '__main__':
    main()
