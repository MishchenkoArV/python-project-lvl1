#!/usr/bin/env python


from brain_games.cli import get_answer, is_correct, welcome_user
from brain_games.cli import MAX_SCORE
from brain_games.games.progression import progression


name = welcome_user()


def main():
    print('What number is missing in the progression?')

    for scrore in range(0, MAX_SCORE):
        correct = progression()
        answer = get_answer()
        if not is_correct(answer, correct, name):
            return 0
    print(f'Congratulations, {name}!')
    return 0


if __name__ == '__main__':
    main()
