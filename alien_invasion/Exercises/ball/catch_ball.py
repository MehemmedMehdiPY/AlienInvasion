import pygame
from pygame.constants import GL_MULTISAMPLEBUFFERS
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from character import Android
from ball import Ball
from game_stats import GameStats

def run_game():
    pygame.init()

    cb_settings = Settings()

    screen = pygame.display.set_mode((
        cb_settings.screen_width, cb_settings.screen_height))
    pygame.display.set_caption("Catching ball")
    
    stats = GameStats(cb_settings)

    android = Android(screen)
    bullets = Group()
    balls = Group() 
    #gf.create_ball(screen, balls)

    while True:

        gf.check_events(cb_settings, screen, android, bullets, stats)
        if stats.game_active:
            android.update(cb_settings)
            gf.update_bullet(bullets, balls, stats)

        gf.update_screen(screen, cb_settings, android, bullets, balls, stats)

run_game()