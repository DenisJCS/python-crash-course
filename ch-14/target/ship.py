import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its position on the screen."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()  # NOTE: rect is the HTML rect attribute
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.center = float(self.rect.centery)
        self.moving_up = False  # movement flag
        self.moving_down = False  # movement flag

    def update(self):
        """Update ship position based on movement flag."""
        # if self.moving_down and self.rect.bottom <= self.screen_rect.height:
        #     self.y += self.ai_settings.ship_speed_factor

        # if self.moving_up and self.rect.top >= 0:
        #     self.center -= self.ai_settings.ship_speed_factor

        # self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.left