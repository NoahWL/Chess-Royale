import pygame


class MPPlayer:

    def __init__(self, name, posX, posY, window):
        self.name = name
        self.posX = posX
        self.posY = posY
        self.win = window
        self.pPlayer = pygame.rect.Rect(posX, posY, 60, 60)
        
    def draw(self):
        self.pPlayer.x = self.posX
        self.pPlayer.y = self.posY
        pygame.draw.rect(self.win, (255, 0, 0), self.pPlayer)
