import pygame,sys
from modoSolo import *
from classMenu import *

width = 640
height = 480
def mostrarloading(self):
    inicio = True
    screen = pygame.display.set_mode( (width, height))
    fondo = pygame.image.load('imagesInicio/loading.png').convert() 
    fondo = pygame.transform.scale(fondo,(width,height))
    pygame.display.set_caption('Guitar Hero') 
    self.clock = pygame.time.Clock()
    cont =0
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            screen.blit(fondo, (0, 0))
            pygame.display.update()
            self.clock.tick(30)#FPS = 30 
        if cont>= 1000000:
            inicio = False
        cont+=1
def cargarArchivo(filename,self):
    print(filename)
    #Poner Gameplay.
    
    mostrarloading(self)