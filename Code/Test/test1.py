import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [0,1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball =pygame.transform.scale((pygame.image.load("Img/Notas/Green.png")), (25,25))
ballrect = ball.get_rect()


while 1:
    ballrect = ballrect.move(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if(ballrect.bottom == height):
        speed = [0,0]
    screen.fill(black)
    screen.blit(ball,ballrect)
    pygame.display.flip()


screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('player.bmp').convert()
>>> background = pygame.image.load('background.bmp').convert()
>>> screen.blit(background, (0, 0))
>>> objects = []
>>> for x in range(10):                    #create 10 objects</i>
...     o = GameObject(player, x*40, x)
...     objects.append(o)
>>> while 1:
...     for event in pygame.event.get():
...         if event.type in (QUIT, KEYDOWN):
...             sys.exit()
...     for o in objects:
...         screen.blit(background, o.pos, o.pos)
...     for o in objects:
...         o.move()
...         screen.blit(o.image, o.pos)
...     pygame.display.update()
...     pygame.time.delay(100)