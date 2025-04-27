import pygame

class Player(pygame.sprite.Sprite):
    '''Создание самого главного класса во всей игре - Player'''
    def __init__(self, spawn_coordinates: tuple) -> None:
        '''Создание главной функции класса Player'''
        super().__init__()
        
        self.__image = pygame.image.load('src/textures/player.png').convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * 10,
                                                             self.__image.get_height() * 10))
        
        self.__rect = self.__image.get_rect(center=spawn_coordinates)

        self.__speed = 10 # базовая скорость Player
        self.__speed_of_falling = 1 # базовая скорость падения Player вниз
        self.__jump_force = 20 # сила с которой Player отталкивается от платформы (нижней границы экрана)
        self.__speedy = 0 # скорость падения Player

    def update(self, pressed_keys: pygame.key.ScancodeWrapper) -> None:
        '''Создание функции update класса Player'''

        # увеличение скорости падения Player
        self.__speedy += self.__speed_of_falling

        # проверка на то, что Player пересек нижнюю границу экрана
        if self.__rect.bottomright[1] >= 540:

            '''остановка падения, и поднятие Player на высоту нижней границы экрана
            то-есть препятствование падению игрока ЗА нижнюю границу экрана'''
            self.__speedy = 0
            self.__rect.bottomright = (self.__rect.bottomright[0], 540)

            # проверка на прыжок, в момент, когда Player находится на платформе (нижней границе экрана)
            if pressed_keys[pygame.K_w]:
                self.__speedy = -self.__jump_force

        # проверка на нажатие клавиш для движений вправо и влево
        if pressed_keys[pygame.K_d]:
            self.__rect.centerx += self.__speed
        if pressed_keys[pygame.K_a]:
            self.__rect.centerx -= self.__speed

        # падение игрока вниз, то-есть искусственная гравитация
        self.__rect.centery += self.__speedy

    def draw(self, drawing_screen: pygame.surface.Surface) -> None:
        '''Создание функции draw класса Player'''

        # отрисовка Player
        drawing_screen.blit(self.__image, self.__rect)
