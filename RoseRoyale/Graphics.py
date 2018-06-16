# import the pygame module, so you can use it
import pygame
from RoseRoyale.Player import Player
 
# define a main function
def main():
    
    pygame.init()
    win = pygame.display.set_mode((1024,1024))
    
    pygame.display.set_caption("minimal program")
    pygame.key.set_repeat(1,0)
    clock = pygame.time.Clock()
    tempBack = pygame.image.load("tempBack.png").convert()
    win.blit(tempBack, (0, 0))
    player = Player(126, 770, "gun", win)
    
    running = True
    # create a surface on screen that has the size of 240 x 180
    
    posx = 0
    posy = 0
    # main loop
    while running:
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    posx -= 4
                    
                if event.key == pygame.K_d:
                    posx += 4
                    
                if event.key == pygame.K_s:
                    posy += 4
                    
                if event.key == pygame.K_w:
                    posy -= 4
                    
                if event.key == pygame.K_SPACE:
                    player.getWeapon().shoot()
                    
        
        
        if (posx != 0 or posy != 0):
            win.blit(tempBack, (0, 0))
            player.move(posx, posy)
            #print("jeff")
        
        pygame.display.update()
        clock.tick(60)
                        
    
            
                
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__== "__main__":
    # call the main function
    main()