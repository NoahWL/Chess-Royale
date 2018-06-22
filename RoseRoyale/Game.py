# TODO: ADD DROP

import pygame
import time

import os
from win32api import GetSystemMetrics

from RoseRoyale.Player import Player
from RoseRoyale.MPPlayer import MPPlayer
from RoseRoyale.Gun import Pistol
from RoseRoyale.Bullet import PistolBullet, RPGPellets, RPGBullet, ShotgunBullet
from RoseRoyale.Terrain import Terrain
from pygame.constants import K_a, K_d, K_SPACE, K_t, K_ESCAPE
from pygame.constants import K_a, K_d, K_SPACE, K_t, K_e

players = []
window = None
mainWin = None

# Variables for resolution scaling.  Game is designed around 1920x1080 but objects and their positions will scale to available space.
resolutionX = GetSystemMetrics(0)
resolutionY = GetSystemMetrics(1)
windowScaleX = 1
windowScaleY = 1

bullets = [] # List of bullets that need to be drawn, updated, collided with


def initialize():
    shouldRun = True
    
    # Pygame related setup
    pygame.init()
    
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    global mainWin
    global window
    mainWin = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
    window = mainWin.copy()
    mainWin = pygame.display.set_mode((resolutionX, resolutionY), pygame.NOFRAME)
    
    pygame.display.set_caption('Rose Royale')
    pygame.key.set_repeat(1, 0)
    clock = pygame.time.Clock()
    
    tempBack = pygame.image.load("chessBackground.png").convert()
    
    terrain = Terrain(window)
    
    terrainList = terrain.terrain
    
    # Level set up
    player = Player(600, 50, 'shotgun', window, terrainList)

    posx = 0
    posy = 0
    
    lastShot = 0
    clickCount = 0
    
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
        
        click = pygame.mouse.get_pressed()
            
        if click[0] == 1:
            clickCount += 1
            
            if time.time() - lastShot > 0.5 and player.weaponName == 'pistol':  # How often the player can shoot in seconds
                    bullets.append(player.getWeapon().shoot())
                    lastShot = time.time()
            elif time.time() - lastShot > 0.75 and player.weaponName == 'shotgun':
                for i in range(3):
                    bullets.append(player.getWeapon().shoot(i))
                lastShot = time.time()

            elif time.time() - lastShot > 0.15 and player.weaponName == 'smg':
                bullets.append(player.getWeapon().shoot())
                lastShot = time.time()
                
            elif time.time() - lastShot > 0 and player.weaponName == 'rpg':
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
        terrain.drawAfter()        
        
        mainWin.blit(pygame.transform.scale(window, (resolutionX, resolutionY)), (0, 0))
        pygame.display.update()
        clock.tick(60)
        
    # Runs on window close
    pygame.display.quit()
    pygame.quit()


"""Server commands.  These can be called be the ClientConnection instance to update objects on the player's screen."""


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

        
def spawnBullet(bulletX, bulletY, bulletType, bulletDirection):
    bullet = None
    
    if bulletType == 'PistolBullet':
        pass
    
