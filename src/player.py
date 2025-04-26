import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_coordinates: tuple) -> None:
        '''Создание главной функции класса Player'''
        super().__init__()
        self.__image = pygame.image.load('src/textures/player.png').convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * 10, 
                                                             self.__image.get_height() * 10))
        self.__rect = self.__image.get_rect(center=spawn_coordinates)
    
    def update(self) -> None:
        pass
    
    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.__image, self.__rect)
        