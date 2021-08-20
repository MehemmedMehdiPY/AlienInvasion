import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(screen, "PLAY")

    gf.create_fleet(screen, ai_settings, ship, aliens)

    while True:
        gf.check_events(screen, ai_settings, ship, bullets, play_button, stats)
        if stats.game_active:
            ship.update(ai_settings)
            gf.update_bullets(screen, ai_settings, ship, aliens, bullets)
            gf.update_aliens(screen, ai_settings, aliens, bullets, ship, stats)
        gf.update_screen(screen, ai_settings, ship, aliens, bullets, stats, play_button)
        
run_game()