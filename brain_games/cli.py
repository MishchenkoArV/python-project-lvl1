"""Some module."""
import prompt


def welcome_user():
    """Get user's name."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
