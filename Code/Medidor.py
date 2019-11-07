from note import load_image
import pygame
class Medidor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = load_image("Img/Gameplay/Starpower.png", True)
        self.image = pygame.transform.scale(self.image,(117,93))
        self.x = x
        self.y = y
        #valor = 100 verde
        # 20 <valor < 100 = amarillo
        # valor < 20 = rojo        
        self.score = 0
    def draw(self,surface,score):
        surface.blit(self.image,(self.x,self.y))
        #falta agregar metodo que dibuje y sume puntaje
    def __score(self,score):
        if(score > 100):
            self.image = load_image("Img/Gameplay/StarpowerBlue.png", True)
            self.image = pygame.transform.scale(self.image,(117,93))
        if((score<100)and(score>20)):
            self.image = load_image("Img/Gameplay/StarpowerYellow.png", True)
            self.image = pygame.transform.scale(self.image,(117,93))
        if(score<20):
            self.image = load_image("Img/Gameplay/StarpowerRed.png", True)
            self.image = pygame.transform.scale(self.image,(117,93))
    def evaluar(self,score):
        self.__score(score)