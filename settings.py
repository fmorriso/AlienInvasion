# import screen size utility module that helps us scale the game based on screen size
import pyautogui

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        deviceWidth, deviceHeight = pyautogui.size()
        self.screenPct: float = float(2.0 / 3.0)

        gameWidth: int = int((deviceWidth * self.screenPct // 100) * 100)
        gameHeight: int =  int((deviceHeight * self.screenPct // 100) * 100)

        self.scaleFactor = deviceWidth / deviceHeight + self.screenPct
        print(f'scale factor = {self.scaleFactor}')
        self.screen_width = gameWidth #1200
        self.screen_height = gameHeight # 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed: float = float(1.0 * self.scaleFactor)

        # Bullet settings
        self.bullet_speed = 5 * self.scaleFactor
        self.bullet_width = 3 * self.scaleFactor
        self.bullet_height = 15 * self.scaleFactor
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed: int = int(3 * self.scaleFactor)

        # Alien settings
        self.alien_speed = 1.0 * self.scaleFactor
        self.fleet_drop_speed: int = int(10 * self.scaleFactor)
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
