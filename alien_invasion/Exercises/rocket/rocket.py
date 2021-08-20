import pygame

class Rocket():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        # Positions
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Positions in the values of float
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Rocket movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self, ai_settings):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += ai_settings.rocket_speed_factor

        if self.moving_left and self.rect.left > 0 :
            self.center -= ai_settings.rocket_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.bottom -= 1
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += 1

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
