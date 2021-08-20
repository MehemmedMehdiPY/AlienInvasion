from hashlib import new
import pygame
import sys
from ball import Ball
from bullet import Bullet
from game_over import GameOver

def check_KEYDOWN_events(event, cb_settings, screen, android, bullets, stats):
    if event.key == pygame.K_RIGHT:
        android.moving_right = True
    
    elif event.key == pygame.K_LEFT:
        android.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullets(cb_settings, screen, android, bullets, stats)

    elif event.key == pygame.K_q:
        sys.exit()
    

def check_KEYUP_events(event, android):
    if event.key == pygame.K_RIGHT:
        android.moving_right = False
    
    elif event.key == pygame.K_LEFT:
        android.moving_left = False

def check_events(cb_settings, screen, android, bullets, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event, cb_settings, screen, android, bullets, stats)

        elif event.type == pygame.KEYUP:
            check_KEYUP_events(event, android)

def fire_bullets(cb_settings, screen, android, bullets, stats):
    if len(bullets) < cb_settings.bullet_allowed and stats.missed_target < cb_settings.limited_target_number :
        new_bullet = Bullet(cb_settings, screen, android)
        bullets.add(new_bullet)

    elif stats.missed_target >= cb_settings.limited_target_number:
        stats.game_active = False

def update_screen(screen, cb_settings, android, bullets, balls, stats):
    screen.fill(cb_settings.bg_color)

    if not stats.game_active:
        message = GameOver(cb_settings, screen)
        message.blitme()

    android.blitme()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    create_ball(screen, balls)

    balls.draw(screen)
    pygame.display.flip()

def update_bullet(bullets, balls, stats):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.top < 0:
            stats.missed_target += 1
            bullets.remove(bullet)

    check_bullet_ball_collisions(bullets, balls, stats)

def create_ball(screen, balls):
    if len(balls) == 0:
        new_ball = Ball(screen)
        balls.add(new_ball)

def check_bullet_ball_collisions(bullets, balls, stats):
    collisions = pygame.sprite.groupcollide(bullets, balls, True, True)
    if collisions:
        stats.missed_target = 0


        