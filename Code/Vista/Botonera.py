import pygame


class Botonera:
   
    def __init__(self,pantalla,listaInterprete):
        self.lista = listaInterprete

        for i in range(8):
            self.lista[i] =listaInterprete[i]

        self.greenRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Verde1.png")), (100,100))
        self.greenPressed = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Verde2.png")), (100,100))
        self.blueRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Azul1.png")), (100,100))
        self.bluePressed= pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Azul2.png")), (100,100))
        self.orangeRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Naranjo1.png")), (100,100))
        self.orangePressed= pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Naranja2.png")), (100,100))
        self.yellowRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Amarillo1.png")), (100,100))
        self.yellowPressed= pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Amarillo.png")), (100,100))
        self.redRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Rojo.png")), (100,100))
        self.redPressed= pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Rojo2.png")), (100,100))
        self.Slayer = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/ON.png")), (100,100))
        self.starPowerRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/starpower.png")), (100,100))
        self.StarPowerPressed = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/starpower2.png")), (100,100))
        self.starPowerSlayer = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/starpower3.png")), (100,100))
        pantalla.blit(self.greenRelease,(0,0))
        pantalla.blit(self.redRelease,(100,0))
        pantalla.blit(self.yellowRelease,(200,0))
        pantalla.blit(self.blueRelease,(300,0))
        pantalla.blit(self.orangeRelease,(400,0))
        if(self.lista[5]==0):
            self.normalGmPlay(pantalla)
        else:
            self.starpowerOn(pantalla)

    def starpowerOn(self,pantalla):
        pantalla.blit(self.starPowerRelease,(0,0))
        pantalla.blit(self.starPowerRelease,(100,0))
        pantalla.blit(self.starPowerRelease,(200,0))
        pantalla.blit(self.starPowerRelease,(300,0))
        pantalla.blit(self.starPowerRelease,(400,0))
        if(self.lista[0]== 1):
            pantalla.blit(self.StarPowerPressed,(0,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.starPowerSlayer,(0,0))
        if(self.lista[1]== 1):
            pantalla.blit(self.StarPowerPressed,(100,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.starPowerSlayer,(100,0))
        if(self.lista[2]== 1):
            pantalla.blit(self.StarPowerPressed(200,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.starPowerSlayer,(200,0))
        if(self.lista[3]== 1):
            pantalla.blit(self.StarPowerPressed,(300,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.starPowerSlayer,(300,0))
        if(self.lista[4]== 1):
            pantalla.blit(self.StarPowerPressed,(400,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.starPowerSlayer,(400,0)) 

    def normalGmPlay(self,pantalla):
        if(self.lista[0]== 1):
            pantalla.blit(self.greenPressed,(0,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.Slayer,(0,0))
        if(self.lista[1] == 1):
            pantalla.blit(self.redPressed,(100,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.Slayer,(100,0))
        if(self.lista[2]== 1):
            pantalla.blit(self.yellowPressed,(200,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.Slayer,(200,0))
        if(self.lista[3]== 1):
            pantalla.blit(self.bluePressed,(300,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.Slayer,(300,0))
        if(self.lista[4]== 1):
            pantalla.blit(self.orangePressed,(400,0))
            if(self.lista[7]== 1):
                pantalla.blit(self.Slayer,(400,0))