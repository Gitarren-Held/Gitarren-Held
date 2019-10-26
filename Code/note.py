import sys, pygame
import threading
import time
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
        self.contador = 0    
    #dibuja la nota en pantalla 
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))  
    #movimiento : mueve la nota hasta el limite de pantalla
    def __movimientos(self,dificultad):
        if(self.y < HEIGHT):
            if(dificultad==0):
                self.rect.top+=1
                self.y +=1
            if(dificultad==1):
                self.rect.top+=2
                self.y +=3
            if(dificultad==2):
                self.rect.top+=3
                self.y +=6
            if(dificultad==3):
                self.rect.top+=4
                self.y +=10
            
        else:
            self.kill()
    #metodo que genera el movimiento
    def comportamiento(self,dificultad):
        self.__movimientos(dificultad)
            


       

#crea una lista de notas( solo crea notas si estas estan en el arreglo )
# screen = pantalla de pygame
# notas = arreglo de notas ej[0,0,1,1,0,0,1]
# x e y = posicion (creo que duplique esto )    
def Linea(screen,notas,x,y):
    listaNotas=[]
    if(notas[0]==1):
        Green = note(x+0,y+0,"Green")
        listaNotas.append(Green)
    if(notas[1]==1):
        Red = note(x+50,y+0,"Red")
        listaNotas.append(Red)
    if(notas[2]==1):
        Blue = note(x+100,y+0,"Blue")
        listaNotas.append(Blue)
    if(notas[3]==1):
        Yellow = note(x+150,y+0,"Yellow")
        listaNotas.append(Yellow)
    if(notas[4]==1):
        Orange = note(x+200,y+0,"Orange")
        listaNotas.append(Orange)
    return listaNotas
#genera un movimiento en todas las notas existentes en la lista
def movimientolista(listaNotas,screen):
    for i in range(0,len(listaNotas)):
        listaNotas[i].comportamiento(3)
        listaNotas[i].draw(screen)
   


def main():
    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    #se crean dos arreglo
    MatrizNotas=[]
    MatrizLNotas=[]
    #se rellenan estos arreglos con 1000 datos (deberia cargar las lineas de la cancion)
    print("Cancion:")
    for i in range(1000): 
        #crea cada vez una linea ( inputArduino) nueva 
        input = [random.randrange(2),random.randrange(2),random.randrange(2),random.randrange(2),random.randrange(2),0,0,0]
        print(input)
        MatrizNotas.append(input)
    for i in range(0,len(MatrizNotas)):
        #crea las lineas de "notas" 
        LineaN = Linea(screen,MatrizNotas[i],0,0-(i*50))
        MatrizLNotas.append(LineaN)
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0) 
        screen.fill([0,0,0])
        reloj.tick(60)
        #for que genera el movimiento en las notas segun cuantas existan en la cancion
        for i in range(0,len(MatrizNotas)):
            movimientolista(MatrizLNotas[i],screen)
        Linea(screen,input,0,0)
        pygame.display.flip()
        pygame.display.update()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()