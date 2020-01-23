import pygame

class botonera():
    def __init__(self,x,y):
        self.green = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Verde1.png")), (100,100))
        self.blue = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Azul1.png")), (100,100))
        self.orange = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Naranjo1.png")), (100,100))
        self.yellow = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Amarillo1.png")), (100,100))
        self.red = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Rojo.png")), (100,100))
        self.Slayer = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/ON.png")), (100,100))
       
        self.starPowerRelease = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/starpower.png")), (100,100))
        self.StarPowerPressed = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/starpower2.png")), (100,100))
        self.starPowerSlayer = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/starpower3.png")), (100,100))
        puntaje = 0
    def pos(self,x,y,screen):
        screen.blit(self.green,(150+x,0+y))
        screen.blit(self.red,(180+x,0+y))
        screen.blit(self.yellow,(210+x,0+y))
        screen.blit(self.blue,(240+x,0+y))
        screen.blit(self.orange,(270+x,0+y))
    def __press(self,input):
        if(input[0]==1):
            self.green = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Verde2.png")), (100,100))
        if(input[1]==1):
            self.red = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Rojo2.png")), (100,100))
        if(input[2]==1):
            self.yellow = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Amarillo2.png")), (100,100))
        if(input[3]==1):
            self.blue = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Azul2.png")), (100,100))
        if(input[4]==1):
            self.orange = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Naranja2.png")), (100,100))
        self.green = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Verde1.png")), (100,100))
        self.blue = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Azul1.png")), (100,100))
        self.orange = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Naranjo1.png")), (100,100))
        self.yellow = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Amarillo1.png")), (100,100))
        self.red = pygame.transform.scale((pygame.image.load("Img/Sprites/Botonera/Rojo.png")), (100,100))
        
