# import screen size utility module that helps us scale the game based on screen size
import pyautogui

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings

        # calculate game size as a percentage of device screen size
        deviceWidth, deviceHeight = pyautogui.size()
        screenPct = 0.6667
        gameWidth: int = int((deviceWidth * screenPct // 100) * 100)
        gameHeight: int =  int((deviceHeight * screenPct // 100) * 100)

        self.screen_width = gameWidth #1200
        self.screen_height = gameHeight # 800
        self.bg_color = (230, 230, 230)