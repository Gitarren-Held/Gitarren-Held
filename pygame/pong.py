# Módulos
import sys,pygame
from pygame.locals import *
# Constantes
width = 640
height = 480
# Clases
# ---------------------------------------------------------------------
class Bola (pygame.sprite.Sprite):#Creamos la bola, que hereda los métodos de la clase pygaqme.sprite.Sprite. Presenta métodos importantes para manejar los Sprites.
    def _init_(self):#Crea el método que inicia la clase.
        pygame.sprite.Sprite._init_(self)#Invocamos el método INIT de la clase heredada
        self.image = load_image("images/ball.png",True)#Carga la imágen de la pelota, esta en True, pk la img tiene zonas transparente.
        self.rect = self.image.get_rect()#Obtiene un rectángulo con las dimensiones y posicion de la imágen(self.image)-->Asignando a self.rect



# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent = False):
    try: image = pygame.image.load(filename)
    #Borramos el message!, no funcionaba!
    except pygame.error:
            raise SystemExit
    image = image.convert()
    if transparent:
            color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
    return image
 
# ---------------------------------------------------------------------
def main():
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Ping Pong")
    background_image = load_image('images/fondo_pong.png')#Como ves no definimos color transparente, porque para el fondo no es necesario.
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        screen.blit(background_image, (0,0))
        pygame.display.flip()#Esto lo que hace es actualizar toda la ventana para que se muestren los cambios que han sucedido.
    return 0
if __name__ == '__main__':
    pygame.init()
    main()