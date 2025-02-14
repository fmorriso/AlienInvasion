import pygame
from pygame.sprite import Sprite

from gui_settings import GuiSettings


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.images_dir = GuiSettings().get_images_directory()
        # print(f'in alien.py, images directory = {self.images_dir}')
        self.image = pygame.image.load(f'{self.images_dir}/alien.bmp')
        self.image.convert()
        self.rect = self.image.get_rect()

        # scale the image
        # double angle = 0;
        angle: float = 0
        scale: float = float(ai_game.settings.scaleFactor * 0.5)
        self.image = pygame.transform.rotozoom(self.image, angle, scale)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x
