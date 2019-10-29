import sys, pygame
import threading
import time
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
        self.speed = 10
        self.rect.top = y
        self.rect.left = x
        self.x = x
        self.y = y
        self.Max = HEIGHT
        self.ubicar = 0  
        self.TamX=32
        self.TamY=16
        self.image = pygame.transform.scale(self.image,(self.TamX,self.TamY))
        self.tipo = "Def"
    #dibuja la nota en pantalla 
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))  
        
    #movimiento : mueve la nota hasta el limite de pantalla
    def __movimientos(self,dificultad):
        if((self.y < 300)):
            if(self.y>-20):
                if((self.y>40)and(self.TamX<65)):
                    self.TamX += (int)(self.y*0.011)
                    self.TamY += (int)(self.y*0.010)
                    self.x += -0.3
                    self.image = load_image("Img/Notas/"+self.tipo+".png", True)
                    self.image = pygame.transform.scale(self.image,(self.TamX,self.TamY))
                if(self.tipo=="Green"):     
                    self.x -=1.4
                    self.rect.left -=1.4
                if(self.tipo=="Red"):
                    self.x -= 0.8
                    self.rect.left -=0.8
                if(self.tipo=="Yellow"):
                    self.x -= 0.05
                    self.rect.left -=0.05
                if(self.tipo=="Blue"):
                    self.x += 0.6
                    self.rect.left +=0.6
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
        Green = note(x+100,y,"Green")
        Green.tipo = "Green"
        listaNotas.append(Green)
    if(notas[1]==1):
        Red = note(x+135,y,"Red")
        Red.tipo = "Red"
        listaNotas.append(Red)
    if(notas[2]==1):
        Yellow = note(x+158,y,"Yellow")
        Yellow.tipo = "Yellow"
        listaNotas.append(Yellow)
    if(notas[3]==1):
        Blue = note(x+200,y,"Blue")
        Blue.tipo = "Blue"
        listaNotas.append(Blue)
    if(notas[4]==1):
        Orange = note(x+230,y,"Orange")
        Orange.tipo = "Orange"
        listaNotas.append(Orange)
    return listaNotas
#genera un movimiento en todas las notas existentes en la lista
def movimientolista(listaNotas,screen):
    for i in range(0,len(listaNotas)):
        listaNotas[i].comportamiento(1)
        if(listaNotas[i].y>-10):
            listaNotas[i].draw(screen)
        if(listaNotas[i].y>300):
            listaNotas[i].kill()
            
       
   


def main():
    song = load_sound("test")
    Guitarra = pygame.image.load("Img/Notas/Background4.png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    #se crean dos arreglo
    MatrizLNotas=[]
    #se rellenan estos arreglos con 1000 datos (deberia cargar las lineas de la cancion)
    #crea cada vez una linea ( inputArduino) nueva 
    MatrizNotas = matriz("Code/test-song1")
    #for i in MatrizNotas:
        #print(i)
    

    for i in range(0,len(MatrizNotas)):
        #crea las lineas de "notas" 
        LineaN = Linea(screen,MatrizNotas[i],150,(0-(80*i)))
        MatrizLNotas.append(LineaN)
    song.play()
    while True:
        screen.fill([0,0,0])
        screen.blit(Guitarra,(-315,-180))
        reloj.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0) 
        #for que genera el movimiento en las notas segun cuantas existan en la cancion
        for i in range(0,len(MatrizNotas)):
            movimientolista(MatrizLNotas[i],screen)
        pygame.display.flip()
        pygame.display.update()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()