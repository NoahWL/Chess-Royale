import pygame
import math
from RoseRoyale.Gun import Pistol
import RoseRoyale.ClientConnection
import random


class Player:
    
    def __init__(self, posx, posy, weapon, window, terrain):
        self.win = window
        self.pPlayer = pygame.image.load("tempPlayer.png").convert()
        self.hitbox = pygame.Rect(posx, posy, 64, 64)
        window.blit(self.pPlayer, (posx, posy))
        
        self.terrainList = terrain
        self.posx = posx
        self.posy = posy
        self.serverPosX = 0
        self.serverPosY = 0
        
        self.living = True
        self.onGround = False
        self.setWeapon(weapon)
    
    def _checkTerrain(self, terrain):
        for t in terrain:
            if self.hitbox.colliderect(t):
                return True
            
        return False
    
    def move(self, dx, dy, terrain):
        self.onGround = False
        
        # Process movement and collisions in x-axis
        if dx > 0:
            while dx > 0:
                self.hitbox.x = self.hitbox.x + 1
                dx = dx - 1
                if self._checkTerrain(terrain):
                    self.hitbox.x = self.hitbox.x - 1
                    break
        elif dx < 0:
            while dx < 0:
                self.hitbox.x = self.hitbox.x - 1
                dx = dx + 1
                if self._checkTerrain(terrain):
                    self.hitbox.x = self.hitbox.x + 1
                    break
                
        # Process movement and collisions in y-axis
        if dy > 0:
            while dy > 0:
                self.hitbox.y = self.hitbox.y + 1
                dy = dy - 1
                if self._checkTerrain(terrain):
                    self.hitbox.y = self.hitbox.y - 1
                    self.onGround = True
                    break
        elif dy < 0:
            while dy < 0:
                self.hitbox.y = self.hitbox.y - 1
                dy = dy + 1
                if self._checkTerrain(terrain):
                    self.hitbox.y = self.hitbox.y + 1
                    break
                
        self.posx = self.hitbox.x
        self.posy = self.hitbox.y
        self.win.blit(self.pPlayer, (self.posx, self.posy))
        self.weapon.draw(self.posx + 51, self.posy + 12)
        
        totalMovement = self.posx + self.posy
        totalMovementServer = self.serverPosX + self.serverPosY
        if abs(totalMovement - totalMovementServer) > 4 and RoseRoyale.ClientConnection.theClientConnection != None:
            RoseRoyale.ClientConnection.theClientConnection.sendPlayerPos(self.posx, self.posy)  # Send new player position to the server
            self.serverPosX = self.posx
            self.serverPosY = self.posy
        # pygame.draw.rect(self.window, (255, 0, 0), self.hitbox)
        
    def getPosX(self):
        return self.posx
    
    def getPosY(self):
        return self.posy
    
    def setWeapon(self, weapon):
        if (weapon == 'Pistol'):
            self.weapon = Pistol(126, 770, self.win, self.terrainList)
            
    def getWeapon(self):
        return self.weapon
