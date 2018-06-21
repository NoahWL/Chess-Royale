import pygame
import RoseRoyale.Game
from RoseRoyale.Bullet import PistolBullet, RPGBullet, SMGBullet, ShotgunBullet



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

class SMG:
    
    def __init__(self, posX, posY, window, terrain):
        self.name = 'smg'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.smg = pygame.image.load("smg.png")
        self.terrain = terrain
        window.blit(self.smg, (self.posX, self.posY))
        
    def draw(self, x, y):
        self.posX = x
        self.posY = y
        self.win.blit(self.smg, (x + 15, y + 25))
    
    def shoot(self):
        return SMGBullet(self.win, self.terrain, self.posX, self.posY)

class Shotgun:

    def __init__(self, posX, posY, window, terrain, onGround):
        self.name = 'shotgun'
        self.posX = posX
        self.posY = posY
        self.win = window
        self.shotgunImage = pygame.image.load("shotgun.png")
        self.hitbox = pygame.Rect(posX - 25, posY + 18, 60, 24)  # Used for pickup.  Does not need to be changed once picked up.
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
        self.rpg = pygame.image.load("rpg.png")
        
        self.win = window
        self.terrain = terrain
        
    def draw(self, x, y):
        self.posX = x
        self.posY = y + 26
        self.win.blit(self.rpg, (self.posX, self.posY))
    
    def shoot(self):
        return RPGBullet(self.win, self.terrain, self.posX + 30, self.posY)
    
        
