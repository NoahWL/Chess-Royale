import pygame
import time
<<<<<<< HEAD:RoseRoyale/Graphics.py
import os
=======
>>>>>>> Optimizations:RoseRoyale/Game.py

from RoseRoyale.Player import Player
from RoseRoyale.MPPlayer import MPPlayer
from RoseRoyale.Gun import Pistol
from RoseRoyale.Bullet import Bullet
<<<<<<< HEAD:RoseRoyale/Graphics.py
from RoseRoyale.Terrain import Terrain
from pygame.constants import K_a, K_d, K_SPACE, K_t, K_ESCAPE

global players
=======
from pygame.constants import K_a, K_d, K_SPACE, K_t

>>>>>>> Optimizations:RoseRoyale/Game.py
players = []
window = None

            
def initialize():
    shouldRun = True
    
    # Pygame related setup
    pygame.init()
<<<<<<< HEAD:RoseRoyale/Graphics.py
    global win
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    win = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
=======
    global window
    window = pygame.display.set_mode((1024, 1024))
>>>>>>> Optimizations:RoseRoyale/Game.py
    
    pygame.display.set_caption('Rose Royale')
    pygame.key.set_repeat(1, 0)
    clock = pygame.time.Clock()
<<<<<<< HEAD:RoseRoyale/Graphics.py
    tempBack = pygame.image.load("chessBackground.png").convert()
    
    terrainList = Terrain(win)
    
    terrain = terrainList.terrain
      
    
    player = Player(126, 770, "gun", win, terrain)
    pistol = Gun(126, 770, win, terrain)
    
    
    running = True
=======
    
    # Level set up
    tempBack = pygame.image.load('tempback.png').convert() # Level background image
    
    floor = pygame.Rect(0, 834, 1024, 192) # Terrain objects over background (for collisions)
    plat1 = pygame.Rect(194, 384, 320, 64)
    plat2 = pygame.Rect(194, 576, 320, 64)
    
    terrainList = [floor, plat1, plat2]
    
    player = Player(126, 770, 'Pistol', window, terrainList)
>>>>>>> Optimizations:RoseRoyale/Game.py

    posx = 0
    posy = 0
    
    lastShot = 0
    bullets = [] 
    
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
                pygame.quit()
                running = False
            
            if keys[K_a]:
                posx = -2
                
            if keys[K_d]:
                posx = 2
                
            if keys[K_SPACE] and player.onGround:
                posy = -29
            
            if keys[K_t]:
                if time.time() - lastShot > 0.75:  # How often the player can shoot in seconds
                    bullets.append(player.getWeapon().shoot())
                    lastShot = time.time()
        
        # Draw the player if it has moved
        if (posx != 0 or posy != 0):
<<<<<<< HEAD:RoseRoyale/Graphics.py
            win.blit(tempBack, (0, 0))
            terrainList.draw()
            player.move(posx, posy, terrain)
            pistol.drawGun(player.posx + 51, player.posy + 10)
=======
            window.blit(tempBack, (0, 0))
            player.move(posx, posy, terrainList)
>>>>>>> Optimizations:RoseRoyale/Game.py
            
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
