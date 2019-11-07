import pygame
from note import *

class Botonera(pygame.sprite.Sprite):
    def __init__(self,x,y,tipo):
        self.image = load_image("Img/Botonera/"+tipo+".png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x 
        self.rect.centery = y 
        self.rect.top = y
        self.rect.left = x
        self.x  = x
        self.y  = y
        self.tipo = tipo 
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))
    def __On(self,num,slayer,surface):
        if(num==1):
            self.image = load_image("Img/Botonera/"+self.tipo+"On.png", True)
            self.draw(surface)
            #if(slayer==1):
                #self.image = load_image("Img/Botonera/On.png", True)
    def comportamiento(self,num,slayer,surface):
        self.__On(num,slayer,surface)