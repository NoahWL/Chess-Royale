import pygame

class Terrain:
    
    def __init__(self, win):
        
        self.win = win
        
        floor = pygame.Rect(0, 1080, 1920, 192)
        plat1 = pygame.Rect(170, 880, 320, 64)
        
        self.terrain = [floor, plat1]
    
    def draw(self):
        
        grassPlatform = pygame.image.load("grassPlatform.png").convert_alpha(self.win)
        
        self.win.blit(grassPlatform, (170, 880))
        
        
    