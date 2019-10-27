#Módulos
import random
import pygame,sys
from pygame.locals import *
#Funciones privadas:
def cancion1():
    print ("Selecciono la cancion 1 ")
def cancion2():
    print ("Selecciono la cancion 2 ")
def cancion3():
    print ("Selecciono la cancion 3 ")
def cancion4():
    print ("Selecciono la cancion 4 ")
def cancion5():
    print ("Selecciono la cancion 5 ")
#Constantes privadas:
dificultades = [("Easy", cancion1),("Medium", cancion2),("Hard", cancion3),("Expert", cancion4)]
width = 640
height = 480
black = (0, 0, 0)
gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
class dificulty:
    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (black))#acá cambiamos el color de letra normal
        self.imagen_destacada = fuente.render(titulo, 2, (blue))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)
    def actualizar(self):
        destino_x = 90
        self.x += (destino_x - self.x) / 5.0
        self.rect.x = int(self.x)
    def imprimir(self, screen):
        screen.blit(self.image, self.rect)
    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal
    def activar(self):
        self.funcion_asignada()
class Cursor:
    def __init__(self, x, y, dy):
        self.image = pygame.image.load('images/cursor.png').convert_alpha()
        #self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)
    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)
    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy
    def imprimir(self, screen):
        screen.blit(self.image, self.rect)
class Menudificulty:
    #"Representa el menú, de guitar Hero"
    def __init__(self, dificultades):
        self.dificultades = []
        fuente = pygame.font.Font('images/white-space.ttf', 25)
        x = 80 #posicion inicial del menú
        y = 260
        paridad = 1
        self.cursor = Cursor(x - 30, y, 30)
        for titulo, funcion in dificultades:
            self.dificultades.append(dificulty(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1
        self.seleccionado = 0
        self.total = len(self.dificultades)
        self.mantiene_pulsado = False
    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
        k = pygame.key.get_pressed()
        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.dificultades[self.seleccionado].activar()
        # procura que el cursor esté entre las dificultades permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        self.cursor.seleccionar(self.seleccionado)
        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]
        self.cursor.actualizar()
        for o in self.dificultades:
            o.actualizar()
    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""
        self.cursor.imprimir(screen)
        for dificulty in self.dificultades:
            dificulty.imprimir(screen)
def solo():
    pygame.font.init()
    screen = pygame.display.set_mode((width, height))
    fondo = pygame.image.load('imagesInicio/Dificulty.JPG').convert() 
    fondo = pygame.transform.scale(fondo,(width,height))#Escalamos la imagen en Pygame
    menu = Menudificulty(dificultades)
    pygame.display.set_caption('Guitar Hero') 
    salir = False
    while not salir:
        for event in pygame.event.get():
            if event.type == QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
            #En el caso de que se apreta la letra q , se cierra la ventana.
                if event.key == pygame.K_q:
                    salir = True
        screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(0)
    return 0