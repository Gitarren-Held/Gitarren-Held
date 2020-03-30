import math, random, sys
import pygame
from pygame.locals import *
# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
# define display surface			
W, H = 800, 800
HW, HH = int(W / 2), int(H / 2)
AREA = W * H
# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Sprite Sheets")
FPS = 10 #Los cuadros por segundo
# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
#Definimos la clase Spritsheets para poder leer las columnas y filas 
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
#Creamos la Instancia de la clase Spritesheet 
s = spritesheet("fuego.png", 1, 3) # 7 Columnas y 4 filas
CENTER_HANDLE = 4#Centralizamos la imagen en el plano carteseano X/Y
index = 0
# main loop
while True:
	events()
    #Traemos el metodo draw para correr elmmétodo de la clase
	s.draw(DS, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
	index += 1
	pygame.draw.circle(DS, WHITE, (HW, HH), 2, 0)
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)