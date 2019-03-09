import pygame
from settings import Settings
import sys

# Makes pretty pretty colors

blue    = (0,0,255)
red     = (255,0,0)
green   = (0,255,0)
cyan    = (0,255,255)
magenta = (255,0,255)
yellow  = (255,255,0)



# Ball varianles

animtiontimer = time.Clock()

x  = 450
y  = 300
dx = 1    # x velocity
dy = 2    # y velocity
 

#def castlewall():

def run_game():

  # Start game and create game screen
    pygame.init()
    bb_settings = Settings()
    screen = pygame.display.set_mode((bb_settings.screen_width, bb_settings.screen_height))
    pygame.display.set_caption("Ball Brick Break 2")

    
    
   # Start the main loop of the game

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # Re draw the screen during each pass through loop

        screen.fill(bb_settings.bg_color)
        
        

        # Makes rectangles in the corner
        
        topleft    = pygame.draw.rect(screen,cyan,(0,0,250,150),0)
        
        bottomleft  = pygame.draw.rect(screen,magenta,(650,0,250,150),0)

        topright    = pygame.draw.rect(screen,yellow,(0,450,250,150),0)

        bottomright = pygame.draw.rect(screen,green,(650,450,250,150),0)
    


        # moves the ball

        x += dx
        y += dy

        


        # Updates screen
        
        pygame.display.update()

run_game()



# I wish I knew how to get this thing to work...
