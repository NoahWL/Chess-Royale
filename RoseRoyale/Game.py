# TODO: ADD DROP

import pygame
import time

import os
from win32api import GetSystemMetrics

from RoseRoyale.Player import Player
from RoseRoyale.MPPlayer import MPPlayer
from RoseRoyale.Gun import Pistol
from RoseRoyale.Bullet import PistolBullet, RPGPellets, RPGBullet, ShotgunBullet, SMGBullet
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

bullets = []  # List of bullets that need to be drawn, updated, collided with
terrain = None  # Terrain object containing and managing all terrain that must be drawn


def initialize(username):
    shouldRun = True
    
    # Pygame related setup
    pygame.display.init()
    
    #os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    global mainWin
    global window
    global terrain
    
    mainWin = pygame.display.set_mode((1920, 1080), pygame.NOFRAME, 16)
    window = mainWin.copy()
    terrain = Terrain(window, players)
    #mainWin = pygame.display.set_mode((resolutionX, resolutionY), pygame.FULLSCREEN | pygame.HWACCEL, 16)
    mainWin = pygame.display.set_mode((resolutionX, resolutionY), 16)
    
    pygame.display.set_caption('Rose Royale')
    pygame.key.set_repeat(1, 0)
    clock = pygame.time.Clock()
    
    tempBack = pygame.image.load("chessBackground.jpg").convert()
    
    # Level set up
    player = Player(username, 600, 50, 'pistol', window, terrain)
    players.append(player)
    
    posx = 0
    posy = 0
    direction = True
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
                pygame.display.quit()
                pygame.quit()
                return
                
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            shouldRun = False
            return
        
        if keys[K_a]:
            posx = -6
            direction = False
            
        if keys[K_d]:
            posx = 6
            direction = True
            
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
                
            elif time.time() - lastShot > 2 and player.weaponName == 'rpg':
                bullets.append(player.getWeapon().shoot())
                lastShot = time.time()
        
        # Draw the player if it has moved
        if (posx != 0 or posy != 0):
            window.blit(tempBack, (0, 0))
            terrain.draw()
            player.move(posx, posy, terrain, direction)
            
        # Draw remote players
        for mpplayer in players:
            if not mpplayer.isLocal:
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


def updateMPPlayer(name, x, y, direction, weaponName):
    player = None
    for p in players:
        if p.name == name:
            player = p
    if player == None:
        global window
        player = MPPlayer(name, x, y, window, terrain, weaponName)
        players.append(player)
    else:
        player.posX = x
        player.posY = y
        player.direction = direction
        if player.weaponName != weaponName:
            player.setWeapon(weaponName)

        
def spawnBullet(bulletX, bulletY, bulletType, bulletDirection, owner):
    bullet = None
     
    if bulletType == 'PistolBullet':
        bullet = PistolBullet(window, terrain, bulletX, bulletY, bulletDirection, owner)
    elif bulletType == 'SMGBullet':
        bullet = SMGBullet(window, terrain, bulletX, bulletY, bulletDirection, owner)
    elif bulletType == 'RPGBullet':
        bullet = RPGBullet(window, terrain, bulletX, bulletY, bulletDirection, owner)
    elif bulletType == 'ShotgunBullet':
        bullet = ShotgunBullet(window, terrain, bulletX, bulletY, 0, bulletDirection, owner)
        bullets.append(ShotgunBullet(window, terrain, bulletX, bulletY, 1, bulletDirection, owner))
        bullets.append(ShotgunBullet(window, terrain, bulletX, bulletY, 2, bulletDirection, owner))
         
    bullets.append(bullet)
    
