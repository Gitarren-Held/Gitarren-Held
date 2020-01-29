import pygame
from note import *
import time

WIDTH = 640
HEIGHT = 480
color = (31,255,0)
start_pos = (0, 420)
end_pos = (WIDTH,420)
start_pos2 = (0, 440)
end_pos2 = (WIDTH,440)
width = 1
#clase botonera "OJO " solo carga un 'boton'
class Botonera(pygame.sprite.Sprite):
    #parametros x e y (posicion), tipo = Green,Blue etc...
    def __init__(self,x,y,tipo):
        self.image = load_image("Img/Botonera/"+tipo+".png", True)
        self.image = pygame.transform.scale(self.image,(100,56))
        self.rect = self.image.get_rect()
        self.rect.centerx = x/2
        self.rect.centery = y/2  + 35
        self.rect.top = y+20
        self.rect.left = x
        self.x  = x
        self.y  = y
        self.tipo = tipo 
    #dibuja la clase , surface = pantalla donde se dibuja   
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))
    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
    def Active_collider(self,sprite,score,screen):
        #print(len(sprite))
        for i in range(0,len(sprite)):
            if((self.is_collided_with(sprite[i]))and(self.tipo==sprite[i].tipo)and(sprite[i].y>439)and(sprite[i].y<471)): 
                sprite[i].kill()
                sprite[i].end=True
                self.image = pygame.transform.scale(load_image("Img/Botonera/"+self.tipo+"OnFire.png", True),(100,56))
                screen.blit(self.image,(self.x,self.y))
                
                return (True,sprite)
        return (False,sprite)
        
    #determina el estado del 'boton' dependiendo del input del usuario
    #1 = activo, num = arreglo[posicion](0,0,0,0,0,0)
    def __On(self,num,slayer):
        if(num==1):
            self.image = pygame.transform.scale(load_image("Img/Botonera/"+self.tipo+"On.png", True),(100,56))
            #if(slayer==1):
                #self.image = load_image("Img/Botonera/On.png", True)
        else:
            self.image = pygame.transform.scale(load_image("Img/Botonera/"+self.tipo+".png", True),(100,56))  
    def comportamiento(self,num,slayer):
        self.__On(num,slayer)

#Crea la botonera completa con todos los colores y las guarda en una lista, Devuelve la lista 
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
#Evalua el comportamiento de cada boton segun el input
def comportamientoBotonera(bot,Input,screen):
    bot[0].comportamiento(Input[0],Input[7])
    bot[1].comportamiento(Input[1],Input[7])
    bot[2].comportamiento(Input[2],Input[7])
    bot[3].comportamiento(Input[3],Input[7])
    bot[4].comportamiento(Input[4],Input[7])
#dibuja la botonera
def drawAll(bot,screen):
    bot[0].draw(screen)
    bot[1].draw(screen)
    bot[2].draw(screen)
    bot[3].draw(screen)
    bot[4].draw(screen)
