import pygame
import consts


class Player(pygame.sprite.Sprite):

    def __init__(self) -> None:

        super().__init__()

        self.__original_image = pygame.image.load('src/_content/images/player.png').convert_alpha()

        self.__original_image = pygame.transform.scale(
            self.__original_image,
            (
                self.__original_image.get_width() * 7,
                self.__original_image.get_height() * 7
            )
        )

        self.__image = self.__original_image.copy()
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (0, consts.GAME_FIELD_HEIGHT - self.__rect.height)

        self.__speedx = consts.PLAYER_SPEED
        self.__speed_of_falling_coefficient = consts.PLAYER_SPEED_OF_FALLING_COEFFICIENT
        self.__jump_force = consts.PLAYER_JUMP_FORCE
        self.__speed_of_falling = 0

    def update(self, pressed_keys: pygame.key.ScancodeWrapper) -> None:

        self.__speed_of_falling += self.__speed_of_falling_coefficient

        if self.__rect.bottomright[1] >= consts.GAME_FIELD_HEIGHT:

            '''остановка падения, и поднятие Player на высоту нижней границы игрового поля,
            то-есть препятствование падению игрока ЗА нижнюю границу игрового поля'''

            self.__speed_of_falling = 0
            self.__rect.bottomright = (self.__rect.bottomright[0], consts.GAME_FIELD_HEIGHT)

            if pressed_keys[pygame.K_w]:
                self.__speed_of_falling = -self.__jump_force

        if pressed_keys[pygame.K_d]:
            self.__rect.centerx += int(self.__speedx)
        if pressed_keys[pygame.K_a]:
            self.__rect.centerx -= int(self.__speedx)

        if self.__rect.bottomright[0] > consts.GAME_FIELD_WIDTH: 
            self.__rect.bottomright = (consts.GAME_FIELD_WIDTH, self.__rect.bottomright[1])
        if self.__rect.topleft[0] < 0:
            self.__rect.topleft = (0, self.__rect.topleft[1])

        self.__rect.centery += int(self.__speed_of_falling)

    def draw(self, screen: pygame.Surface, scale: float) -> None:

        self.__image = pygame.transform.scale(
            self.__original_image,
            (
                self.__original_image.get_width() * scale,
                self.__original_image.get_height() * scale
            )
        )

        rect = self.__image.get_rect(center=(self.__rect.centerx * scale, self.__rect.centery * scale))

        screen.blit(self.__image, rect)

        if consts.IS_DEBUG:
            '''Отрисовка границ Player на экране'''
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
