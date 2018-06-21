# TODO: ADD DROP

import pygame
import time

import os
from win32api import GetSystemMetrics

from RoseRoyale.Player import Player
from RoseRoyale.MPPlayer import MPPlayer
from RoseRoyale.Gun import Pistol
from RoseRoyale.Bullet import PistolBullet
from RoseRoyale.Bullet import ShotgunBullet
from RoseRoyale.Terrain import Terrain
from pygame.constants import K_a, K_d, K_SPACE, K_t, K_ESCAPE
from pygame.constants import K_a, K_d, K_SPACE, K_t, K_e

players = []
window = None

# Variables for resolution scaling.  Game is designed around 1920x1080 but objects and their positions will scale to available space.
resolutionX = 1920
resolutionY = 1080
windowScaleX = 0
windowScaleY = 0

bullets = [] 

def initialize():
    shouldRun = True
    
    # Pygame related setup
    pygame.init()
    
    _setupDisplay()
    
    pygame.display.set_caption('Rose Royale')
    pygame.key.set_repeat(1, 0)
    clock = pygame.time.Clock()
    
    tempBack = pygame.image.load("chessBackground.png").convert()
    tempBack = pygame.transform.scale(tempBack, (int(1920 * windowScaleX), int(1080 * windowScaleY)))
    
    terrain = Terrain(window)
    
    terrainList = terrain.terrain
    
    # Level set up
    
    player = Player(600, 50, 'rpg', window, terrainList)

    posx = 0
    posy = 0
    
    lastShot = 0
    
    
    # main loop
    while shouldRun:
        # Manage local player physics and controls
        if posx > 0:
            posx = posx - 1
        elif posx < 0:
            posx = posx + 1
        
        if posy < 28:
            posy = posy + 2
        elif posy > 4:
            posy = posy - 4
        elif posy < 4:
            posy = posy + 16
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                shouldRun = False
                
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                pygame.display.quit()
                pygame.quit()
                shouldRun = False
            
            if keys[K_a]:
                posx = -6
                
            if keys[K_d]:
                posx = 6
                
            if keys[K_SPACE] and player.onGround:
                posy = -29
            
            if keys[K_e]:
                if time.time() - lastShot > 0.75:
                    player.pickup(terrain)
                    lastShot = time.time()
            
            if keys[K_t]:
                if time.time() - lastShot > 0.75:  # How often the player can shoot in seconds
                    
                    if player.weaponName == 'shotgun':
                        for i in range(3):
                            bullets.append(player.getWeapon().shoot(i))
                        lastShot = time.time()
                    
                    else: # player.weaponName == 'pistol':
                        bullets.append(player.getWeapon().shoot())
                        lastShot = time.time()
        
        if not shouldRun:
            break
        
        # Draw the player if it has moved
        if (posx != 0 or posy != 0):
            window.blit(tempBack, (0, 0))
            terrain.draw()
            player.move(posx, posy, terrainList)
            
        # Draw remote players
        for mpplayer in players:
            mpplayer.draw()
        
        # Draw bullets
        for bullet in bullets:
            if not bullet.drawBullet():
                bullets.remove(bullet)
            
        pygame.display.update()
        clock.tick(60)
        
    # Runs on window close
    pygame.display.quit()
    pygame.quit()


def updateMPPlayer(name, x, y):
    player = None
    for p in players:
        if p.name == name:
            player = p
    if player == None:
        global window
        player = MPPlayer(name, x, y, window)
        players.append(player)
    else:
        player.posx = x
        player.posy = y


def _setupDisplay():
    global window
    global resolutionX
    global resolutionY
    global windowScaleX
    global windowScaleY
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)
    resolutionX = screenWidth
    resolutionY = screenHeight
    
    windowScaleX = screenWidth / 1920
    windowScaleY = screenHeight / 1080
    
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    window = pygame.display.set_mode((screenWidth, screenHeight), pygame.NOFRAME)
    
