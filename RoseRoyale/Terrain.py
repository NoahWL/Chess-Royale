import pygame

import RoseRoyale.Game
from RoseRoyale.Gun import Shotgun, RPG, SMG


class Terrain:
    
    def __init__(self, win, players):
        self.win = win
        self.setup()
        self.players = players
        
    def setup(self):
        
        # Platforms - Textures
        self.grassPlatform = pygame.image.load("grassPlatform.png").convert_alpha(self.win)
        self.floor = pygame.image.load("floorTile.png").convert_alpha(self.win)       
        self.upsidedownGrass = pygame.image.load("upsidedownGrass.png").convert_alpha(self.win)
        self.grassPlatformLeftSide = pygame.image.load("grassPlatformLeftSide.png").convert_alpha(self.win)
        self.grassPlatformRightSide = pygame.image.load("grassPlatformRightSide.png").convert_alpha(self.win)
        
        # Platforms - Hitboxes
        floor = pygame.Rect(0, 1070, 1920, 10)
        plat1 = pygame.Rect(180, 880, 443, 80)
        plat2 = pygame.Rect(600, 660, 443, 80)
        plat3 = pygame.Rect(1000, 660, 443, 80)
        plat4 = pygame.Rect(1400, 880, 443, 80)
        plat5 = pygame.Rect(1407, 450, 443, 80)
        plat6 = pygame.Rect(100, 450, 443, 80)
        plat7 = pygame.Rect(-100, 450, 443, 80)
        plat8 = pygame.Rect(1707, 450, 443, 80)
        wall1 = pygame.Rect(920, 250, 125, 443)
        
        self.terrain = [floor, plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, wall1]
        
        # List of weapons on ground
        self.weapons = [Shotgun(300, 1020, self.win, self, True,
                        'terrain'), RPG(950, 1020, self.win, self, True, 'terrain'),
                        SMG(1600, 1020, self.win, self, True, 'terrain')]
        
    def draw(self):
        # Draw platforms
        self.win.blit(self.grassPlatformLeftSide, (920, 250))
        self.win.blit(self.grassPlatformRightSide, (960, 250))
        self.win.blit(self.grassPlatform, (600, 660))
        self.win.blit(self.grassPlatform, (1000, 660))
        self.win.blit(self.grassPlatform, (1400, 880))
        self.win.blit(self.grassPlatform, (170, 880))
        self.win.blit(self.grassPlatform, (-100, 450))
        self.win.blit(self.grassPlatform, (100, 450))
        self.win.blit(self.grassPlatform, (1707, 450))
        self.win.blit(self.grassPlatform, (1407, 450))
        
        # Weapons
        for weapon in self.weapons:
            if weapon.onGround:
                weapon.draw(weapon.posX, weapon.posY, True)
                # pygame.draw.rect(self.win, (0, 0, 0), weapon.hitbox)
            else:
                self.weapons.remove(weapon)
                
    def drawAfter(self):
        self.win.blit(self.upsidedownGrass, (750, 990))
        
        for i in range(102):
            self.win.blit(self.floor, (21 * i, 1080 - self.floor.get_height()))
   
