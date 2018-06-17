import pygame

class Bullet:
    
    def __init__(self, win, terrain):
        self.posx = 0
        self.posy = 0
        self.win = win
        self.terrain = terrain
        self.bullet = pygame.image.load("bullet.png")
        self.hitbox = pygame.Rect(self.posx, self.posy, 64, 64)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox)
        
    
    def drawBullet(self, posx, posy):
        
        self.posx = posx
        self.posy = posy
        
        
            
        self.win.blit(self.bullet, (posx, posy))
            
           
    