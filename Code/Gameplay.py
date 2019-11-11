from note import *
from botonera import *
from Arduino import *
from Score import *
from Medidor import *
import random,pygame,time
def main():
    song = load_sound("test")
    fps=0
    cont=1
    Guitarra = pygame.image.load("Img/Sprites/Guitarra/guitar"+str(cont)+".png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guitarrend Held")
    #botonera
    botonera = BotoneraCompleta()
    direccion = '/dev/cu.usbmodem144401'
    lista = [0,0,0,0,0,0,0,0]
    #score
    score = Score(20,120)
    medidor = Medidor(500,120)
    #se crean dos arreglo
    MatrizLNotas=[]
    #se rellenan estos arreglos con 1000 datos (deberia cargar las lineas de la cancion)
    #crea cada vez una linea ( inputArduino) nueva 
    MatrizNotas = matriz("Code/test-song1")
    #for i in MatrizNotas:
        #print(i)
    clock = pygame.time.Clock() 
    for i in range(0,len(MatrizNotas)):
        #crea las lineas de "notas" 
        # i comparar i+1 mismo valor 
        #MatrizNotas[i]--> Fila de la matriz
        LineaN = Linea(screen,MatrizNotas[i],150,(0-(80*i)))
        MatrizLNotas.append(LineaN)   
    #song.play()
    while True:
        #inp = Leer(direccion)
        screen.fill([0,0,0])
        screen.blit(Guitarra,(-315,-180))
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
        comportamientoBotonera(botonera,lista)
        drawAll(botonera,screen)
        #for que genera el movimiento en las notas segun cuantas existan en la cancion
        for i in range(0,len(MatrizNotas)):
            movimientolista(MatrizLNotas[i],screen)
        score.draw(screen,0)
        medidor.evaluar(101)
        medidor.draw(screen,101)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
        #Cambio de Screen de la guitarra 
        if fps>3:    
            if cont<16:
                cont+=1
                Guitarra = pygame.image.load("Img/Sprites/Guitarra/guitar"+str(cont)+".png")
                Guitarra=pygame.transform.scale(Guitarra,(1280,720))
            else:
                cont=1
                Guitarra = pygame.image.load("Img/Sprites/Guitarra/guitar"+str(cont)+".png")
                Guitarra=pygame.transform.scale(Guitarra,(1280,720))
            fps=0
        fps+=1
    pygame.quit()
    return 0 
if __name__ == '__main__':
    pygame.init()
    main()