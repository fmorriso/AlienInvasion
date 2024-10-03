from alien_invasion import AlienInvasion
import sys


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

if __name__ == '__main__':
    msg = f'Python version {get_python_version()}'
    print(msg)
    # Make a game instance, and run the game.
    ai = AlienInvasion(msg)
    ai.run_game()