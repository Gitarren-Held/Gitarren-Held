import pygame,sys
from pygame.locals import *
# ---------------------------------------------------------------------
#Constantes
# ---------------------------------------------------------------------
width = 640
height = 480
HW, HH = int(width / 2), int(height / 2)
black = (0,0,0,250)
white = (255, 255, 255, 255)
# ---------------------------------------------------------------------
#Clases:
class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols 
        h = self.cellHeight = self.rect.height / rows
        hw, hh = self.cellCenter = (w / 2, h / 2)
        self.cells = list([(index % cols * w, index / cols * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([(0, 0), (-hw, 0), (-w, 0),(0, -hh), (-hw, -hh), (-w, -hh),(0, -h), (-hw, -h), (-w, -h),])
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
#Funciones:s
def load_image(filename,transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    imgage = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color,RLEACCEL)
    return image
# ---------------------------------------------------------------------
def main():
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Sprites Guitarrista")
    DS = pygame.display.set_mode((width, height))
    background_image = load_image('images/sidecar.jpg')
    clock = pygame.time.Clock()
    fps=8
    sprite = spritesheet('images/band.png', 1, 4) # 1 Columnas y 3 filas
    CENTER_HANDLE = 4#Centralizamos la imagen en el plano carteseano X/Y
    index = 0
    while True:
        sprite.draw(DS, index % sprite.totalCellCount, 330, 300, CENTER_HANDLE)#manejo x e y del Sprite
        index += 1
        pygame.draw.circle(DS, white, (HW, HH), 1, 0)
        pygame.display.update()
        clock.tick(fps)
        screen.blit(background_image, (0,0)) #DS.fill(white)      
        keys = pygame.key.get_pressed()
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        pygame.display.flip()
        
if __name__=='__main__':
    pygame.init()
    main()