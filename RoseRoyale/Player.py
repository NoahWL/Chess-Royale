import pygame
from RoseRoyale.Gun import Pistol
from RoseRoyale.Gun import Shotgun
import RoseRoyale.ClientConnection


class Player:
    
    def __init__(self, posX, posY, weapon, window, terrain):
        self.win = window
        self.pPlayer = pygame.image.load("chess piece.png").convert_alpha()
        self.hitbox = pygame.Rect(posX, posY, 45, 104)
        window.blit(self.pPlayer, (posX, posY))
        
        self.terrainList = terrain
        self.posX = posX
        self.posY = posY
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
                
        self.posX = self.hitbox.x
        self.posY = self.hitbox.y
        self.win.blit(self.pPlayer, (self.posX, self.posY))
        self.weapon.draw(self.posX + 51, self.posY + 12)
        
        totalMovement = self.posX + self.posY
        totalMovementServer = self.serverPosX + self.serverPosY
        if abs(totalMovement - totalMovementServer) > 4 and RoseRoyale.ClientConnection.theClientConnection != None:
            RoseRoyale.ClientConnection.theClientConnection.sendPlayerPos(self.posX, self.posY)  # Send new player position to the server
            self.serverPosX = self.posX
            self.serverPosY = self.posY
        # pygame.draw.rect(self.window, (255, 0, 0), self.hitbox)
        
    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def setWeapon(self, weapon):
        if (weapon == 'Pistol'):
            self.weapon = Shotgun(126, 770, self.win, self.terrainList)
            
    def getWeapon(self):
        return self.weapon
