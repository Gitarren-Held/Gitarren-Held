import random,sys
import pygame
from pygame.locals import *

class Opcion:
    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 0))
        self.imagen_destacada = fuente.render(titulo, 1, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 500 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)
    def actualizar(self):
        destino_x = 105
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
        self.image = pygame.image.load('cursor.png').convert_alpha()
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
class Menu:
    "Representa un menú con opciones para un juego"
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font('dejavu.ttf', 20)
        x = 105
        y = 105
        paridad = 1

        self.cursor = Cursor(x - 30, y, 30)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 30
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
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
                self.opciones[self.seleccionado].activar()
        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        self.cursor.seleccionar(self.seleccionado)
        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]
        self.cursor.actualizar()
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""
        self.cursor.imprimir(screen)
        for opcion in self.opciones:
            opcion.imprimir(screen)
class spritesheet:
    	def __init__(self, filename, cols, rows):
		self.sheet = pygame.image.load(filename).convert_alpha()#cargo por parámetro el png
		self.cols = cols#indico las columnas de matriz
		self.rows = rows#indico filas de matriz
		self.totalCellCount = cols * rows#total de celdas
		self.rect = self.sheet.get_rect()#retorna el width y height, dividido en array
		w = self.cellWidth = self.rect.width / cols #Tenemos el ancho
		h = self.cellHeight = self.rect.height / rows#tenemos el largo
		hw, hh = self.cellCenter = (w / 2, h / 2)
		self.cells = list([(index % cols * w, index / cols * h, w, h) for index in range(self.totalCellCount)])
        #Recortamos nuestra matriz, tomando en cuenta el ancho y largo, va desde 0 hasta el tamaño de elementos en la matriz.
        #Tomamos la forma de un rectángulo --> example : [0,0,25,25] -->[25,0,25,25] --> [50,0,25,25] --> [75,0,25,25] -->[0,25,25,25] 
        #Ejemplo: colum 0 fila 0, colum 25 fila 0, colum 50 fila 0,  colum 75 fila -->Si es de 25 pixeles la img
		self.handle = list([#Creamos una lista de Handle, q es básicamente an offset to the X and Y coordinate 
			(0, 0), (-hw, 0), (-w, 0),
			(0, -hh), (-hw, -hh), (-w, -hh),
			(0, -h), (-hw, -h), (-w, -h),])	#tomo 9 posiciones, arriba, abajo, derecha,izquierda, etc.
    #el método draws es una surface que proporcionamos parámetros de entrada, el parámetro de índice de celda señala que un elemento dentro de la lista de rectángulos se creó antes de la posición indicada por X e Y en la superficie que vamos a cortar y
	def draw(self, surface, cellIndex, x, y, handle = 0):
		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
        #Recordar! handle es cero del valor de offset son cero if the handle
        #foutthe image is centralizada, 
def comenzar_nuevo_juego():
    print(" Función que muestra un nuevo juego.")
def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")
def creditos():
    print (" Función que muestra los creditos del programa.")
def salir_del_programa():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)

if __name__ == '__main__':
    salir = False
    opciones = [
        ("Single", comenzar_nuevo_juego),
        ("Versus", mostrar_opciones),
        ("Modo Carrera", creditos),
        ("Salir", salir_del_programa)
        ]
    pygame.font.init()
    W, H = 800, 800
    HW, HH = int(W / 2), int(H / 2)
    AREA = W * H
    CLOCK = pygame.time.Clock()
    DS = pygame.display.set_mode((W, H))
    pygame.display.set_caption("code.Pylet - Sprite Sheets")
    FPS = 10 #Los cuadros por segundo
    s = spritesheet("fuego.png", 1, 3) # 7 Columnas y 4 filas
    index = 0
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)   
    CENTER_HANDLE = 4 
    screen = pygame.display.set_mode((320, 200))
    fondo = pygame.image.load("fondo.png").convert()
    menu = Menu(opciones)
    while not salir:
        for e in pygame.event.get():
            if e.type == QUIT:
                salir = True
        #Traemos el metodo draw para correr elmmétodo de la clase
        s.draw(DS, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
        index += 1
        pygame.draw.circle(DS, WHITE, (HW, HH), 2, 0)
        pygame.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)
        #screen.blit(fondo, (0, 0))
        menu.actualizar()
        menu.imprimir(screen)
        pygame.display.flip()
        pygame.time.delay(0)