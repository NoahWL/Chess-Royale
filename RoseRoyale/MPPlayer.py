import pygame

class MPPlayer:
    def __init__(self, name, posx, posy, window):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.win = window
        self.pPlayer = pygame.rect.Rect(posx, posy, 60, 60)
        
    def draw(self):
        self.pPlayer.x = self.posx
        self.pPlayer.y = self.posy
        pygame.draw.rect(self.win, (255, 0, 0), self.pPlayer)