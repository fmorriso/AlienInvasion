from alien_invasion import AlienInvasion
import sys


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()