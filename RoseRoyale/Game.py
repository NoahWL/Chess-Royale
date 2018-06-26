# TODO: ADD DROP

import pygame
import time

import os
from win32api import GetSystemMetrics

from RoseRoyale.Player import Player
from RoseRoyale.MPPlayer import MPPlayer
from RoseRoyale.Bullet import PistolBullet, RPGBullet, ShotgunBullet, SMGBullet
from RoseRoyale.Terrain import Terrain
from RoseRoyale.EndScreen import WinScreen, LoseScreen

from pygame.constants import K_a, K_d, K_SPACE, K_t, K_ESCAPE, K_RALT
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


def initialize(username, ClientConnection):
    shouldRun = True
    
    # Pygame related setup
    pygame.display.init()
    
    # os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    global mainWin
    global window
    global terrain
    
    mainWin = pygame.display.set_mode((1920, 1080), pygame.NOFRAME, 16)
    window = mainWin.copy()
    terrain = Terrain(window, players)
    # mainWin = pygame.display.set_mode((resolutionX, resolutionY), pygame.FULLSCREEN | pygame.HWACCEL, 16)
    mainWin = pygame.display.set_mode((resolutionX, resolutionY), 16)
    
    pygame.display.set_caption('Rose Royale')
    pygame.key.set_repeat(1, 0)
    clock = pygame.time.Clock()
    
    tempBack = pygame.image.load("chessBackground.jpg").convert()
    
    # End screen setup
    winscreen = WinScreen(window)
    losescreen = LoseScreen(window)
    
    # Level set up
    player = Player(username, 600, 50, 'Pistol', window, terrain)
    players.append(player)
    
    posx = 0
    posy = 0
    direction = True
    lastShot = 0
    rpgTime = 2 # used for cheating
    
    r = pygame.rect.Rect((50, 50), (5, 5))
    while shouldRun:
        # Check if an end screen should be drawn
        if not player.alive:
            losescreen.draw()
        
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
            if time.time() - lastShot > 0.10:
                player.pickup(terrain)
                lastShot = time.time()
        
        if keys[K_RALT]:
            rpgTime = 0
        
        click = pygame.mouse.get_pressed()
            
        if click[0] == 1:
            weapon = player.weaponName
            spawnedBullet = None
            
            if time.time() - lastShot > 0.5 and weapon == 'Pistol':  # How often the player can shoot in seconds
                    spawnedBullet = player.getWeapon().shoot()
                    lastShot = time.time()
            elif time.time() - lastShot > 0.75 and weapon == 'Shotgun':
                spawnedBullet = player.getWeapon().shoot(1)
                for i in range(3):
                    bullets.append(player.getWeapon().shoot(i))
                lastShot = time.time()

            elif time.time() - lastShot > 0.15 and weapon == 'SMG':
                spawnedBullet = player.getWeapon().shoot()
                lastShot = time.time()
                
            elif time.time() - lastShot > rpgTime and weapon == 'RPG':
                spawnedBullet = player.getWeapon().shoot()
                lastShot = time.time()
            
            if spawnedBullet != None:
                if ClientConnection != None:
                    ClientConnection.sendBullet(spawnedBullet.posX, spawnedBullet.posY, spawnedBullet.name, direction)
                if spawnedBullet.name != 'ShotgunBullet':
                    bullets.append(spawnedBullet)

        # Draw background, terrain (platforms, guns on ground, etc.)
        window.blit(tempBack, (0, 0))
        terrain.draw()
        
        # Draw players
        for p in players:
            if p.isLocal:
                p.move(posx, posy, direction)
            else:
                p.draw()
        
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
    mpplayer = None
    for p in players:
        if p.name == name:
            mpplayer = p
    if mpplayer == None:
        global window
        mpplayer = MPPlayer(name, x, y, window, terrain, weaponName)
        players.append(mpplayer)
    else:
        mpplayer.posX = x
        mpplayer.posY = y
        mpplayer.direction = direction
        if mpplayer.weaponName != weaponName:
            mpplayer.setWeapon(weaponName)

        
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

def getMouseScaled():
    m1 = pygame.mouse.get_pos()[0]
    m2 = pygame.mouse.get_pos()[1]
    m1 = m1 * (1920 / resolutionX)
    m2 = m2 * (1080 / resolutionY)
