import pygame
import Botonera
from Controlador.InputArduino import InputArduino


pygame.init()
port='/dev/cu.usbmodem142301'
pantalla = pygame.display.set_mode((500,100))
backGround = [0, 0, 0]
pantalla.fill(backGround)
input = inputArduino
listaInteprete = [0,0,0,0,0,0,0,0]


while True:
    pantalla.fill(backGround)
    for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
    listaInteprete = input.input(port)
    bot = Botonera(pantalla,listaInteprete)
    pygame.display.update()
