import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ai_settings, ship):

        super(Bullet, self).__init__()

        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        ai_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.color = 30, 30, 30

        self.y = float(self.rect.y)

    def update(self, ai_settings):
        self.y -= ai_settings.bullet_speed_factor
        self.rect.y = self.y 
        
    def bullet_draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)