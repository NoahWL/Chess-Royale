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

from pygame.constants import K_a, K_d, K_SPACE, K_t, K_ESCAPE, K_RALT, \
    MOUSEBUTTONDOWN
from pygame.constants import K_a, K_d, K_SPACE, K_t, K_e


def resource_path(relative_path):  # Get correct path for images when packaged into an executable file.
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS  # @UndefinedVariable
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Various window surfaces
window = None  # This is drawn to and then scaled to the appropriate resolution
mainWin = None  # Window is drawn to this.  It takes up the entire screen.
winscreen = None  # Shown if the local player is the last one standing
losescreen = None  # Shown if the player has been killed

# Variables for resolution scaling.  Game is designed around 1920x1080 but objects and their positions will scale to available space.
resolutionX = GetSystemMetrics(0)
resolutionY = GetSystemMetrics(1)

# List of various objects/entities that must be drawn
bullets = []  # List of bullets
players = []  # List of players (including local)
terrain = None  # Terrain class, contains list of terrain objects and players
player = None  # Local player controlled by this client

# Misc variables
gameStarted = False  # True if the server has started the game
gameEnded = False  # True if the player has won or died.  Used to allow clicking on endscreen buttons.
clientConnection = None  # ClientConnection to server for this client


# Check if an end screen should be drawn
def drawEndScreen(player):
    global gameStarted
    # Lose screen
    if not player.alive:
        losescreen.draw()
        gameEnded = True
    # Win screen
    elif len(players) == 1 and gameStarted:
        winscreen.draw()
        gameEnded = True


def initialize(username, ClientConnection):
    # Variables that should be accessed anywhere in this module
    global mainWin
    global window
    global terrain
    global winscreen
    global losescreen
    global gameStarted
    global gameEnded
    global player
    global clientConnection
    
    shouldRun = True
    clientConnection = ClientConnection
    
    # Pygame related setup
    pygame.display.init()
    
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"  # Set game window to start at the top-left corner of the screen
    mainWin = pygame.display.set_mode((1920, 1080), pygame.NOFRAME, 16)
    window = mainWin.copy()
    terrain = Terrain(window, players)
    mainWin = pygame.display.set_mode((resolutionX, resolutionY), pygame.NOFRAME, 16)
    # mainWin = pygame.display.set_mode((resolutionX, resolutionY), 16)
    
    pygame.display.set_caption('Rose Royale')
    pygame.key.set_repeat(1, 0)
    clock = pygame.time.Clock()
    
    tempBack = pygame.image.load(resource_path('assets/chessBackground.jpg')).convert()
    waitingScreen = pygame.image.load(resource_path('assets/waitingPlayers.png')).convert_alpha()
    
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
    rpgTime = 2  # RPG fire rate
    
    def waitForStart():
        # Wait for the server owner to start the game
        while not gameStarted:
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
        
            backgroundRect = pygame.rect.Rect(0, 0, 1920, 1080)
            pygame.draw.rect(window, (0, 100, 100), backgroundRect)
            window.blit(waitingScreen, (706, 471))  # Draw waiting image in center of screen
            mainWin.blit(pygame.transform.scale(window, (resolutionX, resolutionY)), (0, 0))  # Blit "window" to "mainWin," scaling it to the user's resolution
            pygame.display.update()  # Update the display
            clock.tick(30)
        
    waitForStart()
    
    # Main game loop
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
            
            if event.type == MOUSEBUTTONDOWN and gameEnded:
                click = getMouseScaled()
                
                if winscreen.restartBox.collidepoint(click) or losescreen.restartBox.collidepoint(click):
                    gameStarted = False
                    gameEnded = False
                    waitForStart()
                    player.health = 100
                    player.alive = True
                if winscreen.quitBox.collidepoint(click) or losescreen.quitBox.collidepoint(click):
                    shouldRun = False
                    return
                    
        # Checks for key presses    
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
        # makes the RPG fire time 0 (a cheat)
        if keys[K_RALT]:
            rpgTime = 0
        
        click = pygame.mouse.get_pressed()
            
        if click[0] == 1 and player.alive:
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

        # 1 - Draw background, terrain (platforms, guns on ground, etc.)
        window.blit(tempBack, (0, 0))
        terrain.draw()
        
        # 2 - Draw players
        for p in players:
            if not p.alive:
                players.remove(p)
            
            if p.isLocal:
                p.move(posx, posy, direction)
            else:
                p.draw()
        
        # 3 - Draw bullets
        for bullet in bullets:
            if not bullet.drawBullet():
                bullets.remove(bullet)
                
        # 4 - Draw terrain that should appear on top of the player
        terrain.drawAfter()
        
        # 5 - Draw an end screen if required
        drawEndScreen(player)
        
        mainWin.blit(pygame.transform.scale(window, (resolutionX, resolutionY)), (0, 0))  # Blit "window" to "mainWin," scaling it to the user's resolution
        pygame.display.update()  # Update the display
        clock.tick(60)  # Tick pygame's clock to keep 60FPS (TODO: Replace this garbage)
        
    # Runs on window close
    pygame.display.quit()
    pygame.quit()


"""Server commands.  These can be called be the ClientConnection instance to update objects on the player's screen."""


def startGame():
    global gameStarted
    gameStarted = True


def updateMPPlayer(name, x, y, direction, weaponName):
    global clientConnection
    
    mpplayer = None
    for p in players:
        if p.name == name:
            mpplayer = p
    if mpplayer == None:
        mpplayer = MPPlayer(name, x, y, window, terrain, weaponName, clientConnection)
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

    
def DamagePlayer(amount):
    global player
    player.hit(amount)


def getMouseScaled():
    m1 = pygame.mouse.get_pos()[0]
    m2 = pygame.mouse.get_pos()[1]
    m1 = m1 * (1920 / resolutionX)
    m2 = m2 * (1080 / resolutionY)
    return(m1, m2)
