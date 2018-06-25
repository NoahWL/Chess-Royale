import pygame
import random


def checkPlayerCollision(bullet, players):
    hitbox = bullet.hitbox
    owner = bullet.owner
    damage = bullet.damage
    
    for player in players:
        if hitbox.colliderect(player.hitbox) and owner != player.name:
            player.hit(damage)
            return True
    return False


def checkTerrainCollision(bullet, terrainList):
    hitbox = bullet.hitbox
    
    for terrain in terrainList:
        if hitbox.colliderect(terrain):
            return True
    return False


class PistolBullet:
    
    def __init__(self, window, terrain, posX, posY, direction, owner):
        self.name = 'PistolBullet'
        self.owner = owner
        self.win = window
        self.direction = direction
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.startPosX = posX
        
        self.speed = 10
        self.damage = 25
        
        self.posX = posX
        self.posY = posY
        self.bulletR = pygame.image.load("bullet.png").convert_alpha()
        self.bulletL = pygame.transform.flip(self.bulletR, True, False)
        self.hitbox = pygame.Rect(self.posX + 15, self.posY + 6, 32, 10)
        
    def drawBullet(self):
        
        if abs(self.startPosX - self.posX) < 1800:
            if self.direction:
                self.posX += self.speed
                self.win.blit(self.bulletR, (self.posX + 30, self.posY + 20))
            else:
                self.posX -= self.speed
                self.win.blit(self.bulletL, (self.posX - 38, self.posY + 20))
            self.hitbox.x = self.posX
            
            return not (checkTerrainCollision(self, self.terrainList) or checkPlayerCollision(self, self.terrain.players))
        else:
            return False


class SMGBullet:
     
    def __init__(self, window, terrain, posX, posY, direction, owner):
        self.name = 'SMGBullet'
        self.owner = owner
        self.win = window
        self.direction = direction
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.startPosX = posX
        
        self.speed = 10
        self.damage = 15
        
        self.posX = posX
        self.posY = posY
        self.bullet = pygame.image.load("smgBullet.png").convert_alpha()
        self.hitbox = pygame.Rect(self.posX, self.posY, 20, 20)
        
    def drawBullet(self):
         
        if abs(self.startPosX - self.posX) < 900:
            if self.direction:
                self.posX += self.speed
                self.hitbox.x = self.posX + 60
                self.win.blit(self.bullet, (self.posX + 60, self.posY + 20))
            else:
                self.posX -= self.speed
                self.hitbox.x = self.posX - 65
                self.win.blit(self.bullet, (self.posX - 44, self.posY + 20))
             
            return not (checkTerrainCollision(self, self.terrainList) or checkPlayerCollision(self, self.terrain.players))
        else:
            return False


class ShotgunBullet:
    
    def __init__(self, window, terrain, posX, posY, pyState, direction, owner):
        self.name = 'ShotgunBullet'
        self.owner = owner
        self.win = window
        self.direction = direction
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.startPosX = posX
        
        self.speedX = 10
        self.speedY = 2
        self.damage = 50
        self.pyState = pyState
        
        self.posX = posX
        self.posY = posY
        self.bullet = pygame.image.load("shotgunBullet.png").convert_alpha()
        self.hitbox = pygame.Rect(self.posX - 10, self.posY + 15, 22, 22)
        
    def drawBullet(self):
        # Draw bullet's y velocity depending on which one it is in the spread (0, 1, or 2)
        if self.pyState == 0:
            self.posY += self.speedY
        elif self.pyState == 1:
            pass
        elif self.pyState == 2:
            self.posY -= self.speedY
        
        if abs(self.startPosX - self.posX) < 1800:
            if self.direction:
                self.posX += self.speedX
            else:
                self.posX -= self.speedX
            self.hitbox.x = self.posX
            self.hitbox.y = self.posY
            
            self.win.blit(self.bullet, (self.posX, self.posY))
            
            return not (checkTerrainCollision(self, self.terrainList) or checkPlayerCollision(self, self.terrain.players))
        else:
            return False

        
class RPGPellets:
    
    def __init__(self, window, terrain, posX, posY, owner):
        self.name = 'RPGPellet'
        self.owner = owner
        self.win = window
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.startPosX = posX
        
        self.speedX = random.randint(-5, 5)
        self.speedY = random.randint(-5, 5)
        if self.speedX == 0:
            self.speedX = 1
        if self.speedY == 0:
            self.speedY = -1
        self.damage = 5
        self.bounce = 0
        
        self.posX = posX
        self.posY = posY
        self.bullet = pygame.image.load("shotgunBullet.png").convert_alpha()
        self.hitbox = pygame.Rect(self.posX - 10, self.posY + 15, 22, 22)
        
    def drawBullet(self):
        if abs(self.startPosX - self.posX) < 500:
            self.posX += self.speedX
            self.posY += self.speedY
            
            self.hitbox.x = self.posX - 10
            self.hitbox.y = self.posY + 15
            
            self.win.blit(self.bullet, (self.posX, self.posY))
            
            def doHit():
                self.bounce += 1
    
                self.speedX = -self.speedX
                self.speedY = -self.speedY
                
                if self.bounce == 3:
                    self.hitbox = None
                    return False
                return True
                    
            if checkTerrainCollision(self, self.terrainList) or checkPlayerCollision(self, self.terrain.players):
                return doHit()
            return True
        else:
            return False

        
class RPGBullet:
    
    def __init__(self, window, terrain, posX, posY, direction, owner):
        self.name = 'RPGBullet'
        self.owner = owner
        self.direction = direction
        self.win = window
        self.terrain = terrain
        self.terrainList = terrain.terrain
        self.startPosX = posX
        
        self.speed = 10
        self.damage = 100
        self.collided = False
        self.pellets = []
        
        self.posX = posX
        self.posY = posY
        self.rpgBulletR = pygame.image.load("rpgBullet.png").convert_alpha()
        self.rpgBulletL = pygame.transform.flip(self.rpgBulletR, True, False)
        self.hitbox = pygame.Rect(self.posX, self.posY, 32, 15)

    def drawBullet(self):
        if self.collided:
            for pellet in self.pellets:
                if not pellet.drawBullet():
                    self.pellets.remove(pellet)
            if len(self.pellets) <= 0:
                return False
            return True
        else:
            # pygame.draw.rect(self.win, (0,0,0), self.hitbox)
            if abs(self.startPosX - self.posX) < 2000:
                if self.direction:
                    self.posX += self.speed
                    pelletOffset = -10
                    self.win.blit(self.rpgBulletR, (self.posX, self.posY))
                else:
                    self.posX -= self.speed
                    pelletOffset = 20
                    self.win.blit(self.rpgBulletL, (self.posX, self.posY))
                self.hitbox.x = self.posX
                    
                def spawnPellets():
                    for i in range(15):
                        pellet = RPGPellets(self.win, self.terrain, self.posX + pelletOffset, self.posY, self.owner)
                        self.pellets.append(pellet)
                    self.collided = True
                    
                if checkTerrainCollision(self, self.terrainList) or checkPlayerCollision(self, self.terrain.players):
                    spawnPellets()
                            
                return True
            else:
                return False
