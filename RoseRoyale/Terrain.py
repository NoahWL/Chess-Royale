import pygame

import RoseRoyale.Game
from RoseRoyale.Gun import Shotgun, RPG, SMG


class Terrain:
    
    def __init__(self, win):
        self.win = win
        self.scaleX = RoseRoyale.Game.windowScaleX
        self.scaleY = RoseRoyale.Game.windowScaleY
        
        self.setup()
        
    def setup(self):
        sX = self.scaleX
        sY = self.scaleY
        
        # Platforms - Textures
        self.grassPlatform = pygame.image.load("grassPlatform.png").convert_alpha(self.win)
        self.grassPlatform = pygame.transform.scale(self.grassPlatform, (int(463 * sX), int(100 * sY))) # Scale image to screen
        
        self.floor = pygame.image.load("floorTile.png").convert_alpha(self.win)
        self.floor = pygame.transform.scale(self.floor, (int(21 * sX), int(10 * sY))) # Scale image to screen
        
        self.upsidedownGrass = pygame.image.load("upsidedownGrass.png").convert_alpha(self.win)
        self.upsidedownGrass = pygame.transform.scale(self.upsidedownGrass, (int(463 * sX), int(100 * sY)))
        
        # Platforms - Hitboxes
        floor = pygame.Rect(0, 1070, 1920, 10)
        plat1 = pygame.Rect(180, 880, 443, 80)
        plat2 = pygame.Rect(600, 660, 443, 80)
        plat3 = pygame.Rect(1000, 660, 443, 80)
        plat4 = pygame.Rect(1400, 880, 443, 80)
        
        self.terrain = [floor, plat1, plat2, plat3, plat4]
        
        # List of weapons on ground
        self.weapons = [Shotgun(300, 1020, self.win, self.terrain, True), 
                        RPG(950, 1020, self.win, self.terrain, True), 
                        SMG(1600, 1020, self.win, self.terrain, True)]
        
    def draw(self):
        # Draw platforms
        self.win.blit(self.grassPlatform, (600, 660))
        self.win.blit(self.grassPlatform, (1000, 660))
        self.win.blit(self.grassPlatform, (1400, 880))
        self.win.blit(self.grassPlatform, (170, 880))
        
        # Weapons
        for weapon in self.weapons:
            if weapon.onGround:
                weapon.draw(weapon.posX, weapon.posY)
                #pygame.draw.rect(self.win, (0, 0, 0), weapon.hitbox)
            else:
                self.weapons.remove(weapon)
                
    def drawAfter(self):
        sX = self.scaleX
        sY = self.scaleY
        
        self.win.blit(self.upsidedownGrass, (750 * sX, 990 * sY))
        
        for i in range(102):
            self.win.blit(self.floor, (int(21 * sX) * i, 1080 - self.floor.get_height()))
    
    
    
   