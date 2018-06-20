import pygame

import RoseRoyale.Game


class Terrain:
    
    def __init__(self, win):
        self.win = win
        self.scaleX = RoseRoyale.Game.windowScaleX
        self.scaleY = RoseRoyale.Game.windowScaleY
        
        self.setup()
        
    def setup(self):
        sX = self.scaleX
        sY = self.scaleY
        
        self.grassPlatform = pygame.image.load("grassPlatform.png").convert_alpha(self.win)
        self.grassPlatform = pygame.transform.scale(self.grassPlatform, (int(463 * sX), int(100 * sY)))
        
        self.floor = pygame.image.load("floorTile.png").convert_alpha(self.win)
        self.floor = pygame.transform.scale(self.floor, (int(21 * sX), int(10 * sY)))
        
        floor = pygame.Rect(0 * sX, 1070 * sY, 1920 * sX, 10 * sY)
        plat1 = pygame.Rect(180 * sX, 880 * sY, 443 * sX, 80 * sY)
        plat2 = pygame.Rect(600 * sX, 660 * sY, 443 * sX, 80 * sY)
        plat3 = pygame.Rect(1000 * sX, 660 * sY, 443 * sX, 80 * sY)
        plat4 = pygame.Rect(1400 * sX, 880 * sY, 443 * sX, 80 * sY)
        
        self.terrain = [floor, plat1, plat2, plat3, plat4]
    
    def draw(self):
        sX = self.scaleX
        sY = self.scaleY
        
        # platforms:
        self.win.blit(self.grassPlatform, (600 * sX, 660 * sY))
        self.win.blit(self.grassPlatform, (1000 * sX, 660 * sY))
        self.win.blit(self.grassPlatform, (1400 * sX, 880 * sY))
        self.win.blit(self.grassPlatform, (170 * sX, 880 * sY))
       
        # floor
        
        for i in range(102):
            self.win.blit(self.floor, (int(21 * sX) * i, RoseRoyale.Game.resolutionY - self.floor.get_height()))