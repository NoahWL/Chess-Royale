import pygame

import RoseRoyale.Game


class MPPlayer:

    def __init__(self, name, posX, posY, window):
        self.scaleX = RoseRoyale.Game.windowScaleX
        self.scaleY = RoseRoyale.Game.windowScaleY
        
        self.name = name
        self.posX = posX
        self.posY = posY
        self.win = window
        self.pPlayer = pygame.image.load("chess piece.png").convert_alpha()
        # self.hitbox = pygame.Rect(posX, posY, 45, 104)
        
    def draw(self):
        self.win.blit(self.pPlayer, (self.posX * self.scaleX, self.posY * self.scaleY))
