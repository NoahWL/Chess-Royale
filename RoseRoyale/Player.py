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
        
        
    def checkTerrain(self, terrain):
        for t in terrain:
            if self.hitbox.colliderect(t):
                print('COLLIDE')
                return True
        return False
    
    def move(self, dx, dy, terrain):
        # Process movement and collisions in x-axis
        if dx > 0:
            while dx > 0:
                self.hitbox.x = self.hitbox.x + 1
                dx = dx - 1
                if self.checkTerrain(terrain):
                    self.hitbox.x = self.hitbox.x - 1
                    break
        elif dx < 0:
            while dx < 0:
                self.hitbox.x = self.hitbox.x - 1
                dx = dx + 1
                if self.checkTerrain(terrain):
                    self.hitbox.x = self.hitbox.x + 1
                    break
                
        # Process movement and collisions in y-axis
        if dy > 0:
            while dy > 0:
                self.hitbox.y = self.hitbox.y + 1
                dy = dy - 1
                if self.checkTerrain(terrain):
                    self.hitbox.y = self.hitbox.y - 1
                    break
        elif dy < 0:
            while dy < 0:
                self.hitbox.y = self.hitbox.y - 1
                dy = dy + 1
                if self.checkTerrain(terrain):
                    self.hitbox.y = self.hitbox.y + 1
                    break
                
        self.posx = self.hitbox.x
        self.posy = self.hitbox.y
        self.win.blit(self.pPlayer, (self.posx, self.posy))
        pygame.draw.rect(self.win, (255, 0, 0), self.hitbox)
    
    def setWeapon(self, weapon):
        if (weapon == "gun"):
            self.weapon = Gun()
            
    def getWeapon(self):
        return self.weapon
