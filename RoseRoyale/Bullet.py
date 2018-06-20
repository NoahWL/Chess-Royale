import pygame


class Bullet:
    
    def __init__(self, window, terrain, posX, posY):
        self.startPosX = posX
        self.posX = posX
        self.posY = posY
        self.speed = 10
        self.win = window
        self.terrain = terrain
        self.bullet = pygame.image.load("bullet.png")
        self.hitbox = pygame.Rect(self.posX + 15, self.posY + 6, 32, 10)
        pygame.draw.rect(window, (0, 0, 0), self.hitbox)
        # pygame.draw.rect(window, (0, 0, 0), self.hitbox)
        
    def drawBullet(self):
        
        if abs(self.startPosX - self.posX) < 1800:
            self.posX += self.speed
            
            self.hitbox.x = self.posX
            self.win.blit(self.bullet, (self.posX - 10, self.posY + 15))
            
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    return False
            
            return True
        else:
            return False
