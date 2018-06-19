import pygame

class Bullet:
    
    def __init__(self, win, terrain, posx, posy):
        self.startPosX = posx
        self.posx = posx
        self.posy = posy
        self.speed = 8
        self.win = win
        self.terrain = terrain
        self.bullet = pygame.image.load("bullet.png")
        self.hitbox = pygame.Rect(self.posx + 15, self.posy + 6, 32, 10)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox)
        
    def drawBullet(self):
        
        if abs(self.startPosX - self.posx) < 1000:
            self.posx += self.speed
            
            self.hitbox.x = self.posx
            self.win.blit(self.bullet, (self.posx, self.posy))
            
            for t in self.terrain:
                if self.hitbox.colliderect(t):
                    return False
            
            
            return True
        else:
            return False
            
            
        
            
           
    