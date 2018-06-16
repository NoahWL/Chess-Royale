import pygame
import math
from RoseRoyale.Gun import Gun

class Player:
    
    def __init__(self, posx, posy, weapon, win, terrain):
        
        self.posx = posx
        self.posy = posy
        
        self.weapon = weapon
        
        self.living = True

        self.win = win
        self.pPlayer = pygame.image.load("tempPlayer.png").convert()
        self.hitbox = pygame.Rect(posx, posy, 64, 64)
        win.blit(self.pPlayer, (self.posx, self.posy))
        
        print("created player")
        
        
        
    
    def move(self, posx, posy, terrain):       
        
        newx = 0
        breakout = False
        for t in terrain:
            if breakout:
                break
            
            for i in range(posx):
                newx = self.posx + i
                self.hitbox.x = newx
                
                if self.hitbox.colliderect(t):
                    newx -= 1
                    breakout = True
                    print("collide x")
                    break
                
        newy = 0
        breakout = False
        for t in terrain:
            if breakout:
                break
            
            for i in range(posy):
                newy = self.posy + i
                self.hitbox.y = newy
                
                if self.hitbox.colliderect(t):
                    newy -= 1
                    breakout = True
                    print("collide x")
                    break
                
        self.win.blit(self.pPlayer, (newx, newy))
        self.posx = newx
        self.posy = newy
        
    
    def setWeapon(self, weapon):
        if (weapon == "gun"):
            self.weapon = Gun()
            
    def getWeapon(self):
        return self.weapon
