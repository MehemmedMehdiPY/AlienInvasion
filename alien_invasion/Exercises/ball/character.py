import pygame

class Android():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/android.png')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.centerx = float(self.rect.centerx)

    def update(self, cb_settings):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += cb_settings.android_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.centerx -= cb_settings.android_speed_factor

        self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)