import pygame

class GameOver():
    def __init__(self, cb_settings, screen):
        self.screen = screen
        
        self.image = pygame.image.load('images/game_over.png')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        
        self.rect.x = (cb_settings.screen_width - self.rect.width) // 2
        self.rect.y = (cb_settings.screen_height - self.rect.height) // 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
