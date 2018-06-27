import os
import sys

import pygame
import RoseRoyale.Game
import RoseRoyale.ClientConnection
from RoseRoyale.Bullet import PistolBullet, RPGBullet, SMGBullet, ShotgunBullet


def resource_path(relative_path):  # Get correct path for images when packaged into an executable file.
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # @UndefinedVariable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Pistol:
    
    def __init__(self, posX, posY, window, terrain, owner):
        self.name = 'Pistol'
        self.posX = posX
        self.posY = posY
        self.owner = owner
        self.win = window
        self.pistolImageR = pygame.image.load(resource_path('assets/pistol.png')).convert_alpha()
        self.pistolImageL = pygame.transform.flip(self.pistolImageR, True, False)  # flips the gun image to draw it left
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.players = terrain.players
        
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y
        self.direction = direction
        if direction:  # checks to see if it should draw the gun left or right
            self.win.blit(self.pistolImageR, (x + 15, y + 25))  # the numbers added make sure the gun is in the right position
        else:
            self.win.blit(self.pistolImageL, (x - 15, y + 25))
    
    def shoot(self):
        return PistolBullet(self.win, self.terrain, self.posX, self.posY, self.direction, self.owner)


class SMG:
    
    def __init__(self, posX, posY, window, terrain, onGround, owner):
        self.name = 'SMG'
        self.owner = owner
        self.posX = posX
        self.posY = posY
        self.win = window
        self.smgImageR = pygame.image.load(resource_path('assets/smg.png')).convert_alpha()
        self.smgImageL = pygame.transform.flip(self.smgImageR, True, False)
        self.terrain = terrain
        self.onGround = onGround 
        self.hitbox = pygame.Rect(posX + 15, posY + 25, 60, 24)  # Used for pickup.  Does not need to be changed once picked up.
        
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y
        self.direction = direction
        if direction:
            self.win.blit(self.smgImageR, (x + 15, y + 25))  # the numbers added make sure the gun is in the right position
        else:
            self.win.blit(self.smgImageL, (x - 30, y + 25))
    
    def shoot(self):
        return SMGBullet(self.win, self.terrain, self.posX, self.posY, self.direction, self.owner)


class Shotgun:

    def __init__(self, posX, posY, window, terrain, onGround, owner):
        self.name = 'Shotgun'
        self.owner = owner
        self.posX = posX
        self.direction = True
        self.posY = posY
        self.win = window
        self.shotgunImageR = pygame.image.load(resource_path('assets/shotgun.png')).convert_alpha()
        self.shotgunImageL = pygame.transform.flip(self.shotgunImageR, True, False)
        self.hitbox = pygame.Rect(posX - 15, posY + 28, 60, 24)  # Used for pickup.  Does not need to be changed once picked up.
        self.terrain = terrain
        self.onGround = onGround
    
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y
        self.direction = direction
        if direction:
            self.win.blit(self.shotgunImageR, (x + 25, y + 28))  # the numbers added make sure the gun is in the right position
        else:
            self.win.blit(self.shotgunImageL, (x - 40, y + 28))
    
    def shoot(self, pyMove):
        if self.direction:
            magicNum = 65  # these numbers again re-center, but this time it centers the bullets
        else:
            magicNum = -50
        return ShotgunBullet(self.win, self.terrain, self.posX + magicNum, self.posY + 15, pyMove, self.direction, self.owner)


class RPG:
    
    def __init__(self, posX, posY, window, terrain, onGround, owner):
        self.name = 'RPG'
        self.owner = owner
        self.offsetX = 0
        self.offsetY = 26
        
        self.posX = posX
        self.posY = posY
        self.onGround = onGround
        self.hitbox = pygame.Rect(posX, posY + 26, 60, 24)  # Used for pickup.  Does not need to be changed once picked up.
        self.rpgImageR = pygame.image.load(resource_path('assets/rpg.png')).convert_alpha()
        self.rpgImageL = pygame.transform.flip(self.rpgImageR, True, False)
        self.win = window
        self.terrain = terrain
        
    def draw(self, x, y, direction):
        if not self.onGround:
            x += self.offsetX
            y += self.offsetY
        
        self.posX = x
        self.posY = y
        self.direction = direction
        
        if self.direction:
            self.win.blit(self.rpgImageR, (self.posX, self.posY))
        else:
            self.win.blit(self.rpgImageL, (self.posX - 35, self.posY))  # the numbers subtracted make sure the gun is in the right position
    
    def shoot(self):
        if self.direction:
            offsetX = 30
        else:
            offsetX = -30
            
        return RPGBullet(self.win, self.terrain, self.posX + offsetX, self.posY, self.direction, self.owner)
        
