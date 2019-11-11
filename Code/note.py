import sys, pygame
import threading
#import time
import os
from pygame.locals import *
from Api import *
import random
# Constantes
# NO CONSIDERAR:usar velocidades para que tengan distinto ritmo falta agregar metodo para mover el arreglo (sigue usando el arreglo si sirve)
WIDTH = 640
HEIGHT = 480
EASY = 0
MEDIUM = 1
HARD = 2
EXPERT =3
#Clase que almacena la "nota" en el constructor cuenta con un "x" e "y" que son la posicion donde partiran esta nota 
class note(pygame.sprite.Sprite):
    def __init__(self,x,y,tipo):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Img/Notas/"+tipo+".png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.rect.top = y
        self.rect.left = x
        self.x = x
        self.y = y 
        self.TamX=16
        self.TamY=8
        self.image = pygame.transform.scale(self.image,(self.TamX,self.TamY))
        self.tipo =tipo
    #dibuja la nota en pantalla 
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))  
    #movimiento : mueve la nota hasta el limite de pantalla
    def __movimientos(self,dificultad):
        if((self.y < 440)):
            if(self.y>60):
                if((self.y>40)and(self.TamX<64)):
                    self.TamY += (int)(self.y*0.006)
                    self.TamX += (int)(self.y*0.009)
                    self.x += 0.2
                    self.image = load_image("Img/Notas/"+self.tipo+".png", True)
                    self.image = pygame.transform.scale(self.image,(self.TamX,self.TamY))
                if(self.tipo=="Green"):     
                    self.x -=1.7
                    self.rect.left -=1.7
                if(self.tipo=="Red"):
                    self.x -= 1
                    self.rect.left -=1
                if(self.tipo=="Yellow"):
                    self.x -= 0.28
                    self.rect.left -=0.28
                if(self.tipo=="Blue"):
                    self.x += 0.35
                    self.rect.left +=0.35
                if(self.tipo=="Orange"):
                    self.x += 1.2
                    self.rect.left +=1.2
            if(dificultad==0):
                self.rect.top+=1
                self.y +=1
            if(dificultad==1):
                self.rect.top+=3
                self.y +=3
            if(dificultad==2):
                self.rect.top+=4
                self.y +=4
            if(dificultad==3):
                self.rect.top+=6
                self.y +=6
            #pygame.display.update()
    #metodo que genera el movimiento
    def comportamiento(self,dificultad):
        self.__movimientos(dificultad)
def load_sound(sound_filename):
    """load the sound file from the given directory"""
    sound = pygame.mixer.Sound("Sounds/"+sound_filename+".wav")
    return sound
#crea una lista de notas( solo crea notas si estas estan en el arreglo )
# screen = pantalla de pygame
# notas = arreglo de notas ej[0,0,1,1,0,0,1]
# x e y = posicion (creo que duplique esto )    
def Linea(screen,notas,x,y):
    listaNotas=[]
    if(notas[0]==1):
        Green = note(x+130,y,"Green")
        Green.tipo = "Green"
        listaNotas.append(Green)
    if(notas[1]==1):
        Red = note(x+150,y,"Red")
        Red.tipo = "Red"
        listaNotas.append(Red)
    if(notas[2]==1):
        Yellow = note(x+165,y,"Yellow")
        Yellow.tipo = "Yellow"
        listaNotas.append(Yellow)
    if(notas[3]==1):
        Blue = note(x+190,y,"Blue")
        Blue.tipo = "Blue"
        listaNotas.append(Blue)
    if(notas[4]==1):
        Orange = note(x+210,y,"Orange")
        Orange.tipo = "Orange"
        listaNotas.append(Orange)
    return listaNotas
#genera un movimiento en todas las notas existentes en la lista
def movimientolista(listaNotas,screen):
    for i in range(0,len(listaNotas)):
        listaNotas[i].comportamiento(1)
        if((listaNotas[i].y>90)and(listaNotas[i].y<440)):
            listaNotas[i].draw(screen)
        if(listaNotas[i].y>440):
            listaNotas[i].kill()