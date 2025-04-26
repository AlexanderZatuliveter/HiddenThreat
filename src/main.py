import sys
import pygame

from player import Player

pygame.init()

screen = pygame.display.set_mode((960, 540), pygame.RESIZABLE)
clock = pygame.time.Clock()

player = Player(spawn_coordinates=(100, 100))

while True:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    
    screen.fill((125, 125, 125))

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    player.update(keys=keys)
    
    player.draw(screen=screen)
    
    pygame.display.update()
    

    clock.tick(60)
