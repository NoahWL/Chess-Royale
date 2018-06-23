import pygame
import RoseRoyale.Game
import RoseRoyale.ClientConnection
from RoseRoyale.Bullet import PistolBullet, RPGBullet, SMGBullet, ShotgunBullet


class Pistol:
    
    def __init__(self, posX, posY, window, terrain):
        self.name = 'pistol'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.pistolImageR = pygame.image.load("pistol.png").convert_alpha()
        self.pistolImageL = pygame.transform.flip(self.pistolImageR, True, False)
        self.terrain = terrain
        
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y
        self.direction = direction
        if direction:
            self.win.blit(self.pistolImageR, (x + 15, y + 25))
        else:
            self.win.blit(self.pistolImageL, (x - 30, y + 25))
    
    def shoot(self):
        if RoseRoyale.ClientConnection.theClientConnection != None:
            RoseRoyale.ClientConnection.theClientConnection.sendBullet(self.posX, self.posY, 'PistolBullet', self.direction)
        return PistolBullet(self.win, self.terrain, self.posX, self.posY, self.direction)


class SMG:
    
    def __init__(self, posX, posY, window, terrain, onGround):
        self.name = 'smg'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.smgImageR = pygame.image.load("smg.png").convert_alpha()
        self.smgImageL = pygame.transform.flip(self.smgImageR, True, False)
        self.terrain = terrain
        self.onGround = onGround
        self.hitbox = pygame.Rect(posX + 15, posY + 25, 60, 24)
        
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y
        self.direction = direction
        if direction:
            self.win.blit(self.smgImageR, (x + 15, y + 25))
        else:
            self.win.blit(self.smgImageL, (x - 30, y + 25))
    
    def shoot(self):
        return SMGBullet(self.win, self.terrain, self.posX, self.posY, self.direction)


class Shotgun:

    def __init__(self, posX, posY, window, terrain, onGround):
        self.name = 'shotgun'
        self.posX = posX
        self.direction = True
        self.posY = posY
        self.win = window
        self.shotgunImageR = pygame.image.load("shotgun.png").convert_alpha()
        self.shotgunImageL = pygame.transform.flip(self.shotgunImageR, True, False)
        self.hitbox = pygame.Rect(posX - 15, posY + 28, 60, 24)  # Used for pickup.  Does not need to be changed once picked up.
        self.terrain = terrain
        self.onGround = onGround
    
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y
        self.direction = direction
        if direction:
            self.win.blit(self.shotgunImageR, (x + 25, y + 28))
        else:
            self.win.blit(self.shotgunImageL, (x - 40, y + 28))
    
    def shoot(self, pyMove):
        if self.direction:
            magicNum = 65
        else:
            magicNum = -50
        return ShotgunBullet(self.win, self.terrain, self.posX + magicNum, self.posY + 15, pyMove, self.direction)


class RPG:
    
    def __init__(self, posX, posY, window, terrain, onGround):
        self.name = 'rpg'
        self.posX = posX
        self.posY = posY
        self.onGround = onGround
        self.rpgImageR = pygame.image.load("rpg.png").convert_alpha()
        self.rpgImageL = pygame.transform.flip(self.rpgImageR, True, False)
        self.win = window
        self.terrain = terrain
        self.hitbox = pygame.Rect(posX, posY + 26, 60, 24)
        
    def draw(self, x, y, direction):
        self.posX = x
        self.posY = y 
        self.direction = direction
        if direction:
            self.win.blit(self.rpgImageR, (x, y + 26))
        else:
            self.win.blit(self.rpgImageL, (x - 35, y + 26))
    
    def shoot(self):
        if self.direction:
            magicNum = 30
        else:
            magicNum = -30
        return RPGBullet(self.win, self.terrain, self.posX + magicNum, self.posY, self.direction)
        
