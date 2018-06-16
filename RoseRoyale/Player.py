import pygame
import math
from RoseRoyale.Gun import Gun

class Player:
    
    def __init__(self, posx, posy, weapon, win):
        
        self.posx = posx
        self.posy = posy
        self.weapon = weapon
        self.living = True
        self.win = win
        self.pPlayer = pygame.image.load("tempPlayer.png").convert()
        win.blit(self.pPlayer, (self.posx, self.posy))
        print("created player")
        
        
        
    
    def move(self, posx, posy):
        
        newx = self.posx + posx
        newy = self.posy + posy
        
        self.win.blit(self.pPlayer, (newx, newy))
        
    
    def setWeapon(self, weapon):
        if (weapon == "gun"):
            self.weapon = Gun()
            
    def getWeapon(self):
        return self.weapon
