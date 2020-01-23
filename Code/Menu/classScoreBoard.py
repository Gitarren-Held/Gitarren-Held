import pygame,sys
import utils
from utils import *
class ScoreBoard():
    enemiesKilled = 0
    playerAmmo = 0
    playerLives = 0
    def drawEnemiesKilled(self):

        text = getFont(size=24, style="bold").render(("Killed: " + str(ScoreBoard.enemiesKilled)), True, black)
        self.image.blit(text, (5, 10))
    def drawPlayerAmmo(self):

        text = getFont(size=24, style="bold").render(("Ammo: " + str(ScoreBoard.playerAmmo)), True, black)
        self.image.blit(text, (5, 35))
    def drawPlayerLives(self):

        text = getFont(size=24, style="bold").render(("Lives: " + str(ScoreBoard.playerLives)), True, black)
        self.image.blit(text, (5, 60))
    def update(self, gw):
        self.image.fill(white)
        self.drawEnemiesKilled()
        self.drawPlayerAmmo()
        self.drawPlayerLives()
        gw.blit(self.image, self.rect)