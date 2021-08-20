import pygame
from random import randint
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/basketball.png')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.x = randint(self.rect.width, self.screen_rect.width - self.rect.width)
        self.rect.y = self.screen_rect.top + self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)