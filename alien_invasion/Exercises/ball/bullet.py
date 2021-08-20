import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, cb_settings, screen,android):
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0,
                      cb_settings.bullet_width, cb_settings.bullet_height)
        
        self.rect.centerx = android.rect.centerx
        self.rect.top = android.rect.top

        self.y = float(self.rect.y)

        self.color = cb_settings.bullet_color
        self.speed_factor = cb_settings.bullet_speed_factor
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)