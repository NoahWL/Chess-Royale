import pygame
from RoseRoyale.Bullet import Bullet

class Gun:
    
    def __init__(self, posx, posy, win, terrain):
        self.posx = posx
        self.posy = posy
        self.bullet = Bullet(win, terrain)
        self.win = win
        self.pistol = pygame.image.load("pistol.png")
        win.blit(self.pistol, (self.posx, self.posy))
        
    def drawGun(self, x, y):
        self.posx = x
        self.posy = y
        self.win.blit(self.pistol, (x, y))
    
    def shoot(self):
        
        self.bullet.drawBullet(self.posx, self.posy)
        