import pygame
from RoseRoyale.Bullet import PistolBullet
from RoseRoyale.Bullet import ShotgunBullet


class Pistol:
    
    def __init__(self, posX, posY, window, terrain):
        self.posX = posX
        self.posY = posY
        self.win = window
        self.pistol = pygame.image.load("pistol.png")
        self.terrain = terrain
        window.blit(self.pistol, (self.posX, self.posY))
        
    def draw(self, x, y):
        self.posX = x
        self.posY = y
        self.win.blit(self.pistol, (x - 36, y + 18))
    
    def shoot(self):
        return PistolBullet(self.win, self.terrain, self.posX, self.posY)

class Shotgun:

    def __init__(self, posX, posY, window, terrain):
        self.posX = posX
        self.posY = posY
        self.win = window
        self.shotgun = pygame.image.load("shotgun.png")
        self.terrain = terrain
        window.blit(self.shotgun, (self.posX, self.posY))
    
    def draw(self, x, y):
        self.posX = x
        self.posY = y
        self.win.blit(self.shotgun, (x - 25, y + 18))
    
    def shoot(self, pyMove):
        return ShotgunBullet(self.win, self.terrain, self.posX, self.posY, pyMove)
        