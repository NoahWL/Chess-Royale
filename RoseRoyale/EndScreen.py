import pygame


class WinScreen:
    
    def  __init__(self, window):
        self.win = window
        
        self.winScreen = pygame.image.load('winScreen.jpg').convert_alpha()
        self.buttonMain = pygame.image.load('buttonMain.png').convert_alpha()
        self.buttonQuit = pygame.image.load('buttonQuit.png').convert_alpha()
        
    def draw(self):
        self.restartBox = pygame.Rect(500, 800, 300, 100)
        self.quitBox = pygame.Rect(1150, 800, 300, 100)
        self.win.blit(self.winScreen, (675, 350))
        self.win.blit(self.buttonMain, (500, 800))
        self.win.blit(self.buttonQuit, (1150, 800)) 
        
        
    def checkClick(self, win):
        pass


class LoseScreen:
    
    def __init__(self, window):
        self.win = window
        
        self.deathScreen = pygame.image.load('deathScreen.jpeg').convert_alpha()
        self.buttonMain = pygame.image.load('buttonMain.png').convert_alpha()
        self.buttonQuit = pygame.image.load('buttonQuit.png').convert_alpha()
        
    def draw(self):
        self.restartBox = pygame.Rect(500, 800, 300, 100)
        self.quitBox = pygame.Rect(1150, 800, 300, 100)
        self.win.blit(self.deathScreen, (675, 350))
        self.win.blit(self.buttonMain, (500, 800))
        self.win.blit(self.buttonQuit, (1150, 800))
        
