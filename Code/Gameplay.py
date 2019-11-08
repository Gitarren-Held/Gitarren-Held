from note import *
from botonera import *
from Arduino import *
from Score import *
from Medidor import *
import random
WIDTH = 640
HEIGHT = 480

def main():
    #carga cancion por test
    song = load_sound("test")
    #-----------------------------------------------------------------------------
    #carga img de guitarra ( fondo donde van las notas) y luego le da un tamaño
    Guitarra = pygame.image.load("Img/Gameplay/Guitarra.png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    #-----------------------------------------------------------------------------
    #detalles de pantalla pygame reloj = fps 
    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    #-----------------------------------------------------------------------------
    #botonera
    botonera = BotoneraCompleta()
    #-----------------------------------------------------------------------------
    direccion = '/dev/cu.usbmodem144401'
    lista = [0,0,0,0,0,0,0,0]
    #score y medidor
    score = Score(20,120)
    medidor = Medidor(500,120)
    #-----------------------------------------------------------------------------
    #se crean dos arreglo
    MatrizLNotas=[]
    #se rellenan estos arreglos con 1000 datos (deberia cargar las lineas de la cancion)
    #crea cada vez una linea ( inputArduino) nueva 
    MatrizNotas = matriz("Code/test-song1")
    #for i in MatrizNotas:
        #print(i)
    for i in range(0,len(MatrizNotas)):
        #crea las lineas de "notas" 
        # i comparar i+1 mismo valor 
        LineaN = Linea(screen,MatrizNotas[i],150,(0-(80*i)))
        MatrizLNotas.append(LineaN)
    #termina de cargar la cancion en memoria
    #-----------------------------------------------------------------------------
    #comienza el loop y por lo tanto la cancion se ejecuta
    song.play()
    while True:
        #input arduino (error de lag)
        #inp = Leer(direccion)
        #-----------------------------------------------------------------------------
        #ajustes de pygame(fps,fondo,posiciona la guitarra)
        reloj.tick(60)
        screen.fill([0,0,0])
        screen.blit(Guitarra,(-315,-180))
        #-----------------------------------------------------------------------------
        #eventos de pygame,se ejecutan el precionar teclas
        for eventos in pygame.event.get():
            if eventos.type == pygame.KEYDOWN:
            # Resuelve que ha sido una tecla de flecha, por lo que
            # ajusta la velocidad.
                if eventos.key == pygame.K_z:
                    lista[0]=1
                if eventos.key == pygame.K_x:
                    lista[1]=1
                if eventos.key == pygame.K_c:
                    lista[2]=1
                if eventos.key == pygame.K_v:
                    lista[3]=1
                if eventos.key == pygame.K_b:
                    lista[4]=1
            if eventos.type == pygame.KEYUP:
            # Resuelve que ha sido una tecla de flecha, por lo que
            # ajusta la velocidad.
                if eventos.key == pygame.K_z:
                    lista[0]=0
                if eventos.key == pygame.K_x:
                    lista[1]=0
                if eventos.key == pygame.K_c:
                    lista[2]=0
                if eventos.key == pygame.K_v:
                    lista[3]=0
                if eventos.key == pygame.K_b:
                    lista[4]=0
            if eventos.type == QUIT:
                sys.exit(0) 
        #-----------------------------------------------------------------------------
        #ejecuta comportaminetobotomnera con la lista creada a partir del teclado y luego la dibuja
        comportamientoBotonera(botonera,lista)
        drawAll(botonera,screen)
        #-----------------------------------------------------------------------------
        #for que genera el movimiento en las notas segun cuantas existan en la cancion
        for i in range(0,len(MatrizNotas)):
            movimientolista(MatrizLNotas[i],screen)
        score.draw(screen,0)
        medidor.evaluar(101)
        medidor.draw(screen,101)
        pygame.display.flip()
        pygame.display.update()
    return 0 
if __name__ == '__main__':
    pygame.init()
    main()