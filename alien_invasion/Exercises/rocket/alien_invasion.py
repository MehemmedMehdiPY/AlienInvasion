# W A S D

import pygame
from settings import Settings
import game_functions as gf
from rocket import Rocket

def run_game():
    pygame.init()

    ai_settings = Settings()

    

    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    rocket = Rocket(screen)

    while True:
        
        gf.check_events(rocket)
        rocket.update(ai_settings)
        gf.update_screen(screen, ai_settings, rocket)


run_game()