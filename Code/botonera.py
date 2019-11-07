import pygame
from note import *

class Botonera(pygame.sprite.Sprite):
    def __init__(self,x,y,tipo):
        self.image = load_image("Img/Botonera/"+tipo+".png", True)
        self.image = pygame.transform.scale(self.image,(100,56))
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
    def __On(self,num,slayer):
        if(num==1):
            self.image = pygame.transform.scale(load_image("Img/Botonera/"+self.tipo+"On.png", True),(100,56))
            #if(slayer==1):
                #self.image = load_image("Img/Botonera/On.png", True)
        else:
            self.image = pygame.transform.scale(load_image("Img/Botonera/"+self.tipo+".png", True),(100,56))  
    def comportamiento(self,num,slayer):
        self.__On(num,slayer)


def BotoneraCompleta():
    bot = []
    botG = Botonera(75,420,"Green")
    botR = Botonera(180,420,"Red")
    botY = Botonera(285,420,"Yellow")
    botB = Botonera(385,420,"Blue")
    botO = Botonera(485,420,"Orange")
    bot.append(botG)
    bot.append(botR)
    bot.append(botY)
    bot.append(botB)
    bot.append(botO)
    return bot
def comportamientoBotonera(bot,Input):
    bot[0].comportamiento(Input[0],Input[7])
    bot[1].comportamiento(Input[1],Input[7])
    bot[2].comportamiento(Input[2],Input[7])
    bot[3].comportamiento(Input[3],Input[7])
    bot[4].comportamiento(Input[4],Input[7])
def drawAll(bot,screen):
    bot[0].draw(screen)
    bot[1].draw(screen)
    bot[2].draw(screen)
    bot[3].draw(screen)
    bot[4].draw(screen)
