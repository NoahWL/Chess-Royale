import time
import os
import sys

import pygame
from pygame.constants import K_ESCAPE


def resource_path(relative_path):  # Get correct path for images when packaged into an executable file.
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # @UndefinedVariable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


lastClick = 0


class ServerGUI:

    def __init__(self, server):
        self.shouldRun = True
        self.gameStarted = False
        self.server = server
    
    def setupObjects(self):
        self.startGameRect = pygame.rect.Rect(106, 78, 300, 100)
        self.startImage = pygame.image.load(resource_path('assets/start.png')).convert_alpha()
    
    def stop(self):
        self.shouldRun = False
        
    def startButton(self, window):
        global lastClick
        if pygame.mouse.get_pressed()[0] == 1 and time.time() - lastClick > 0.75:
            mPos = pygame.mouse.get_pos()
            if self.startGameRect.collidepoint(mPos):
                self.server.startGame()
                lastClick = time.time()
    
    def startGUI(self):
        # PyGame setup
        pygame.init()
        clock = pygame.time.Clock()
        
        window = pygame.display.set_mode((512, 256))
        pygame.display.set_caption('RoseRoyale Server')
        
        self.setupObjects()
        window.blit(self.startImage, (106, 78))
        
        # Main draw loop
        while (self.shouldRun):
            
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    self.shouldRun = False
                    pygame.display.quit()
                    pygame.quit()
                    return
                    
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.quit()
                self.shouldRun = False
                return
                
            # Draw buttons
            self.startButton(window)
            
            pygame.display.update()  # Update the display
            clock.tick(15)
