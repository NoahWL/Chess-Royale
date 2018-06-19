import pygame
from RoseRoyale.Bullet import Bullet


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
        self.win.blit(self.pistol, (x, y))
    
    def shoot(self):
        return Bullet(self.win, self.terrain, self.posX, self.posY)
