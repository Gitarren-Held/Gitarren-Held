from note import *
from botonera import *


def main():
    song = load_sound("test")
    Guitarra = pygame.image.load("Img/Gameplay/Guitarra.png")
    Guitarra=pygame.transform.scale(Guitarra,(1280,720))
    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    #botonera
    bot = Botonera(100,100,"Green")
    bot.draw(screen)
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
    song.play()
    while True:
        screen.fill([0,0,0])
        screen.blit(Guitarra,(-315,-180))
        bot.comportamiento(bot.x,bot.y,screen)
        reloj.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0) 
        #for que genera el movimiento en las notas segun cuantas existan en la cancion
        for i in range(0,len(MatrizNotas)):
            movimientolista(MatrizLNotas[i],screen)
        pygame.display.flip()
        pygame.display.update()
    return 0 
if __name__ == '__main__':
    pygame.init()
    main()