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
    def actualizar(self, time,pala_jug,pala_cpu,puntos):#el método actualizar, recibe el parámetro self y el tiempo transcurrido.
        self.rect.centerx += self.speed[0] * time #   OJO: self.rect.centerx: Centro de nuestro rectangulo en x es el valor que tenía 
        self.rect.centery += self.speed[1] * time # Energía = Velocidad (self.speed[0]) * tiempo (tiempo)
        """   Nota:
        - si la parte izquierda del rectángulo de la bola es <= 0 ó la parte derecha del rectángulo de la bola es >= Ancho pantalla.
        la velocidad en el eje X, cambia de signo , conseguimos que se vaya al otro lado.
         """
    #Agregamos los correspondientes puntos por jugador o CPU:
        if self.rect.left <=0:
            puntos[1]+=1#Correspondiente  a puntos del CPU
        if self.rect.right >= width:
            puntos[0]+=1 #Correspondiente a los puntos del jugador. 

        if self.rect.left <= 0 or self.rect.right >=width:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0]*time
        """  pasa lo mismo en el eje Y , velocidad en Y va hace el otro lado."""
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] = -self.speed[1]
            self.rect.centery +=self.speed[1]*time   
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
    #COLISIONEAS: Esto comprueba si el rectángulo del Sprite objeto1 está en contacto con el rectángulo de objeto2: 
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        return puntos

#Creamos la clase PALA, es muy parecido a la bola, solo q le pasamos el parámetro x, para usarlo como self.recr.centerx.
#ya que necesitamos 2 palas, una en la IZQ  otra en la Right, 
#El parámetro X: definimos a q altura del eje x, queremos colocar el Sprite.
class Pala (pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/pala.png');
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = height / 2
        self.speed = 0.5#Solo definimos la velocidad para el eje Y, ya q no se mueve en el eje X.
    """Para mover la pala, aplicamos el método: """
    def mover(self, time, keys):
        if self.rect.top>=0:# Resumiendo comprueban que la pala no se sale de la ventana.
            if keys[K_UP]:#mprueba si la constante K_UP de keys es 1, lo que querría decir que tenemos presionada la tecla de la flecha hacia arriba del teclado.
                self.rect.centery -=self.speed*time
        if self.rect.bottom<=height:#caso de tener la tecla presionada disminuye el valor de centery haciendo que la pala se mueva hacia arriba.
            if keys[K_DOWN]:# pero para abajo y aumentando el valor de centery.
                self.rect.centery += self.speed * time 
    #Método que mueve la pala - Comportamiento complejo ; IA            
    def ia(self, time, ball):
     #comprobamos que ball.speed[0] >= 0, es decir, que la velocidad en el eje x de la pelota sea positiva,
     #  es decir, que la pelota se este moviendo hacia la derecha (hacia la pala de la cpu) y
     #  tambien comprueba que ball.rect.centerx >= WIDTH/2 es decir
     #  que el centro x de la pelota sea mayor o igual que el centro del tablero, es decir,
     #  que la pelota este en el campo de la cpu.
     #Es un condicional que comprueba que la pelota vaya hacia donde está la pala de la cpu y que este en su campo, sino, que no se mueva.
        if ball.speed[0] >= 0 and ball.rect.centerx >= width/2:
            if self.rect.centery < ball.rect.centery:#centery de la pala es menor que el centery de la bola, 
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:#
                self.rect.centery -= self.speed * time

# ---------------------------------------------------------------------
 
# Funciones
#Pondremos la funcion que nos facilite el trabajo con textos y nos automatice el proceso, de esta forma, vamos a poner un fonts general para el juego.
def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("images/DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
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
     # crear un nuevo Sprite para las palas,
    pala_jug = Pala(30)#le pasamos 30 como valor X, centerx estará a 30px del borde derecho de la ventana.
    pala_cpu = Pala(width - 30) # PALA CPU!!
    """ OJO;
    - ahora no le pasamos la imágen, en véz de unas coordenadas como en el fondo--> Le pasamos (0,0).... si le debemos pasar el rect de la bola.
    esto q significa? --> Al momento de mover el rect, moveremos la pelotda de sitio.
    OJO2: importante, ponerla en pantalla después y NO antes que el fondo. pk si pones la pelota y luego poner el fondoencima esta no se verá....
    """
     #Creamos un reloj; sabemos cuanto tiempo a pasado desde la ultima actualización de la pelota y con ello poder situarla en el espacio.
    clock = pygame.time.Clock()
    #Creamos la variable puntos, para almacenar:
    puntos =[0,0] #0:JUGADOR 1:CPU
    
    while True:
        #Ahora necesitamos saber cuanto tiempo pasa cada vez que se ejecuta una interección del bucle,
        # para ello dentro del bucle ponemos como primera línea:
        time = clock.tick(60)#El 60 que se le pasa como parámetro es el framerate, nos aseguramos de q el juego no va a más de la velocidad estipulada. Con ello conseguimos que el juego corra igual en todos los ordenadores.
        """Ahora solo debemos saber que teclas se están pulsando creando la variable keys
        Esto nos devuelve las teclas pulsadas en una lista.
         """
        keys = pygame.key.get_pressed()
        for events in pygame.event.get():
            if events.type == QUIT:
                sys.exit(0)
        #Por último debemos actualizar la posición de la bola antes de actualizarla en la ventana, es decir antes de los screen.blit.
        puntos = bola.actualizar(time,pala_jug,pala_cpu,puntos)#Y con esto ya hemos logrado que nuestra bola detecte si ha chocado contra la pala del jugador en caso afirmativo “rebota”.
        #Por ultimo debemos llamar al método mover en el bucle justo después de actualizar la bola:
        pala_jug.mover(time,keys)
        #llamamos a la IA junto con las llamadas actualziar de la bola y mover de la pala_cpu
        pala_cpu.ia(time, bola)

        #Puntajes!!
        p_jug, p_jug_rect = texto(str(puntos[0]),width/4,40 ) 
        p_cpu,p_cpu_rect = texto(str(puntos[1]),width-width/4,40)


        screen.blit(background_image, (0,0))
        #ahora solo debemos poner en la ventana del juego:REVISAR OJO2
        screen.blit(bola.image, bola.rect)
        screen.blit(pala_jug.image,pala_jug.rect)
        screen.blit(pala_cpu.image, pala_cpu.rect)#Agrego la PALA CPU
        #debemos actualizarlo en pantalla como hacemos siempre.
        screen.blit(p_jug,p_jug_rect)
        screen.blit(p_cpu,p_cpu_rect)
        pygame.display.flip()#Esto lo que hace es actualizar toda la ventana para que se muestren los cambios que han sucedido.
        #print(puntos) muestra por consola el puntaje.,
    return 0
if __name__ == '__main__':
    pygame.init()
    main()