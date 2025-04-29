import sys
import pygame
import consts
from player import Player
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

pygame.init()
info = pygame.display.Info()

screen_size = info.current_w * consts.MAIN_WINDOW_SCALE, info.current_h * consts.MAIN_WINDOW_SCALE

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

player = Player()

clock = pygame.time.Clock()

past_screen_width = screen.get_width()
past_screen_height = screen.get_height()

while True:
    events = pygame.event.get()
    pressed_keys = pygame.key.get_pressed()

    scale = screen.get_width() / consts.GAME_FIELD_WIDTH

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.VIDEORESIZE:
            if screen.get_width() / 16 != screen.get_height() / 9:
                if past_screen_width != screen.get_width():
                    screen = pygame.display.set_mode(
                        (
                            screen.get_width(),
                            int(screen.get_width() / 16 * 9)
                        ),
                        pygame.RESIZABLE
                    )
                elif past_screen_height != screen.get_height():
                    screen = pygame.display.set_mode(
                        (
                            int(screen.get_height() / 9 * 16),
                            screen.get_height()
                        ),
                        pygame.RESIZABLE
                    )
            past_screen_width = screen.get_width()
            past_screen_height = screen.get_height()

    screen.fill((125, 125, 125))

    player.update(pressed_keys=pressed_keys)

    player.draw(screen=screen, scale=scale)

    pygame.display.update()

    clock.tick(60)
