"""
Brain-prime game logic.
...
"""

# Standart library imports
import random
import prompt


# Welcome masage
print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')


def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def main():
    # Print the rules
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    
    # Game settings
    MAX_SCORE = 3   # Number of rounds to win
    MAX_RAND = 50   # Maximum number for randon number generator
    MIN_RAND = 1    
    score = 0
    while score < MAX_SCORE:
        # Generate question
        num = random.randint(MIN_RAND, MAX_RAND)
        if is_prime(num):
            correct = 'yes'
        else:
            correct = 'no'
        print(f'Question: {num}')
        
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
