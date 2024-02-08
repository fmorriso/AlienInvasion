# import screen size utility module that helps us scale the game based on screen size
import sys
import pathlib
import pyautogui


class Settings:
    """A class to store all settings for Alien Invasion."""

    # private class variable containing the location of images used by this program
    __images_dir: str = ''

    @staticmethod
    def __find_images_directory() -> str:
        # print('top of __find_images_directory__')
        # get current file being run as the first step
        current_file: str = sys.argv[0]
        # print(f'Current __file__ = {pathlib.Path(__file__)}')
        # print(f'Current file = {current_file}')

        current_file_path = pathlib.Path(current_file)
        base_dir = current_file_path.parent
        # locate the images directory beneath the base directory
        sub_directories = list(base_dir.glob('**/images'))
        images_directory = sub_directories[0]
        if not images_directory.is_dir():
            print('Error: unable to locate images directory')

        return str(images_directory)

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        device_width, device_height = pyautogui.size()
        self.screenPct: float = float(3.0 / 4.0)

        game_width: int = int((device_width * self.screenPct // 100) * 100)
        game_height: int = int((device_height * self.screenPct // 100) * 100)

        self.scaleFactor = device_width / device_height + self.screenPct
        # print(f'scale factor = {self.scaleFactor}')
        self.screen_width = game_width  # 1200
        self.screen_height = game_height  # 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed: float = float(1.0 * self.scaleFactor)
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 5 * self.scaleFactor
        self.bullet_width = 3 * self.scaleFactor  # * 100 <--- for testing only
        self.bullet_height = 15 * self.scaleFactor
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed: int = int(3 * self.scaleFactor)

        # Alien settings
        self.alien_speed = 0.6667 * self.scaleFactor
        self.fleet_drop_speed: int = int(4 * self.scaleFactor)
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Directory locations
        if Settings.__images_dir == '':
            # print('In settings.py, init is about to call __find_images_directory__')
            Settings.__images_dir = Settings.__find_images_directory()
            # print(f'In settings.py, variable images_dir = {Settings.__images_dir}')

    @staticmethod
    def get_images_directory() -> str:
        return Settings.__images_dir
