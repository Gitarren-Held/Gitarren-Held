from note import load_image
import pygame
class Score(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = load_image("Img/Gameplay/puntaje.png", True)
        self.image = pygame.transform.scale(self.image,(100,110))
        self.x = x
        self.y = y
        self.score = 1000
    #score de parametro se suma a lo que ya tenemos
    def draw(self,surface,score):
        self.score += score
        texto = str(score)
        fuente = pygame.font.Font(None, 30)
        texto1 = fuente.render(texto, 0, (255, 255, 255))
        surface.blit(self.image,(self.x,self.y))
        surface.blit(texto1, (45, 125))
        #falta agregar metodo que dibuje y sume puntaje