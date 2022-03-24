import pygame
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self,initPosition) -> None:
        super().__init__()
        self.position = initPosition

    @abstractmethod
    def draw(self):
        pass

class Monster(Character):
    def __init__(self, initPosition, screen) -> None:
        self.ImgRoute = "./assets/img/monstruo.png"
        self.screen = screen
        self.monsterImg = pygame.image.load(self.ImgRoute)
        self.monsterImg = pygame.transform.scale(self.monsterImg, (100,100))
        super().__init__(initPosition)
        
    def draw(self):
        self.screen.blit(self.monsterImg, self.position.getCoordinates())

class Ghost(Character):
    def __init__(self, initPosition, screen) -> None:
        self.ImgRoute = "./assets/img/fantasma.png"
        self.screen = screen
        self.ghostImg = pygame.image.load(self.ImgRoute)
        self.ghostImg = pygame.transform.scale(self.ghostImg, (100,100))
        super().__init__(initPosition)
        
    def draw(self):
        self.screen.blit(self.ghostImg, self.position.getCoordinates())