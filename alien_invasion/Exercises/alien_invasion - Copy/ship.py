import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.ship_speed_factor = 1.5
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed_factor
        self.rect.x = self.x

    def recenter(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)