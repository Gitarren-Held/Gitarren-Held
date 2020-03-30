from note import load_image
import pygame
#clase score muestra el puntaje total de la partida en pantalla
class Score(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = load_image("Img/Gameplay/puntaje.png", True)
        self.image = pygame.transform.scale(self.image,(100,110))
        self.x = x
        self.y = y
        self.score = 1000
    #score de parametro se suma a lo que ya tenemos
    def draw(self,surface,score,multiplicador,cantidadNotas):
        self.score += score
        fuente = pygame.font.Font(None, 30)
        notas = str(cantidadNotas)
        notseguidas = fuente.render(notas, 0, (0,255,255))
        
        if(multiplicador>1):
            texto = str(score)
            por = 'x'
            mul = str(multiplicador)
            texto1 = fuente.render(texto, 0, (255, 255, 255))
            texto2 = fuente.render(por, 0, (255, 0, 255))
            texto3 = fuente.render(mul, 0, (0, 255, 255))
            surface.blit(self.image,(self.x,self.y))
            surface.blit(texto1, (35, 125))
            surface.blit(texto2, (75, 125))
            surface.blit(texto3, (90, 125))
          

            
        else:
            texto = str(score)
            texto1 = fuente.render(texto, 0, (255, 255, 255))
            surface.blit(self.image,(self.x,self.y))
            surface.blit(texto1, (45, 125))
            

            
        if(cantidadNotas>0):
            notas = 'Notas Perfectas Seguidas'
            texto4 = fuente.render(notas,0,(0, 255, 255))
            surface.blit(texto4,(200,10))
            surface.blit(notseguidas,(300,40))
        else:
            notas = ' '
            texto4 = fuente.render(notas,0,(0, 255, 255))
            surface.blit(texto4,(45,290))
            surface.blit(notseguidas,(45,600))
        #falta agregar metodo que dibuje y sume puntaje