# import screen size utility module that helps us scale the game based on screen size
import pyautogui

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        deviceWidth, deviceHeight = pyautogui.size()
        self.screenPct = 0.66667

        gameWidth: int = int((deviceWidth * self.screenPct // 100) * 100)
        gameHeight: int =  int((deviceHeight * self.screenPct // 100) * 100)

        self.imageScale = 1 + self.screenPct#1.5;
        self.screen_width = gameWidth #1200
        self.screen_height = gameHeight # 800
        self.bg_color = (230, 230, 230)
        self.iconScale = 1.5;
