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
        self.TamX=64
        self.TamY=32
        self.image = pygame.transform.scale(self.image,(self.TamX,self.TamY))
        self.tipo = "Def"
    #dibuja la nota en pantalla 
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))  
        
    #movimiento : mueve la nota hasta el limite de pantalla
    def __movimientos(self,dificultad):
        if((self.y < 300)):
            if(self.y>-50):
                if(self.TamX<128):
                    self.TamX = self.TamX+1
                    self.TamY = self.TamY+1
                    #self.image = pygame.transform.scale(self.image,(self.TamX,self.TamY))
                if(self.tipo=="Green"):     
                    self.x -= 1.2
                    self.rect.left -=1
                if(self.tipo=="Red"):
                    self.x -= 0.6
                    self.rect.left -=0.6
                if(self.tipo=="Yellow"):
                    self.x -= 0
                    self.rect.left -=0
                if(self.tipo=="Blue"):
                    self.x += 0.6
                    self.rect.left +=0.6
                if(self.tipo=="Orange"):
                    self.x += 1.1
                    self.rect.left +=1.1
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
        if(self.y == 320):
            print("kill")
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
        Green = note(x+84,y,"Green")
        Green.tipo = "Green"
        listaNotas.append(Green)
    if(notas[1]==1):
        Red = note(x+120,y,"Red")
        Red.tipo = "Red"
        listaNotas.append(Red)
    if(notas[2]==1):
        Yellow = note(x+148,y,"Yellow")
        Yellow.tipo = "Yellow"
        listaNotas.append(Yellow)
    if(notas[3]==1):
        Blue = note(x+176,y,"Blue")
        Blue.tipo = "Blue"
        listaNotas.append(Blue)
    if(notas[4]==1):
        Orange = note(x+220,y,"Orange")
        Orange.tipo = "Orange"
        listaNotas.append(Orange)
    return listaNotas
#genera un movimiento en todas las notas existentes en la lista
def movimientolista(listaNotas,screen):
    for i in range(0,len(listaNotas)):
        listaNotas[i].comportamiento(1)
        if(listaNotas[i].y>10):
            listaNotas[i].draw(screen)
        #if(listaNotas[i].y>320):
       
   


def main():
    Guitarra = pygame.image.load("Img/Notas/Background3.png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    pygame.display.update()
    #se crean dos arreglo
    MatrizNotas=[]
    MatrizLNotas=[]
    #se rellenan estos arreglos con 1000 datos (deberia cargar las lineas de la cancion)
    print("Cancion: ")
    for i in range(1000): 
        #crea cada vez una linea ( inputArduino) nueva 
        input = [random.randrange(2),random.randrange(2),random.randrange(2),random.randrange(2),random.randrange(2),0,0,0]
        print(input)
        MatrizNotas.append(input)
    for i in range(0,len(MatrizNotas)):
        #crea las lineas de "notas" 
        LineaN = Linea(screen,MatrizNotas[i],150,(0-(40*i)))
        MatrizLNotas.append(LineaN)
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