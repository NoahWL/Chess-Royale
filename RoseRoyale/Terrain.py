import pygame

class Terrain:
    
    def __init__(self, win):
        
        self.win = win
        
        self.grassPlatform = pygame.image.load("grassPlatform.png").convert_alpha(self.win)
        self.grassFloor = pygame.image.load("grassFloor.png").convert_alpha(self.win)
        
        floor = pygame.Rect(0, 1080, 1920, 192)
        plat1 = pygame.Rect(180, 880, 443, 80)
        plat2 = pygame.Rect(600, 660, 443, 80)
        plat3 = pygame.Rect(1000, 660, 443, 80)
        plat4 = pygame.Rect(1400, 880, 443, 80)
        
        self.terrain = [floor, plat1, plat2, plat3, plat4]
    
    def draw(self):
        #platforms:
        self.win.blit(self.grassPlatform, (600, 660))
        self.win.blit(self.grassPlatform, (1000, 660))
        self.win.blit(self.grassPlatform, (1400, 880))
        self.win.blit(self.grassPlatform, (170, 880))
   
       
        #floor
        self.win.blit(self.grassFloor, (0, 1062))
        self.win.blit(self.grassFloor, (231, 1062))
        