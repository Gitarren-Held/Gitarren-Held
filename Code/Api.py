import sys, pygame
from pygame.locals import *
from math import *

#Carga una imagen
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error:
                raise SystemExit
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
#lee un archivo y devuelve una matriz con las lineas 
def matriz(archivo):
    txt=str(archivo+".txt")
    cancion = open(txt,"r")
    mat=[]
    for linea in cancion.readlines():
            aux = linea.split(",")
            lis = []
            for num in aux:
                s=int(num)   
                lis.append(s)
            mat.append(lis)
    cancion.close()
    return mat
