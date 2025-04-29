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

past_screen_size = screen.get_size()

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
            if past_screen_size != screen.get_size() and screen.get_width() / screen.get_height() != consts.GAME_FIELD_PROPORTIONS:
                new_scale_width = screen.get_height() / consts.GAME_FIELD_HEIGHT
                new_scale_height = screen.get_width() / consts.GAME_FIELD_WIDTH
                new_scale = max(new_scale_width, new_scale_height)
                screen = pygame.display.set_mode(
                    (
                        consts.GAME_FIELD_WIDTH * new_scale,
                        consts.GAME_FIELD_HEIGHT * new_scale
                    ),
                    pygame.RESIZABLE
                )
                past_screen_size = screen.get_size()

    screen.fill((125, 125, 125))

    player.update(pressed_keys=pressed_keys)

    player.draw(screen=screen, scale=scale)

    pygame.display.update()

    clock.tick(60)
