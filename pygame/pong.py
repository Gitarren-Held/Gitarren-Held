# Módulos
import sys,pygame
from pygame.locals import *
# Constantes
width = 640
height = 480
# Clases
# ---------------------------------------------------------------------
class Bola (pygame.sprite.Sprite):#Creamos la bola, que hereda los métodos de la clase pygaqme.sprite.Sprite. Presenta métodos importantes para manejar los Sprites.
    def __init__(self):#Crea el método que inicia la clase.
        pygame.sprite.Sprite.__init__(self)#Invocamos el método INIT de la clase heredada
        self.image = load_image('images/ball.png',True)#Carga la imágen de la pelota, esta en True, pk la img tiene zonas transparente.
        self.rect = self.image.get_rect()#Obtiene un rectángulo con las dimensiones y posicion de la imágen(self.image)-->Asignando a self.rect
        """Insiso:
        get_rect() --> tiene unos parámetros muy útiles que podemos modificar para posicionar y redimensionar nuestra imagen. SON:
        top, left, bottom, right
        ropleft, bottomleft, topright, bottomright
        midtop, midleft, midbottom, midright
        center, centerx, centery
        size, width, height
        w,h
        example:
        - tenemos self.rect.centerx: devuelve la posición central de la pelota respecto al ancho de la pantalla.
        """
        self.rect.centerx = width/2
        self.rect.centery = height /2
        """ * dejamos el rect.centerx o centery: en la cuál tenemos el centro de la pelota, en el centro de la pantalla"""
        self.speed = [0.5, -0.5]
        """ self.speed : define la velocidad q queremos para la pelota, veloi¡cidad en eje X y en velocidad Y.
         """
    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >=width:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0]*time
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] = -self.speed[1]
            self.rect.centery +=self.speed[1]*time   


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
    #Definimos antes el objeto Bola() antes del bucle.
    bola = Bola()
    """ OJO;
    - ahora no le pasamos la imágen, en véz de unas coordenadas como en el fondo--> Le pasamos (0,0).... si le debemos pasar el rect de la bola.
    esto q significa? --> Al momento de mover el rect, moveremos la pelotda de sitio.
    OJO2: importante, ponerla en pantalla después y NO antes que el fondo. pk si pones la pelota y luego poner el fondoencima esta no se verá....
    """
    while True:
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        screen.blit(background_image, (0,0))
        #ahora solo debemos poner en la ventana del juego:REVISAR OJO2
        screen.blit(bola.image, bola.rect)
        pygame.display.flip()#Esto lo que hace es actualizar toda la ventana para que se muestren los cambios que han sucedido.
    return 0
if __name__ == '__main__':
    pygame.init()
    main()