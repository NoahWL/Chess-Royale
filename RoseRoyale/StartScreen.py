import pygame
from pygame.constants import MOUSEBUTTONDOWN
from RoseRoyale.Main import Main
from time import sleep

pygame.init()

class Game:
    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.win = pygame.display.set_mode(self.width, self.height)
        self.button = pygame.display.set_mode(self.text, self.display)
        self.button.withinBounds()

class Button:
    def __init__(self, size):
        
        self.text = text
        self.size = size
        self.display = display
        self.textType = pygame.font.SysFont(textType, 45, 0, 0)
        self.renderableText = self.textType.render(self.text, True, (255, 255, 255), (0, 0, 0))
        self.rect = self.renderableText.get_rect()
  
    def draw(self):
        self.display.blit(self.renderableText, self.size)
      

win = pygame.display.set_mode((1024,1024))
tempImage = pygame.image.load('chessfigures.jpg').convert()
win.blit(tempImage,(0, 0))

titleFormatted = "Chess Royale"
titleType = pygame.font.SysFont("Cooper Black", 45, 0, 0)
titleDisplayText = titleType.render(titleFormatted, True, (255, 255, 255), (0, 0, 0))

joinFormatted = "Join a Game"
joinType = pygame.font.SysFont("Cooper Black", 45, 0, 0)
joinDisplayText = joinType.render(joinFormatted, True, (255, 255, 255), (0, 0, 0))

serverFormatted = "Host a Server"
serverType = pygame.font.SysFont("Cooper Black", 45, 0, 0)
serverDisplayText = serverType.render(serverFormatted, True, (255, 255, 255), (0, 0, 0))

joinBox = pygame.Rect(75, 100, 280, 53)
hostBox = pygame.Rect(660, 100, 310, 53)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == MOUSEBUTTONDOWN:
            click = event.pos
            
            if joinBox.collidepoint(click) or hostBox.collidepoint(click):
                running = False
    
    win.blit(titleDisplayText, (360, 50))
    win.blit(joinDisplayText, (75, 100))
    win.blit(serverDisplayText, (660, 100))
    pygame.display.update()
    
sleep(1)    
Main(False)

