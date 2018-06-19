import pygame
import time
import sys

from RoseRoyale.Player import Player
from RoseRoyale.MPPlayer import MPPlayer
from RoseRoyale.Gun import Gun
from RoseRoyale.Bullet import Bullet
from pygame.constants import K_a, K_d, K_SPACE, K_t


global players
players = []
            
def init():
    
    pygame.init()
    global win
    win = pygame.display.set_mode((1024, 1024))
    
    pygame.display.set_caption("minimal program")
    pygame.key.set_repeat(1,0)
    clock = pygame.time.Clock()
    tempBack = pygame.image.load("tempBack.png").convert()

    
    floor = pygame.Rect(0, 834, 1024, 192)
    plat1 = pygame.Rect(194, 384, 320, 64)
    plat2 = pygame.Rect(194, 576, 320, 64)
    
    
    terrain = [floor, plat1, plat2]
    
    
    player = Player(126, 770, "gun", win, terrain)
    pistol = Gun(126, 770, win, terrain)
    
    
    running = True

    posx = 0
    posy = 0
    
    lastShot =  0
    bullets = [] 
    
    # main loop
    while running:
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
                running = False
                
            keys = pygame.key.get_pressed()
                
            if keys[K_a]:
                posx = -2
                
            if keys[K_d]:
                posx = 2
                
            if keys[K_SPACE] and player.onGround:
                posy = -32
            
            if keys[K_t]:
                if time.time() - lastShot > 0.75: # How often the player can shoot in seconds
                    bullets.append(pistol.shoot())
                    lastShot = time.time()


                         
        if (posx != 0 or posy != 0):
            win.blit(tempBack, (0, 0))
            player.move(posx, posy, terrain)
            pistol.drawGun(player.posx + 51, player.posy + 10)
            
        for mpplayer in players:
            mpplayer.draw()
            
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
        global win
        player = MPPlayer(name, x, y, win)
        players.append(player)
    else:
        player.posx = x
        player.posy = y