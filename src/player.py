import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, spawn_coordinates: tuple) -> None:
        '''Создание главной функции класса Player'''
        super().__init__()
        self.__image = pygame.image.load('src/textures/player.png').convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * 10, 
                                                             self.__image.get_height() * 10))
        
        self.__rect = self.__image.get_rect(center=spawn_coordinates)
        
        self.__speed = 5
    
    def update(self, keys: pygame.key.ScancodeWrapper) -> None:
        if keys[pygame.K_d]:
            self.__rect.centerx += self.__speed
        if keys[pygame.K_a]:
            self.__rect.centerx -= self.__speed
            
        if keys[pygame.K_w]:
            self.__rect.centery -= self.__speed
        if keys[pygame.K_s]:
            self.__rect.centery += self.__speed
    
    def draw(self, screen: pygame.surface.Surface) -> None:
        screen.blit(self.__image, self.__rect)
        