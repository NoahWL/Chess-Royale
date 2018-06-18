import pygame

class MPPlayer:
    def __init__(self, name, posX, posY, win):
        self.name = name
        self.posX = posX
        self.posY = posY
        self.win = win
        self.pPlayer = pygame.rect.Rect(posX, posY, 60, 60)
        
    def draw(self):
        pygame.draw.rect(self.win, (0, 255, 0), self.pPlayer)