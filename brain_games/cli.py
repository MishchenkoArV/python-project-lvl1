import prompt


# Game settings
MAX_SCORE = 3   # Number of rounds to win
MAX_RAND = 50   # Maximum number for randon number generator
MIN_RAND = 1    # Mininum number for randon number generator


def welcome_user():
    # Welcome masage
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def is_correct(answer, correct, name):
    if answer == str(correct):
        print('Correct!')
        return True
    # If answer is wrong
    else:
        print(f"\n'{answer}' is wrong answer ;(.\
Correct answer was '{correct}'")
        print(f'Let\'s try again, {name}!')
        return False
