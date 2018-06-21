import pygame
import RoseRoyale.Game
from RoseRoyale.Bullet import PistolBullet, RPGBullet
from RoseRoyale.Bullet import ShotgunBullet
#TODO add rgp with shrapnel

class Pistol:
    
    def __init__(self, posX, posY, window, terrain):
        self.name = 'pistol'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.pistol = pygame.image.load("pistol.png")
        self.terrain = terrain
        window.blit(self.pistol, (self.posX, self.posY))
        
    def draw(self, x, y):
        self.posX = x
        self.posY = y
        self.win.blit(self.pistol, (x - 36, y + 18))
    
    def shoot(self):
        return PistolBullet(self.win, self.terrain, self.posX, self.posY)

class Shotgun:

    def __init__(self, posX, posY, window, terrain, onGround):
        self.name = 'shotgun'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.shotgunImage = pygame.image.load("shotgun.png")
        self.hitbox = pygame.Rect(posX - 25, posY + 18, 60, 24) # Used for pickup.  Does not need to be changed once picked up.
        self.terrain = terrain
        self.onGround = onGround
        window.blit(self.shotgunImage, (self.posX, self.posY))
    
    def draw(self, x, y):
        self.posX = x
        self.posY = y
        self.win.blit(self.shotgunImage, (x - 25, y + 18))
    
    def shoot(self, pyMove):
        return ShotgunBullet(self.win, self.terrain, self.posX, self.posY, pyMove)

class RPG:
    
    def __init__(self, posX, posY, window, terrain):
        self.name = 'rpg'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.rpg = pygame.image.load("rpg.png")
        self.terrain = terrain
        window.blit(self.rpg, (self.posX, self.posY))
        
    def draw(self, x, y):
        self.posX = x
        self.posY = y
        self.win.blit(self.rpg, (x - 36, y + 18))
    
    def shoot(self):    
        
        return RPGBullet(self.win, self.terrain, self.posX, self.posY)
    
        