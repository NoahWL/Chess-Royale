import pygame
import os
import sys


def resource_path(relative_path):  # Get correct path for images when packaged into an executable file.
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # @UndefinedVariable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class WinScreen:
    
    def  __init__(self, window):
        self.win = window
        self.restartBox = pygame.Rect(500, 800, 300, 100)
        self.quitBox = pygame.Rect(1150, 800, 300, 100)
        self.winScreen = pygame.image.load(resource_path('assets/winScreen.jpg')).convert_alpha()
        self.buttonMain = pygame.image.load(resource_path('assets/buttonMain.png')).convert_alpha()
        self.buttonQuit = pygame.image.load(resource_path('assets/buttonQuit.png')).convert_alpha()
        
    def draw(self):
        self.win.blit(self.winScreen, (675, 350))
        self.win.blit(self.buttonMain, (500, 800))
        self.win.blit(self.buttonQuit, (1150, 800)) 
        
    def checkClick(self, win):
        pass


class LoseScreen:
    
    def __init__(self, window):
        self.win = window
        self.restartBox = pygame.Rect(500, 800, 300, 100)
        self.quitBox = pygame.Rect(1150, 800, 300, 100)
        self.deathScreen = pygame.image.load(resource_path('assets/deathScreen.jpeg')).convert_alpha()
        self.buttonMain = pygame.image.load(resource_path('assets/buttonMain.png')).convert_alpha()
        self.buttonQuit = pygame.image.load(resource_path('assets/buttonQuit.png')).convert_alpha()
        
    def draw(self):
        self.win.blit(self.deathScreen, (675, 350))
        self.win.blit(self.buttonMain, (500, 800))
        self.win.blit(self.buttonQuit, (1150, 800))
        
