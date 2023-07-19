import pygame
from pygame.locals import *
import sys

from settings import Settings


class Ship:
    """A class to manage the ship."""
    GREEN = (0, 255, 0)
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.images_dir = Settings().get_images_directory()
        # print(f'in ship.py, images directory = {self.images_dir}')
        self.image = pygame.image.load(f'{self.images_dir}/ship.bmp')
        self.image.convert()
        self.rect = self.image.get_rect()
        # scale the image
        # https://pygame.readthedocs.io/en/latest/3_image/image.html
        angle: float = 0
        scale: float = ai_game.settings.scaleFactor
        self.image = pygame.transform.rotozoom(self.image, angle, scale)
        self.rect = self.image.get_rect();

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x: float = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
