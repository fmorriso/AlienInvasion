import pygame
from pygame.locals import *
 
class Ship:
    """A class to manage the ship."""
    GREEN = (0, 255, 0)
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image.convert()
        self.rect = self.image.get_rect()
        print(f'ship rectangle is {self.rect}')

        # add green border to help with debugging of scale up attempt
        # pygame.draw.rect(self.image, Ship.GREEN, self.rect, 1)

        # https://pygame.readthedocs.io/en/latest/3_image/image.html
        angle = 0
        scale = ai_game.settings.imageScale # 1.5
        self.image = pygame.transform.rotozoom(self.image, angle, scale)

        # adjust for new image height
        rect = self.image.get_rect()
        print(f'scaled image rectangle: {rect}')
        self.rect = rect
        print(f'adjusted self.rect = {self.rect}')

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
