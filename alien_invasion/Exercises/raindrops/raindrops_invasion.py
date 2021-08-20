import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings

def run_game():

    pygame.init()

    rd_settings = Settings()
    screen = pygame.display.set_mode((
        rd_settings.screen_width, rd_settings.screen_height))
    pygame.display.set_caption('Raindrop Invasion')

    raindrops = Group()
    gf.create_raindrops(screen, rd_settings, raindrops)
    
    while True:
        gf.check_events()
        gf.update_raindrops(screen, rd_settings, raindrops)
        gf.update_screen(screen, raindrops, rd_settings)

run_game()