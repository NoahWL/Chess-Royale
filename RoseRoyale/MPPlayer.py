import pygame

from RoseRoyale.Gun import Pistol, RPG, SMG, Shotgun


class MPPlayer:

    def __init__(self, name, posX, posY, window, weaponName):
        self.name = name
        self.posX = posX
        self.posY = posY
        self.direction = True
        self.weaponName = weaponName
        
        self.setWeapon(weaponName)
        
        self.win = window
        self.pTextureR = pygame.image.load('chess_piece_right.png').convert_alpha()
        self.pTextureL = pygame.image.load('chess_piece_left.png').convert_alpha()
        # self.hitbox = pygame.Rect(posX, posY, 45, 104)
        
    def draw(self):
        if self.direction:
            self.win.blit(self.pTextureR, (self.posX , self.posY))
        else:
            self.win.blit(self.pTextureL, (self.posX , self.posY))
        self.weapon.draw(self.posX, self.posY, self.direction)
            
    def setWeapon(self, weapon):
        if (weapon == 'shotgun'):
            self.weapon = Shotgun(126, 770, self.win, self.terrainList, False)
        if (weapon == 'pistol'):
            self.weapon = Pistol(126, 770, self.win, self.terrainList)
        if (weapon == 'rpg'):
            self.weapon = RPG(126, 770, self.win, self.terrainList, False)
        if (weapon == 'smg'):
            self.weapon = SMG(126, 770, self.win, self.terrainList, False)
