import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, screen, rd_settings):
        self.screen = screen
        self.rd_settings = rd_settings
        super(Raindrop, self).__init__()

        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        
        
        self.number_raindrops = self.get_number_raindrops_x()
        self.number_rows = self.get_number_rows()
        
    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def check_bottom_edges(self):
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
    
    def update(self):
        self.x += self.rd_settings.raindrop_speed_factor * self.rd_settings.raindrop_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def get_number_raindrops_x(self):
        available_space_x = self.rd_settings.screen_width - 2 * self.rect.width
        number_raindrops = int(available_space_x / (2 * self.rect.width))
        return number_raindrops

    def get_number_rows(self):
        available_space_y = self.rd_settings.screen_height - 3 * self.rect.height
        number_rows = int(available_space_y / (2 * self.rect.height))
        return number_rows