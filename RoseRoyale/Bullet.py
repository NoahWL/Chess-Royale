import pygame

class Bullet:
    
    def __init__(self, window, terrain, posX, posY):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.speed = 8
        self.win = window
        self.terrain = terrain
        self.bullet = pygame.image.load("bullet.png")
<<<<<<< HEAD
        self.hitbox = pygame.Rect(self.posx + 15, self.posy + 6, 32, 10)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox)
=======
        self.hitbox = pygame.Rect(self.posX, self.posY, 64, 64)
        #pygame.draw.rect(window, (0, 0, 0), self.hitbox)
>>>>>>> Optimizations
        
    def drawBullet(self):
        
        if abs(self.startPosX - self.posX) < 1000:
            self.posX += self.speed
            
            self.hitbox.x = self.posX
            self.win.blit(self.bullet, (self.posX, self.posY))
            
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    return False
            
            
            return True
        else:
            return False
