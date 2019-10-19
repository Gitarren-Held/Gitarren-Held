import sys, pygame
from pygame.locals import *
pygame.init()

# Constantes
WIDTH = 640
HEIGHT = 480



class Nota():
    def __init__(self,color,speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        if(color==1):
            self.image = pygame.image.load(8);
            
        if(color==2):
            self.image = pygame.image.load("verde");
           
        if(color==3):
            self.image = pygame.image.load("verde");
           
        if(color==4):
            self.image = pygame.image.load("verde");
            
        if(color==5):
            self.image = pygame.image.load("verde");
        self.nota = self.image.get_rect()
        self.pos = self.image.get_rect().move(0,0)
    
    def move(self):
         self.pos = self.pos.move(0, self.speed)
         if self.pos.bottom >0:
            self.pos.bottom = self.pos.bottom+1


def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error.message:
                raise SystemExit.message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()