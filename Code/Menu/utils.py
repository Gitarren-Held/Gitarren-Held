import pygame,sys
import modoSolo
from modoSolo import *
from main import *
from classMenu import *
#ƒunciones:
def iniciar_solo(): 
    pygame.init()
    solo()
def iniciar_carrera():
    print (" Inicio Modo Carrera!")
def creditos():
    print (" Créditos!!")
def salir_del_programa():
    print (" Salir de Guitar Hero.")
    sys.exit(0)
#constantes
width = 640
height = 480
opciones = [("Solo", iniciar_solo),("Carrera", iniciar_carrera),("Creditos", creditos),("Salir", salir_del_programa)]
#Colores RGB
black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)