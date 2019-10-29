import sys, pygame
from pygame.locals import *
import numpy as np
 
# Constantes
WIDTH = 640
HEIGHT = 480
 
# Clases
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error:
                raise SystemExit
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
def matriz(archivo):
    txt=str(archivo+txt)
    with open(txt) as f:
    size=sum(1 for _ in f)
    arch:open(txt,"r")
    linea=arch.readline.strip
    matris=np.zeros((size),(8))
  
    while linea != "":  
        parte=linea.split(",")
        for i in range (size):
            for j in range(8):
                matris[i][j]=parte[j-1]
        linea=arch.readline.strip
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
 
    background_image = load_image("Img/Sprites/Botonera/Verde1.png")
 
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()