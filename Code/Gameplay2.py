from note import *
from botonera import *
from Arduino import *
from Score import *
from Medidor import *
import random
import time, datetime



WIDTH = 640
HEIGHT = 480
color = (0,0,0)
start_pos = (0, 460)
end_pos = (WIDTH,460)
start_pos2 = (0, 470)
end_pos2 = (WIDTH,470)
width = 1
shape_color = (40, 210, 250)


def GamePlayStart2(screen):
    cadenaNotas = 0
    multiplicador=1
    cantStarPower=50
    isActiveStartPower = False
    EndStartPower=0
    StarPower = False
    game=True
    Cantidad_notas=0
    Dibuj = True
    #carga cancion por test
    scor = 0
#    song = load_sound("test")
    #-----------------------------------------------------------------------------
    #carga img de guitarra ( fondo donde van las notas) y luego le da un tamaño
    Guitarra = pygame.image.load("Img/Gameplay/Guitarra.png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    #-----------------------------------------------------------------------------
    #detalles de pantalla pygame reloj = fps 
    reloj = pygame.time.Clock()
    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
    #---------
    cantidadNotasTotales = len(MatrizNotas) * len(MatrizLNotas) 
    #termina de cargar la cancion en memoria
    #-----------------------------------------------------------------------------
    #comienza el loop y por lo tanto la cancion se ejecuta
    #song.play()
    while (game):    
        #input arduino (error de lag),(cambiar tiempo de lectura)
        #inp = Leer(direccion)in   s
        #-----------------------------------------------------------------------------
        #ajustes de pygame(fps,fondo,posiciona la guitarra)
        reloj.tick(60)
        screen.fill([34,51,59])
        screen.blit(Guitarra,(-315,-180))
        #-----------------------------------------------------------------------------
        #eventos de pygame,se ejecutan el presionar teclas
        for eventos in pygame.event.get():
            if(Dibuj):
                if eventos.type == pygame.KEYDOWN:

                    if eventos.key == pygame.K_z:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i]) = botonera[0].Active_collider(MatrizLNotas[i],scor,screen)
                            if(coll):
                                cadenaNotas=cadenaNotas+1
                                if(cadenaNotas<20):
                                    if(StarPower):
                                        multiplicador = 4
                                    else:
                                        multiplicador = 1
                                    
                                if((cadenaNotas>20)and(cadenaNotas<30)):
                                    if(StarPower):
                                        multiplicador = 6
                                    else:
                                        multiplicador = 2
                                if((cadenaNotas>30)and(cadenaNotas<40)):
                                    if(StarPower):
                                        multiplicador = 8
                                    else:
                                        multiplicador = 3
                                if(cadenaNotas>40):
                                    if(StarPower):
                                        multiplicador = 10
                                    else:
                                        multiplicador = 4
                                for j in range(0,len(MatrizLNotas[i])):
                                    if(MatrizLNotas[i][j].bonus == 0):
                                        scor =scor +2
                                        cantStarPower = cantStarPower +3
                                    
                                if(StarPower):
                                    scor = scor+(1 * multiplicador)
                                else:
                                    scor = scor+1
                            else:
                                cadenaNotas = 0
                        lista[0]=1
                    if eventos.key == pygame.K_x:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i]) = botonera[1].Active_collider(MatrizLNotas[i],scor,screen)
                            if(coll):
                                cadenaNotas=cadenaNotas+1
                                if(cadenaNotas<20):
                                    if(StarPower):
                                        multiplicador = 4
                                    else:
                                        multiplicador = 1
                                    
                                if((cadenaNotas>20)and(cadenaNotas<30)):
                                    if(StarPower):
                                        multiplicador = 6
                                    else:
                                        multiplicador = 2
                                if((cadenaNotas>30)and(cadenaNotas<40)):
                                    if(StarPower):
                                        multiplicador = 8
                                    else:
                                        multiplicador = 3
                                if(cadenaNotas>40):
                                    if(StarPower):
                                        multiplicador = 10
                                    else:
                                        multiplicador = 4
                                for j in range(0,len(MatrizLNotas[i])):
                                    if(MatrizLNotas[i][j].bonus == 0):
                                        scor =scor+2
                                        cantStarPower = cantStarPower +3
                                if(StarPower):
                                    scor = scor+(1 * multiplicador)
                                else:
                                    scor = scor+1
                            else:
                                cadenaNotas = 0
                            lista[1]=1
                    if eventos.key == pygame.K_c:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i]) = botonera[2].Active_collider(MatrizLNotas[i],scor,screen)
                            if(coll):
                                cadenaNotas=cadenaNotas+1
                                if(cadenaNotas<20):
                                    if(StarPower):
                                        multiplicador = 4
                                    else:
                                        multiplicador = 1
                                    
                                if((cadenaNotas>20)and(cadenaNotas<30)):
                                    if(StarPower):
                                        multiplicador = 6
                                    else:
                                        multiplicador = 2
                                if((cadenaNotas>30)and(cadenaNotas<40)):
                                    if(StarPower):
                                        multiplicador = 8
                                    else:
                                        multiplicador = 3
                                if(cadenaNotas>40):
                                    if(StarPower):
                                        multiplicador = 10
                                    else:
                                        multiplicador = 4
                                for j in range(0,len(MatrizLNotas[i])):
                                    if(MatrizLNotas[i][j].bonus == 0):
                                        scor =scor+2
                                        cantStarPower = cantStarPower +3
                                if(StarPower):
                                    scor = scor+(1 * multiplicador)
                                else:
                                    scor = scor+1
                            else:
                                cadenaNotas = 0
                            lista[2]=1
                    if eventos.key == pygame.K_v:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i]) = botonera[3].Active_collider(MatrizLNotas[i],scor,screen)
                            if(coll):
                                cadenaNotas=cadenaNotas+1
                                if(cadenaNotas<20):
                                    if(StarPower):
                                        multiplicador = 4
                                    else:
                                        multiplicador = 1
                                if((cadenaNotas>20)and(cadenaNotas<30)):
                                    if(StarPower):
                                        multiplicador = 6
                                    else:
                                        multiplicador = 2
                                if((cadenaNotas>30)and(cadenaNotas<40)):
                                    if(StarPower):
                                        multiplicador = 8
                                    else:
                                        multiplicador = 3
                                if(cadenaNotas>40):
                                    if(StarPower):
                                        multiplicador = 10
                                    else:
                                        multiplicador = 4
                                for j in range(0,len(MatrizLNotas[i])):
                                    if(MatrizLNotas[i][j].bonus == 0):
                                        cantStarPower = cantStarPower +3
                                        scor = scor+2
                                if(StarPower):
                                    scor = scor+(1 * multiplicador)
                                else:
                                    scor = scor+1
                            else:
                                cadenaNotas = 0
                            lista[3]=1
                    if eventos.key == pygame.K_b:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i]) = botonera[4].Active_collider(MatrizLNotas[i],scor,screen)
                            if(coll):
                                cadenaNotas=cadenaNotas+1
                                if(cadenaNotas<20):
                                    if(StarPower):
                                        multiplicador = 4
                                    else:
                                        multiplicador = 1
                                    
                                if((cadenaNotas>20)and(cadenaNotas<30)):
                                    if(StarPower):
                                        multiplicador = 6
                                    else:
                                        multiplicador = 2
                                if((cadenaNotas>30)and(cadenaNotas<40)):
                                    if(StarPower):
                                        multiplicador = 8
                                    else:
                                        multiplicador = 3
                                if(cadenaNotas>40):
                                    if(StarPower):
                                        multiplicador = 10
                                    else:
                                        multiplicador = 4
                                for j in range(0,len(MatrizLNotas[i])):
                                    if(MatrizLNotas[i][j].bonus == 0):
                                        cantStarPower = cantStarPower +3
                                        scor = scor+2
                                if(StarPower):
                                    scor = scor+(1 * multiplicador)
                                else:
                                    scor = scor+1
                            else:
                                cadenaNotas = 0
                            lista[4]=1
                    if eventos.key == pygame.K_q:
                        if(cantStarPower>0):
                            isActiveStartPower = True  
                            multiplicador = 4   
                        else:
                            isActiveStartPower = False
                            multiplicador=1 
                    if eventos.key == pygame.K_a:
                        isActiveStartPower = False
                        multiplicador=1
                    if eventos.key == pygame.K_p:
                        game = False
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
        if(isActiveStartPower):
                StarPower = isActiveStartPower
                if(cantStarPower<0):
                        StarPower = False  
        else:
            isActiveStartPower=False
            StarPower = False    
        for i in range(0,len(MatrizNotas)):
            (Cantidad_notas,cantStarPower) = movimientolista(MatrizLNotas[i],screen,botonera,StarPower,Cantidad_notas,Dibuj,cantStarPower,cadenaNotas)
        medidor.evaluar(101)
        score.draw(screen,scor,multiplicador,cadenaNotas)
        medidor.draw(screen,101)
        #Fin
        if(Cantidad_notas > 200):
                Dibuj = False;
                fondo = pygame.image.load("Img/Gameplay/fin.png")
                fondo=pygame.transform.scale(fondo,(1280,720))
                screen.blit(fondo,(0,0))
                #calculos
                por = "{0:.4f}".format((scor * 100)/cantidadNotasTotales)
                texto = "Completado :"+str(por)+"%"
                aciertos = "Aciertos :"+str(scor)
                errores = "Errores :"+str(cantidadNotasTotales-scor)
                fuente = pygame.font.Font(None, 60)
                texto1 = fuente.render(texto, 0, (255, 0, 0))
                texto2 = fuente.render(aciertos, 0, (255, 0, 0))
                texto3 = fuente.render(errores, 0, (255, 0, 0))
                screen.blit(texto1, (110,120))
                screen.blit(texto2, (110,220))
                screen.blit(texto3, (110,340))
        #pygame.draw.line(screen, color, start_pos2, end_pos2, width)
       
        pygame.draw.rect(screen, shape_color, ((10, 50), (130, 20)), 3)
        pygame.draw.rect(screen, shape_color, pygame.Rect((10, 50, cantStarPower, 20)), 0)
        pygame.display.flip()
        pygame.display.update()
       
        
    return 0

#if __name__ == '__main__':
#    pygame.init()
 #   GamePlayStart()      