import pygame
from RoseRoyale.Player import Player
 

def main():
    
    pygame.init()
    win = pygame.display.set_mode((1024,1024))
    
    pygame.display.set_caption("minimal program")
    pygame.key.set_repeat(1,0)
    clock = pygame.time.Clock()
    tempBack = pygame.image.load("tempBack.png").convert()
    win.blit(tempBack, (0, 0))
    
    floor = pygame.Rect(0, 834, 1024, 192)
    plat1 = pygame.Rect(194, 384, 320, 64)
    plat2 = pygame.Rect(194, 576, 320, 64)
    
    
    terrain = [floor, plat1, plat2]
    
    
    
    player = Player(126, 770, "gun", win, terrain)
    
    running = True

    
    
    posx = 0
    posy = 0
    
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
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    posx = -2
                    
                if event.key == pygame.K_d:
                    posx = 2
                    
                if event.key == pygame.K_SPACE and player.onGround:
                    posy = -32
                    
        if (posx != 0 or posy != 0):
            win.blit(tempBack, (0, 0))
            player.move(posx, posy, terrain)
            
        
        pygame.display.update()
        clock.tick(60)
                        
    
            
                

if __name__== "__main__":

    main()