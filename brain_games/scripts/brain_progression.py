"""
Brain-proression game logic.
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
    print('What number is missing in the progression?')

     # Game settings
    MAX_SCORE = 3   # Number of rounds to win
    MAX_RAND = 50   # Maximum number for randon number generator
    MIN_RAND = 1    # Minumun number for randon number generator

    score = 0
    while score < MAX_SCORE:
        # Generate question
        begin = random.randint(MIN_RAND, MAX_RAND // 2)
        question = [begin]
        mult = random.randint(1,5)
        for i in range(1, 10):
            question.append(begin + mult*i)
        index = random.choice(range(0,9))
        new = ''
        c = 0
        while c < len(question):
            new += ' '
            if c == index:
                new += '..'
                correct = question[c]
            else:
                new += str(question[c])
            c += 1
        print(f'Question:{new}')
        
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
