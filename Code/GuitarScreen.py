from note import load_image
import pygame

class Guitar(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = load_image("Img/Gameplay/puntaje.png", True)
        self.image = pygame.transform.scale(self.image,(100,110))
        self.x = x
        self.y = y