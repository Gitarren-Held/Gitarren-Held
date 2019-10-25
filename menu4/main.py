#Módulos
import random
import pygame,sys
from pygame.locals import *
from classMenu import * #Importamos la claseMenu!
import utils
from utils import *
# Funciones
# Constantes
# ---------------------------------------------------------------------
# Clases         
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#Iniciamos el Main!!
def main():
    pygame.font.init()
    screen = pygame.display.set_mode((width, height))
    fondo = pygame.image.load('imagesInicio/inicio.JPG').convert() 
    icon = pygame.image.load('images/iconGuitarHero.png') 
    fondo = pygame.transform.scale(fondo,(width,height))#Escalamos la imagen en Pygame
    menu = Menu(opciones)
    menu.inicio1()
    menu.inicio2()
    menu.inicio3()
    pygame.display.set_caption('Guitar Hero') 
    pygame.display.set_icon(icon)
    salir = False
    while not salir:
        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(0)
    return 0
if __name__ == '__main__':  
    pygame.init()
    main()