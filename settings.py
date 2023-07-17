# import screen size utility module that helps us scale the game based on screen size
import sys

import pyautogui


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        device_width, device_height = pyautogui.size()
        self.screenPct: float = float(2.0 / 3.0)

        game_width: int = int((device_width * self.screenPct // 100) * 100)
        game_height: int = int((device_height * self.screenPct // 100) * 100)

        self.scaleFactor = device_width / device_height + self.screenPct
        print(f'scale factor = {self.scaleFactor}')
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
        self.alien_speed = 1.0 * self.scaleFactor
        self.fleet_drop_speed: int = int(10 * self.scaleFactor)
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Directory locations

    @staticmethod
    def get_image_directory() -> str:
        print('top of get_image_directory')
        # get current file being run
        current_file: str = sys.argv[0]
        print(f'current_file: {current_file}')
        i: int = -1
        try:
            i  = current_file.rindex("\\")
        except ValueError:
            print(f'{i}.  No backslash found. Trying forward slash')            
        if i == -1:
            i = current_file.rindex('/')
            
        print(f'last directory separator character location: {i}')
        current_dir: str = current_file[0:i]
        print(f'current_dir: {current_dir}')
        return current_dir
