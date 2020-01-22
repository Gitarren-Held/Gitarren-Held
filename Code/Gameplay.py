from note import *
from botonera import *
from Arduino import *
from Score import *
from Medidor import *
import random
import time, datetime



WIDTH = 640
HEIGHT = 480
color = (255,0,0)
start_pos = (0, 440)
end_pos = (WIDTH,440)
start_pos2 = (0, 470)
end_pos2 = (WIDTH,470)
width = 1

def main():
    StarPower = False
    #carga cancion por test
    
    scor = 0
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
    direccion = '/dev/cu.usbmodem142401'
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
    #song.play()
    while True:        
        #input arduino (error de lag),(cambiar tiempo de lectura)
        #inp = Leer(direccion)in   s
        #-----------------------------------------------------------------------------
        #ajustes de pygame(fps,fondo,posiciona la guitarra)
        reloj.tick(60)
        screen.fill([0,0,0])
        screen.blit(Guitarra,(-315,-180))
        #-----------------------------------------------------------------------------
        #eventos de pygame,se ejecutan el presionar teclas
        for eventos in pygame.event.get():
            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_z:
                    for i in range(0,len(MatrizLNotas)):
                        if(botonera[0].Active_collider(MatrizLNotas[i],scor,screen)):
                           scor+=1
                    lista[0]=1
                if eventos.key == pygame.K_x:
                    for i in range(0,len(MatrizLNotas)):
                       if(botonera[1].Active_collider(MatrizLNotas[i],scor,screen)):
                           scor+=1
                    lista[1]=1
                if eventos.key == pygame.K_c:
                    for i in range(0,len(MatrizLNotas)):
                        if(botonera[2].Active_collider(MatrizLNotas[i],scor,screen)):
                           scor+=1
                    lista[2]=1
                if eventos.key == pygame.K_v:
                    for i in range(0,len(MatrizLNotas)):
                        if(botonera[3].Active_collider(MatrizLNotas[i],scor,screen)):
                           scor+=1
                    lista[3]=1
                if eventos.key == pygame.K_b:
                    for i in range(0,len(MatrizLNotas)):
                       if(botonera[4].Active_collider(MatrizLNotas[i],scor,screen)):
                           scor+=1
                    lista[4]=1
                if eventos.key == pygame.K_q:
                    StarPower = True      
                if eventos.key == pygame.K_a:
                    StarPower = False
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
        comportamientoBotonera(botonera,lista,screen)
        drawAll(botonera,screen)
        #-----------------------------------------------------------------------------
        #for que genera el movimiento en las notas segun cuantas existan en la cancion
        for i in range(0,len(MatrizNotas)):
            movimientolista(MatrizLNotas[i],screen,botonera,StarPower)
        medidor.evaluar(101)
        score.draw(screen,scor)
        medidor.draw(screen,101)
        #pygame.draw.line(screen, color, start_pos, end_pos, width)
        #pygame.draw.line(screen, color, start_pos2, end_pos2, width)
        pygame.display.flip()
        pygame.display.update()
    return 0 
if __name__ == '__main__':
    pygame.init()
    main()      