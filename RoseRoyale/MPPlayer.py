import os
import sys
import pygame

from RoseRoyale.Gun import Pistol, RPG, SMG, Shotgun


def resource_path(relative_path):  # Get correct path for images when packaged into an executable file.
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # @UndefinedVariable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class MPPlayer:

    def __init__(self, name, posX, posY, window, terrain, weaponName):
        self.name = name
        self.direction = True
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.win = window
        self.isLocal = False
        
        self.posX = posX
        self.posY = posY
        self.pTextureR = pygame.image.load(resource_path('assets/chess_piece_right.png')).convert_alpha()
        self.pTextureL = pygame.image.load(resource_path('assets/chess_piece_left.png')).convert_alpha()
        self.hitbox = pygame.Rect(posX, posY, 45, 104)
        
        self.alive = True
        self.health = 100
        self.healthBarGreen = pygame.rect.Rect(self.posX, self.posY, 100, 5)
        self.healthBarRed = pygame.rect.Rect(self.posX, self.posY, 100, 5)
        
        self.setWeapon(weaponName)
        
    def _drawHealth(self):
        self.healthBarRed.x = self.posX - 26
        self.healthBarRed.y = self.posY - 20
        self.healthBarGreen.x = self.posX - 26
        self.healthBarGreen.y = self.posY - 20
        
        self.healthBarGreen.width = self.health
        
        pygame.draw.rect(self.win, (255, 0, 0), self.healthBarRed)
        pygame.draw.rect(self.win, (0, 255, 0), self.healthBarGreen)
        
    def draw(self):
        if self.direction:
            self.win.blit(self.pTextureR, (self.posX , self.posY))
        else:
            self.win.blit(self.pTextureL, (self.posX , self.posY))
        self.weapon.draw(self.posX, self.posY, self.direction)
        self.hitbox.x = self.posX
        self.hitbox.y = self.posY
        
        self._drawHealth()
            
    def setWeapon(self, weapon):
        if (weapon == 'Shotgun'):
            self.weapon = Shotgun(126, 770, self.win, self.terrainList, False, self.name)
        if (weapon == 'Pistol'):
            self.weapon = Pistol(126, 770, self.win, self.terrain, self.name)
        if (weapon == 'RPG'):
            self.weapon = RPG(126, 770, self.win, self.terrainList, False, self.name)
        if (weapon == 'SMG'):
            self.weapon = SMG(126, 770, self.win, self.terrainList, False, self.name)
            
        self.weaponName = weapon
        
    def die(self):
        self.alive = False
        
    def hit(self, damage):
        self.health -= damage
        
        if self.health <= 0:
            self.health = 0
            self.die()
