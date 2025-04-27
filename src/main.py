import sys
import pygame

import consts

from player import Player

pygame.init()


screen = pygame.display.set_mode(consts.START_SCREEN_SIZE, pygame.RESIZABLE)
player = Player(spawn_coordinates=(100, 100))


clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    pressed_keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    
    screen.fill((125, 125, 125))

    player.update(pressed_keys=pressed_keys)
    player.draw(drawing_screen=screen)
    
    pygame.display.update()

    clock.tick(60)
