import pygame
from pygame.locals import *

runGame = True

def initialize():
    pygame.init()
    surface = pygame.display.set_mode((640, 500)) #.convert_alpha() Initialize main surface
    pygame.display.set_caption("Rose Royale") # Set window title

    # Add objects to window
    rectangleOne = pygame.Rect((100, 100, 200, 200))
    pygame.draw.rect(surface, (0, 0, 255), rectangleOne, 10)

    # Game loop
    while runGame:
        for e in pygame.event.get(): # Pass events to event handler
            handleEvent(e)
        pygame.display.update() # Update display
    

# Event handler
def handleEvent(event):
    if event.type == QUIT:
        pygame.quit()
        exit(0)

if __name__ == "__main__":
    initialize()
