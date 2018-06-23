import pygame
import random

class PistolBullet:
    
    def __init__(self, window, terrain, posX, posY, direction):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.speed = 10
        self.win = window
        self.direction = direction
        self.terrain = terrain
        self.bulletR = pygame.image.load("bullet.png").convert_alpha()
        self.bulletL = pygame.transform.flip(self.bulletR, True, False)
        self.hitbox = pygame.Rect(self.posX + 15, self.posY + 6, 32, 10)
        
    def drawBullet(self):
        
        if abs(self.startPosX - self.posX) < 1800:
            if self.direction:
                self.posX += self.speed
            else:
                self.posX -= self.speed
            
            self.hitbox.x = self.posX
            if self.direction:
                self.win.blit(self.bulletR, (self.posX + 30, self.posY + 20))
            else:
                self.win.blit(self.bulletL, (self.posX - 38, self.posY + 20))
            
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    return False
            
            return True
        else:
            return False

class SMGBullet:
     
    def __init__(self, window, terrain, posX, posY, direction):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.speed = 10
        self.win = window
        self.terrain = terrain
        self.bullet = pygame.image.load("smgBullet.png").convert_alpha()
        self.hitbox = pygame.Rect(self.posX + 48, self.posY + 20, 20, 20)
         
    def drawBullet(self):
         
        if abs(self.startPosX - self.posX) < 900:
            if self.direction:
                self.posX += self.speed
            else:
                self.posX -= self.speed
             
            if self.direction:
                self.hitbox.x = self.posX + 60
            else:
                self.hitbox.x = self.posX - 65
            if self.direction:
                self.win.blit(self.bullet, (self.posX + 60, self.posY + 20))
            else:
                self.win.blit(self.bullet, (self.posX - 44, self.posY + 20))
             
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    return False
             
            return True
        else:
            return False


class ShotgunBullet:
    
    def __init__(self, window, terrain, posX, posY, pyState, direction):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.speedX = 10
        self.speedY = 2
        self.pyState = pyState
        self.win = window
        self.terrain = terrain
        self.bullet = pygame.image.load("shotgunBullet.png").convert_alpha()
        self.hitbox = pygame.Rect(self.posX - 10, self.posY + 15, 22, 22)
        
    def drawBullet(self):
        
        
        
        if self.pyState == 0:
            self.posY += self.speedY
        
        if self.pyState == 1:
            self.posY += 0
            
        if self.pyState == 2:
            self.posY -= self.speedY
        
        if abs(self.startPosX - self.posX) < 1800:
            if self.direction:
                self.posX += self.speedX
            else:
                self.posX -= self.speedX
            
            self.hitbox.x = self.posX
            self.hitbox.y = self.posY
            
            self.win.blit(self.bullet, (self.posX, self.posY))
            
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    return False
            
            return True
        else:
            return False
        
class RPGPellets:
    
    def __init__(self, window, terrain, posX, posY):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.speedX = random.randint(-5, 5)
        self.speedY = random.randint(-5, 5)
        if self.speedX == 0:
            self.speedX = 1
        if self.speedY == 0:
            self.speedY = -1
        self.win = window
        self.terrain = terrain
        self.bullet = pygame.image.load("shotgunBullet.png").convert_alpha()
        self.hitbox = pygame.Rect(self.posX - 10, self.posY + 15, 22, 22)
        self.bounce = 0
        
    def drawBullet(self):
        if abs(self.startPosX - self.posX) < 500:
            self.posX += self.speedX
            self.posY += self.speedY
            
            self.hitbox.x = self.posX - 10
            self.hitbox.y = self.posY + 15
            
            self.win.blit(self.bullet, (self.posX, self.posY))
            
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    self.bounce += 1

                    self.speedX = -self.speedX
                    self.speedY = -self.speedY
                    
                    if self.bounce == 3:
                        self.hitbox = None
                        return False
                
            
            return True
        else:
            return False
        
class RPGBullet:
    
    def __init__(self, window, terrain, posX, posY, direction):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.speed = 10
        self.win = window
        self.terrain = terrain
        self.rpgBulletR = pygame.image.load("rpgBullet.png").convert_alpha()
        self.rpgBulletL = pygame.transform.flip(self.rpgBulletR, True, False)
        self.hitbox = pygame.Rect(self.posX, self.posY + 2, 32, 15)
        self.collided = False
        self.pellets = []
    def drawBullet(self):
        
        if self.collided:
            for pellet in self.pellets:
                if not pellet.drawBullet():
                    self.pellets.remove(pellet)
            if len(self.pellets) <= 0:
                return False
            else:
                return True
        else:
            #pygame.draw.rect(self.win, (0,0,0), self.hitbox)
            if abs(self.startPosX - self.posX) < 2000:
                if self.direction:
                    self.posX += self.speed
                else:
                    self.posX -= self.speed
                
                self.hitbox.x = self.posX
                if self.direction:
                    self.win.blit(self.rpgBulletR, (self.posX, self.posY))
                else:
                    self.win.blit(self.rpgBulletL, (self.posX, self.posY))
                if self.direction:
                    magicNum = -10
                else:
                    magicNum = 20
                for t in self.terrain:
                    if self.hitbox.colliderect(t):
                        for i in range(15):
                            pellet = RPGPellets(self.win, self.terrain, self.posX + magicNum, self.posY)
                            self.pellets.append(pellet)
                        self.collided = True
                            
                return True
            else:
                return False
        
