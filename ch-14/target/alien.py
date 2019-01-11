import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize an instance of Alien and set position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set rect attr.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near top left corner of window
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self, ship):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        # if the image moves off the screen to the right or left
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """Move alien to the right."""
        # Increase x of sprite by speed factor
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        # Assign new value of x to alien rect
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)