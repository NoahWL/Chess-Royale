import pygame
import os
import sys

from RoseRoyale.Gun import Pistol, RPG, SMG, Shotgun
from RoseRoyale.Terrain import Terrain
from RoseRoyale.EndScreen import WinScreen, LoseScreen
import RoseRoyale.ClientConnection


def resource_path(relative_path):  # Get correct path for images when packaged into an executable file.
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # @UndefinedVariable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Player:
    
    def __init__(self, name, posX, posY, weapon, window, terrain):
        self.win = window
        self.name = name
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.isLocal = True
        
        self.pTextureR = pygame.image.load(resource_path('assets/chess_piece_right.png')).convert_alpha()
        self.pTextureL = pygame.image.load(resource_path('assets/chess_piece_left.png')).convert_alpha()
        self.hitbox = pygame.Rect(posX, posY, 45, 104)
        self.posX = posX
        self.posY = posY
        self.serverPosX = 0
        self.serverPosY = 0
        self.onGround = False
        
        self.alive = True
        self.health = 100
        self.healthBarGreen = pygame.rect.Rect(self.posX, self.posY, 100, 5)
        self.healthBarRed = pygame.rect.Rect(self.posX, self.posY, 100, 5)
        
        self.weaponName = weapon
        self.setWeapon(weapon)
    
    def _checkTerrain(self):
        for t in self.terrainList:
            if self.hitbox.colliderect(t):
                return True
            
        return False
    
    def _drawHealth(self):
        self.healthBarRed.x = self.posX - 26
        self.healthBarRed.y = self.posY - 20
        self.healthBarGreen.x = self.posX - 26
        self.healthBarGreen.y = self.posY - 20
        
        self.healthBarGreen.width = self.health
        pygame.draw.rect(self.win, (255, 0, 0), self.healthBarRed)
        pygame.draw.rect(self.win, (0, 255, 0), self.healthBarGreen)
    
    def move(self, dx, dy, direction):
        if not self.alive:
            return
        
        self.onGround = False
        
        # Process movement and collisions in x-axis
        if dx > 0:
            while dx > 0:
                self.hitbox.x = self.hitbox.x + 1
                dx = dx - 1
                if self._checkTerrain():
                    self.hitbox.x = self.hitbox.x - 1
                    break
        elif dx < 0:
            while dx < 0:
                self.hitbox.x = self.hitbox.x - 1
                dx = dx + 1
                if self._checkTerrain():
                    self.hitbox.x = self.hitbox.x + 1
                    break
                
        # Process movement and collisions in y-axis
        if dy > 0:
            while dy > 0:
                self.hitbox.y = self.hitbox.y + 1
                dy = dy - 1
                if self._checkTerrain():
                    self.hitbox.y = self.hitbox.y - 1
                    self.onGround = True
                    break
        elif dy < 0:
            while dy < 0:
                self.hitbox.y = self.hitbox.y - 1
                dy = dy + 1
                if self._checkTerrain():
                    self.hitbox.y = self.hitbox.y + 1
                    break
        
        # Update player's position variables
        self.posX = self.hitbox.x
        self.posY = self.hitbox.y
        
        # Depending on which way the player last moved, draw their sprite facing that direction
        if direction:
            self.win.blit(self.pTextureR, (self.posX, self.posY))
        else:
            self.win.blit(self.pTextureL, (self.posX, self.posY))
            
        # Draw the player's health bar above their head
        self._drawHealth()
        
        # Draw the player's weapon
        self.weapon.draw(self.posX, self.posY, direction)
        
        # Send positional data to the server if the player has moved
        totalMovement = self.posX + self.posY
        totalMovementServer = self.serverPosX + self.serverPosY
        if abs(totalMovement - totalMovementServer) >= 1 and RoseRoyale.ClientConnection.theClientConnection != None:
            RoseRoyale.ClientConnection.theClientConnection.sendPlayerPos(self.posX, self.posY, direction, self.weaponName)  # Send new player position to the server
            self.serverPosX = self.posX
            self.serverPosY = self.posY
    
    def setWeapon(self, weapon):
        if (weapon == 'Shotgun'):
            self.weapon = Shotgun(126, 770, self.win, self.terrain, False, self.name)
        if (weapon == 'Pistol'):
            self.weapon = Pistol(126, 770, self.win, self.terrain, self.name)
        if (weapon == 'RPG'):
            self.weapon = RPG(126, 770, self.win, self.terrain, False, self.name)
        if (weapon == 'SMG'):
            self.weapon = SMG(126, 770, self.win, self.terrain, False, self.name)
            
        self.weaponName = weapon
            
    def getWeapon(self):
        return self.weapon
    
    def pickup(self, terrain):
        for weapon in terrain.weapons:
            if self.hitbox.colliderect(weapon.hitbox):
                self.weapon = weapon
                self.weapon.owner = self.name
                self.weaponName = weapon.name
                weapon.onGround = False
                
    def die(self):
        self.alive = False
        
    def hit(self, damage, sendToServer):
        self.health -= damage
        
        if self.health <= 0:
            print('killing local player')
            self.die()
            
