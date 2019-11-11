import sys, pygame
from pygame.locals import *
from math import *
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
    txt=str(archivo+".txt")
    cancion = open(txt,"r")
    matris=[]
    for linea in cancion.readlines():
            aux = linea.split(",")
            lis = []
            for num in aux:
                lis.append(int(num))
            matris.append(lis)
    cancion.close()
    return matris
# ---------------------------------------------------------------------