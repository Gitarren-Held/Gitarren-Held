import sys, pygame
from pygame.locals import *
from Api import *
import random
# Constantes
# usar velocidades para que tengan distinto ritmo falta agregar metodo para mover el arreglo (sigue usando el arreglo si sirve)
WIDTH = 640
HEIGHT = 480
EASY = 1
MEDIUM = 2
HARD = 3
EXPERT =4
class note(pygame.sprite.Sprite):
    def __init__(self,x,y,tipo):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Img/Notas/"+tipo+".png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [0.5, -0.5]
        self.x = x
        self.y = y
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))
    def Move(self,dificultad):
        if(dificultad=="EASY"):
            dist = EASY
        if(dificultad=="MEDIUM"):
            dist = MEDIUM
        if(dificultad=="HARD"):
            dist = HARD
        if(dificultad=="EXPERT"):
            dist = EXPERT
        if(self.y<HEIGHT):
            print(self.y)
            self.y +=dist
        else:
            self.kill()
    
def ArregloNote(notas):
        list=[]
        fin = False
        while(fin!=True):
            if(notas[0]==1):
                Green = note(0,0,"Green")
                list.append(Green)
            if(notas[1]==1):
                Red = note(50,0,"Red")
                list.append(Red)
            if(notas[2]==1):
                Blue = note(100,0,"Blue")
                list.append(Blue)
            if(notas[3]==1):
                Yellow = note(150,0,"Yellow")
                list.append(Yellow)
            if(notas[4]==1):
                Orange = note(200,0,"Orange")
                list.append(Orange)
        return list
       

        
def Linea(screen,notas,x,y):
    limite = 0 
    if(notas[0]==1):
        Green = note(x+0,y+0,"Green")
    if(notas[1]==1):
        Red = note(x+50,y+0,"Red")
    if(notas[2]==1):
        Blue = note(x+100,y+0,"Blue")
    if(notas[3]==1):
        Yellow = note(x+150,y+0,"Yellow")
    if(notas[4]==1):
        Orange = note(x+200,y+0,"Orange")
    while(limite<HEIGHT-100):
        limite = limite+1
        screen.fill([0,0,0])
        if(notas[0]==1):
            Green.Move("EXPERT")
            Green.draw(screen)
        if(notas[1]==1):
            Red.Move("EXPERT")
            Red.draw(screen)
        if(notas[2]==1):
            Blue.Move("EXPERT")
            Blue.draw(screen)
        if(notas[3]==1):
            Yellow.Move("EXPERT")
            Yellow.draw(screen)
        if(notas[4]==1):
            Orange.Move("EXPERT")
            Orange.draw(screen)
        pygame.display.flip()
        pygame.display.update()



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill([0,0,0])
    input = [1,0,1,1,0,0,0,0]
    #Green=note
    #Red=note
    #Yellow=note
    #Blue=note
    #Orange=note
    pygame.display.set_caption("Pruebas Pygame")
    #Background_image = load_image('images/fondo_pong.png')
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        input = [random.randrange(2),random.randrange(2),random.randrange(2),random.randrange(2),random.randrange(2),0,0,0]
        Linea(screen,input,0,0)
        #Linea(screen,input,Green,Red,Blue,Yellow,Orange,0,0)
        pygame.display.flip()
        pygame.display.update()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()