"""Entry point module."""
from brain_games.cli import welcome_user


def main():
    """Entry point function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
