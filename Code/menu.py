import os
from random import randrange
import pygame
import pygameMenu
import random
import time, datetime 
import sys

sys.path.insert(0, '../../')
from note import *
from botonera import *
from Arduino import *
from Score import *
from Medidor import *
from Gameplay import GamePlayStart

import random
import time, datetime 


# -----------------------------------------------------------------------------
# Constantes globales
# -----------------------------------------------------------------------------
COLOR_BACKGROUND = (0, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
DIFFICULTY = ['EASY']
FPS = 60.0
MENU_BACKGROUND_COLOR = (0, 128, 0)
WINDOW_SIZE = (640, 480)#(640, 480)
clock = None
main_menu = None
surface = None
WIDTH = 640
HEIGHT = 480
start_pos = (0, 460)
end_pos = (WIDTH,460)
start_pos2 = (0, 470)
end_pos2 = (WIDTH,470)
width = 1
surface = pygame.display.set_mode(WINDOW_SIZE)
color = (0,0,0)
shape_color = (40, 210, 250)


# -----------------------------------------------------------------------------
# Metodos del MENU
# -----------------------------------------------------------------------------
def change_difficulty(value, difficulty):
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :type value: tuple
    :param difficulty: Optional parameter passed as argument to add_selector
    :type difficulty: basestring
    :return: None
    """
    selected, index = value
    print('Selected difficulty: "{0}" ({1}) at index {2}'.format(selected, difficulty, index))
    DIFFICULTY[0] = difficulty#0 easy 1 medium 2 hard

def random_color():
    """
    Return random color.
    :return: Color tuple
    :rtype: tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)

def play_function(difficulty, font, test=False):
    """
    Main game function.
    :param difficulty: Difficulty of the game
    :type difficulty: basestring
    :param font: Pygame font
    :type font: pygame.font.FontType
    :param test: Test method, if true only one loop is allowed
    :type test: bool
    :return: None
    """
    assert isinstance(difficulty, (tuple, list))
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    # Define globals
    global main_menu
    global clock
    

    if difficulty == 'EASY':
        f = font.render('Playing as a kid (easy)', 1, COLOR_WHITE)
        cancion = "Code/test-song1"
        Gameplay(cancion)
    elif difficulty == 'MEDIUM':
        f = font.render('Playing as a kid (medium)', 1, COLOR_WHITE)
        cancion = "Code/test-song2"
        Gameplay(cancion)
    elif difficulty == 'HARD':
        f = font.render('Playing as a champion (hard)', 1, COLOR_WHITE)
        cancion = "Code/test-song3"
        Gameplay(cancion)
    elif difficulty == 'HARD2':
        f = font.render('Playing as a champion (hard)', 1, COLOR_WHITE)
        cancion = "Code/test-song4"
        Gameplay(cancion)
    elif difficulty == 'HARD3':
        f = font.render('Playing as a champion (hard)', 1, COLOR_WHITE)
        cancion = "Code/test-song5"
        Gameplay(cancion)
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    #bg_color = random_color()
    #f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()
                    # Quit this function, then skip to loop of main-menu on line 317
                    return

        # Pass events to main_menu
        main_menu.mainloop(events)

        # Continue playing
        #surface.fill(bg_color)
        #surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()

        # If test returns
        if test:
            break

def main_background():
    global surface
    surface.fill(COLOR_BACKGROUND)
def main(test=False):
    """
    Main program.
    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame surface and objects
    pygame.display.set_caption(' Guitarren Held ')
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus
    # -------------------------------------------------------------------------

    # Play menu
    play_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.7),
                                menu_width=int(WINDOW_SIZE[0] * 0.7),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Seleccione Cancion',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    play_submenu = pygameMenu.Menu(surface,
                                   bgfun=main_background,
                                   color_selected=COLOR_WHITE,
                                   font=pygameMenu.font.FONT_BEBAS,
                                   font_color=COLOR_BLACK,
                                   font_size=30,
                                   menu_alpha=100,
                                   menu_color=MENU_BACKGROUND_COLOR,
                                   menu_height=int(WINDOW_SIZE[1] * 0.5),
                                   menu_width=int(WINDOW_SIZE[0] * 0.7),
                                   option_shadow=False,
                                   title='Dificultad',
                                   window_height=WINDOW_SIZE[1],
                                   window_width=WINDOW_SIZE[0]
                                   )
    play_submenu.add_selector('Seleccione: ',#Cambiamos las dificultados por las canciones
                           [('- Fácil', 'EASY'),
                            ('- Medio', 'EASY'),
                            ('- Difícil', 'EASY')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')
    play_submenu.add_option('Salir', pygameMenu.events.BACK)

    play_menu.add_option('Comenzar',  
                         play_function,
                         DIFFICULTY,
                         pygame.font.Font(pygameMenu.font.FONT_FRANCHISE, 30))
    play_menu.add_selector('',#Cambiamos las dificultados y las canciones
                           [('1 - Corazon espinado', 'EASY'),
                            ('2 - The Man Who Sold The World', 'MEDIUM'),
                            ('3 - De Musica Ligera', 'HARD2'),
                            ('4 - Back in Black', 'HARD3'),
                            ('5 - ThunderStruck', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')
                           
    play_menu.add_option('Dificultad', play_submenu)
    play_menu.add_option('Volver a menú', pygameMenu.events.BACK)

    # Main del menu
    main_menu = pygameMenu.Menu(surface,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=MENU_BACKGROUND_COLOR,
                                menu_height=int(WINDOW_SIZE[1] * 0.6),
                                menu_width=int(WINDOW_SIZE[0] * 0.6),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Main menu',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )
    main_menu.add_option('Jugar', play_menu)
    
    main_menu.add_option('Salir', pygameMenu.events.EXIT)

    #Configura el main del menu
    main_menu.set_fps(FPS)

    # -------------------------------------------------------------------------
    # Main del ciclo
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        main_menu.mainloop(events, disable_loop=test)

        # Flip surface
        pygame.display.flip()

        # At first losop returns
        if test:
            break
# -----------------------------------------------------------------------------
# Gameplays
# -----------------------------------------------------------------------------
def Gameplay(cancion):
    fin = False
    PuntajeMedidor = 70
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
    song = load_sound("test")
    #-----------------------------------------------------------------------------
    #carga img de guitarra ( fondo donde van las notas) y luego le da un tamaño
    Guitarra = pygame.image.load("Img/Gameplay/Guitarra.png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    #-----------------------------------------------------------------------------
    #detalles de pantalla pygame reloj = fps 
    reloj = pygame.time.Clock()
    #surface = pygame.display.set_mode((WIDTH, HEIGHT))
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
    MatrizNotas = matriz(cancion)
    #for i in MatrizNotas:
        #print(i)
    for i in range(0,len(MatrizNotas)):
        #crea las lineas de "notas" 
        # i comparar i+1 mismo valor 
        LineaN = Linea(surface,MatrizNotas[i],150,(0-(80*i)))
        MatrizLNotas.append(LineaN)
    #---------
    cantidadNotasTotales = len(MatrizNotas) * len(MatrizLNotas) 
    #termina de cargar la cancion en memoria
    #-----------------------------------------------------------------------------
    #comienza el loop y por lo tanto la cancion se ejecuta
    song.play()
    while (game):    
        #input arduino (error de lag),(cambiar tiempo de lectura)
        #inp = Leer(direccion)in   s
        #-----------------------------------------------------------------------------
        #ajustes de pygame(fps,fondo,posiciona la guitarra)
        reloj.tick(60)
        surface.fill([34,51,59])
        surface.blit(Guitarra,(-315,-180))
        #-----------------------------------------------------------------------------
        #eventos de pygame,se ejecutan el presionar teclas
        for eventos in pygame.event.get():
            if(Dibuj):
                if eventos.type == pygame.KEYDOWN:

                    if eventos.key == pygame.K_z:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i],PuntajeMedidor) = botonera[0].Active_collider(MatrizLNotas[i],scor,surface,PuntajeMedidor)
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
                            (coll,MatrizLNotas[i],PuntajeMedidor) = botonera[1].Active_collider(MatrizLNotas[i],scor,surface,PuntajeMedidor)
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
                                    PuntajeMedidor = PuntajeMedidor-1
                                    scor = scor+1
                            else:
                                cadenaNotas = 0
                            lista[1]=1
                    if eventos.key == pygame.K_c:
                        for i in range(0,len(MatrizLNotas)):
                            (coll,MatrizLNotas[i],PuntajeMedidor) = botonera[2].Active_collider(MatrizLNotas[i],scor,surface,PuntajeMedidor)
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
                            (coll,MatrizLNotas[i],PuntajeMedidor) = botonera[3].Active_collider(MatrizLNotas[i],scor,surface,PuntajeMedidor)
                            if(coll):
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
                            (coll,MatrizLNotas[i],PuntajeMedidor) = botonera[4].Active_collider(MatrizLNotas[i],scor,surface,PuntajeMedidor)
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
        comportamientoBotonera(botonera,lista,surface)
        drawAll(botonera,surface)
       
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
            (Cantidad_notas,cantStarPower) = movimientolista(MatrizLNotas[i],surface,botonera,StarPower,Cantidad_notas,Dibuj,cantStarPower,cadenaNotas)
        medidor.evaluar(PuntajeMedidor)
        score.draw(surface,scor,multiplicador,cadenaNotas)
        medidor.draw(surface,PuntajeMedidor)
        #Fin
        if(PuntajeMedidor<0):
            fin = True
        if((Cantidad_notas > 200)or fin):
                song.stop();
                Dibuj = False;
                fondo = pygame.image.load("Img/Gameplay/fin.png")
                fondo=pygame.transform.scale(fondo,(1280,720))
                surface.blit(fondo,(0,0))
                #calculos
                por = "{0:.4f}".format((scor * 100)/cantidadNotasTotales)
                texto = "Completado :"+str(por)+"%"
                aciertos = "Aciertos :"+str(scor)
                errores = "Errores :"+str(cantidadNotasTotales-scor)
                salir = "Aprete 'esc' para volver!"
                fuente = pygame.font.Font(None, 60)
                texto1 = fuente.render(texto, 0, (255, 0, 0))
                texto2 = fuente.render(aciertos, 0, (255, 0, 0))
                texto3 = fuente.render(errores, 0, (255, 0, 0))
                texto4 = fuente.render(salir,0,(255,0,0))
                surface.blit(texto1, (110,120))
                surface.blit(texto2, (110,220))
                surface.blit(texto3, (110,340))
                surface.blit(texto4,(110,420))
                break
        #pygame.draw.line(surface, color, start_pos2, end_pos2, width)
        
        pygame.draw.rect(surface, shape_color, ((10, 50), (130, 20)), 3)
        pygame.draw.rect(surface, shape_color, pygame.Rect((10, 50, cantStarPower, 20)), 0)
        pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':
    main()