import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(screen, ai_settings, ship, aliens)

    while True:
        gf.check_events(screen, ai_settings, ship, bullets)
        ship.update()
        gf.update_bullets(screen, ai_settings, ship, aliens, bullets)
        gf.update_aliens(screen, ai_settings, aliens, bullets, ship)
        gf.update_screen(screen, ai_settings, ship, aliens, bullets)
        
run_game()