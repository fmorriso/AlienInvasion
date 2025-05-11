import sys
from importlib.metadata import version

from alien_invasion import AlienInvasion


def get_package_version(package_name: str) -> str:
    return version(package_name)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def main():
    # Make a game instance, and run the game.
    ai = AlienInvasion(msg)
    ai.run_game()


if __name__ == '__main__':
    msg = f'Python version {get_python_version()}'
    print(msg)

    msg = f'PyAutoGUI version {get_package_version("pyautogui")}'
    print(msg)

    msg = f'PyGame version {get_package_version("pygame")}'
    print(msg)

    main()
