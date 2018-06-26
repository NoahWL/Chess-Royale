from time import sleep

import pygame
from pygame.constants import MOUSEBUTTONDOWN, KEYDOWN, K_1, K_2, K_3, K_4, K_5, \
    K_6, K_7, K_8, K_9, K_0, K_PERIOD, K_BACKSPACE, K_DELETE

from RoseRoyale.Main import Main

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
        self.size = size
        self.renderableText = self.textType.render(self.text, True, (255, 255, 255), (0, 0, 0))
        self.rect = self.renderableText.get_rect()
  
    def draw(self):
        self.display.blit(self.renderableText, self.size)
      

win = pygame.display.set_mode((1024, 1024))
background = pygame.image.load('chessfigures.jpg').convert()
win.blit(background, (0, 0))

basicFont = pygame.font.SysFont("Cooper Black", 45, 0, 0)

titleFormatted = "Chess Royale"
titleDisplayText = basicFont.render(titleFormatted, True, (255, 255, 255), (0, 0, 0))

joinFormatted = "Join a Game"
joinDisplayText = basicFont.render(joinFormatted, True, (255, 255, 255), (0, 0, 0))

serverFormatted = "Host a Server"
serverDisplayText = basicFont.render(serverFormatted, True, (255, 255, 255), (0, 0, 0))

joinBox = pygame.Rect(75, 100, 280, 53)
hostBox = pygame.Rect(660, 100, 310, 53)

ipText = ''
ipBox = basicFont.render(ipText, True, (255, 255, 255), (0, 0, 0))


def updateTextBox(key):
    global ipText
    global ipBox
    
    if len(ipText) > 15:
        return
    
    if key == K_1:
        ipText += '1'
    elif key == K_2:
        ipText += '2'
    elif key == K_3:
        ipText += '3'
    elif key == K_4:
        ipText += '4'
    elif key == K_5:
        ipText += '5'
    elif key == K_6:
        ipText += '6'
    elif key == K_7:
        ipText += '7'
    elif key == K_8:
        ipText += '8'
    elif key == K_9:
        ipText += '9'
    elif key == K_0:
        ipText += '0'
    elif key == K_PERIOD:
        ipText += '.'
    elif key == K_BACKSPACE or key == K_DELETE:
        ipText = ipText[0:len(ipText)-1]
        
    ipBox = basicFont.render(ipText, True, (255, 255, 255), (0, 0, 0))
def waitOnStart():
    running = True
    selected = None
    while running:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == KEYDOWN:
                updateTextBox(event.key)
                
            if event.type == MOUSEBUTTONDOWN:
                click = event.pos
                
                if joinBox.collidepoint(click):
                    running = False
                    selected = False
                
                if hostBox.collidepoint(click):
                    running = False
                    selected = True
        
        win.blit(background, (0, 0))
        win.blit(titleDisplayText, (360, 50))
        win.blit(joinDisplayText, (75, 100))
        win.blit(serverDisplayText, (660, 100))
        win.blit(ipBox, (360, 150))
        pygame.display.update()
        
    return selected

