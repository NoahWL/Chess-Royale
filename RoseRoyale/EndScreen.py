import pygame

class Win:
    
    def  __init__(self):
        self.winScreen = pygame.image.load('winScreen.jpg').convert_alpha()
        self.buttonMain = pygame.image.load('buttonMain.png').convert_alpha()
        self.buttonQuit = pygame.image.load('buttonQuit.png').convert_alpha()
        
        
    def draw(self, win):
        self.checkClick = True
        self.win = win
        win.blit(self.winScreen, (675, 350))
        win.blit(self.buttonMain, (500, 800))
        win.blit(self.buttonQuit, (1150, 800)) 
        self.quitBox = pygame.Rect(1150, 800, 300, 100)
        
    def checkClick(self, win):
        pass
            
                        
        
class Lose:
    
    def __init__(self):
        self.deathScreen = pygame.image.load('deathScreen.jpeg').convert_alpha()
        self.buttonMain = pygame.image.load('buttonMain.png').convert_alpha()
        self.buttonQuit = pygame.image.load('buttonQuit.png').convert_alpha()
        
    def draw(self, win):
        win.blit(self.deathScreen, (675, 350))
        win.blit(self.buttonMain, (500, 800))
        win.blit(self.buttonQuit, (1150, 800))
    
        
        