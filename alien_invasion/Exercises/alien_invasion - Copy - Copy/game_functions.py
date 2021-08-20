import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)

def check_keydown_events(screen, ai_settings, event, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(screen, ai_settings, ship, bullets, play_button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(screen, ai_settings, event, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_clicking_play_button(mouse_x, mouse_y, play_button, stats)

def check_clicking_play_button(mouse_x, mouse_y, play_button, stats):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

        
def change_fleet_direction(aliens, ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(aliens, ai_settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break

def update_aliens(screen, ai_settings, aliens, bullets, ship, stats):
    check_fleet_edges(aliens, ai_settings)
    aliens.update()
    
    check_alien_ship_collisions(screen, ai_settings, aliens, bullets, ship, stats)

def update_bullets(screen, ai_settings, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)
    
    check_alien_bullet_collisions(screen, ai_settings, ship, aliens, bullets)

def update_screen(screen, ai_settings, ship, aliens, bullets, play_button, stats):
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.bullet_draw()
    
    ship.blitme()
    aliens.draw(screen)
    
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def get_number_aliens(screen_width, alien_width):
    available_space_x = screen_width - alien_width * 2 
    number_aliens = int(available_space_x /(alien_width * 2))
    return number_aliens

def get_number_rows(screen_height, alien_height, ship):
    available_space_y = screen_height - alien_height * 3 - ship.rect.height
    number_rows = int(available_space_y / (alien_height * 2))
    return number_rows

def create_alien(screen, ai_settings, aliens, alien_number, row_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number

    aliens.add(alien)

def create_fleet(screen, ai_settings, ship, aliens):
    alien = Alien(screen, ai_settings)
    number_aliens = get_number_aliens(ai_settings.screen_width, alien.rect.width)
    number_rows = get_number_rows(ai_settings.screen_height, alien.rect.height, ship)

    for row_number in range(number_rows):        
        for alien_number in range(number_aliens):
            create_alien(screen, ai_settings, aliens, alien_number, row_number)
    
def check_alien_bullet_collisions(screen, ai_settings, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(screen, ai_settings, ship, aliens)

def ship_hit(screen, ai_settings, aliens, bullets, ship, stats):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()
        bullets.empty()

        create_fleet(screen, ai_settings, ship, aliens)
        ship.recenter()
        # Take a pause
        sleep(0.5)
    else:
        stats.game_active = False

def check_alien_ship_collisions(screen, ai_settings, aliens, bullets, ship, stats):
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, ai_settings, aliens, bullets, ship, stats)