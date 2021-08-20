import pygame
import sys
from raindrop import Raindrop

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

def update_screen(screen, raindrops, rd_settings):
    screen.fill(rd_settings.bg_color)

    raindrops.draw(screen)
    pygame.display.flip()



def create_raindrop(screen, rd_settings, raindrops, row_number, raindrop_number):
    raindrop = Raindrop(screen, rd_settings)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height

    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop_height + 2 * raindrop_height * row_number
    raindrops.add(raindrop)

def create_raindrops(screen, rd_settings, raindrops):
    raindrop = Raindrop(screen, rd_settings) 
    for row_number in range(raindrop.number_rows):
        for raindrop_number in range(raindrop.number_raindrops):
            create_raindrop(screen, rd_settings, raindrops, row_number, raindrop_number)



def create_raindrops_in_row(screen, rd_settings, raindrops):
    raindrop = Raindrop(screen, rd_settings)
    for raindrop_number in range(raindrop.number_raindrops):
        raindrop = Raindrop(screen, rd_settings)
        raindrop_width = raindrop.rect.width
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrops.add(raindrop)

def change_raindrop_direction(rd_settings, raindrops):
    for raindrop in raindrops.sprites():
        raindrop.rect.y += rd_settings.raindrop_drop_speed
    rd_settings.raindrop_direction *= -1

def check_raindrops_edges(screen, rd_settings, raindrops):
    for raindrop in raindrops.sprites():
        if raindrop.check_edges():
            change_raindrop_direction(rd_settings, raindrops)
            break
    
    for raindrop in raindrops.sprites():
        if raindrop.check_bottom_edges():
            count = 0
            for raindrop in raindrops:
                count += 1
                raindrops.remove(raindrop)
                if count == raindrop.number_raindrops:
                    create_raindrops_in_row(screen, rd_settings, raindrops)
                    print(len(raindrops))
                    break
            
    
def update_raindrops(screen, rd_settings, raindrops):
    check_raindrops_edges(screen, rd_settings, raindrops)
    raindrops.update()