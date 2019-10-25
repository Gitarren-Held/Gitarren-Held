#Módulos
import random
import pygame,sys
from pygame.locals import *
from classMenu import * #Importamos la claseMenu!
# Funciones
def iniciar_solo():
    print( " Inicia Modo Solo")
def iniciar_carrera():
    print (" Inicio Modo Carrera!")
def creditos():
    print (" Créditos!!")
def salir_del_programa():
    print (" Salir de Guitar Hero.")
    sys.exit(0)
# Constantes
width = 640
height = 480
opciones = [("Solo", iniciar_solo),("Carrera", iniciar_carrera),("Creditos", creditos),("Salir", salir_del_programa)]
# ---------------------------------------------------------------------
# Clases         
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#Iniciamos el Main!!
def main():
    salir = False
    pygame.font.init()
    screen = pygame.display.set_mode((width, height))
    fondo = pygame.image.load('images/fondo2.png').convert()  
    fondo = pygame.transform.scale(fondo,(width,height))#Escalamos la imagen en Pygame
    menu = Menu(opciones)
    menu.gotoMenu()
    pygame.display.set_caption('Guitar Hero') 

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