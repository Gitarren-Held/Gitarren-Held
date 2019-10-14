
import pygame

from botonera import Botonera
from Arduino import InputArduino



pygame.init()
direccion='/dev/cu.usbmodem142101'
pantalla = pygame.display.set_mode((500,100))
backGround = [0, 0, 0]
pantalla.fill(backGround)
listaInteprete = [0,0,0,0,0,0,0,0]


while True:
    pantalla.fill(backGround)
    for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
    Botonera(InputArduino.Input())
    Botonera.Gameplay(pantalla,listaInteprete)
    pygame.display.update()
