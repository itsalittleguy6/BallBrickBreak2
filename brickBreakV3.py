import pygame
from settings import Settings
from ball import Ball
import sys
import time

# Makes pretty pretty colors

blue    = (0,0,255)
red     = (255,0,0)
green   = (0,255,0)
cyan    = (0,255,255)
magenta = (255,0,255)
yellow  = (255,255,0)


#def castlewall():

def run_game():


  # Start game and create game screen
    pygame.init()
    bb_settings = Settings()
    screen = pygame.display.set_mode((bb_settings.screen_width, bb_settings.screen_height))
    pygame.display.set_caption("Ball Brick Break 2")

    lead_x = 300
    lead_y = 300


    lead_x_change = 0
    lead_y_change = 0

  # Make a ball
    #ball = Ball(screen)
    
    
   # Start the main loop of the game and declares arrow key functionality
    from sys import exit
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -5
                    if event.key == pygame.K_RIGHT:
                        lead_x_change = 5
                    if event.key == pygame.K_UP:
                        lead_y_change = -5
                    if event.key == pygame.K_DOWN:
                        lead_y_change = 5
            
        # Re draw the screen during each pass through loop
        lead_x += lead_x_change
        lead_y += lead_y_change
        screen.fill(bb_settings.bg_color)
        #ball.blitme()
        

        
       # Makes rectangles in the corner
        
        topleft     = pygame.draw.rect(screen,cyan,(0,0,250,150),0)
        
        bottomleft  = pygame.draw.rect(screen,magenta,(650,0,250,150),0)

        topright    = pygame.draw.rect(screen,yellow,(0,450,250,150),0)

        bottomright = pygame.draw.rect(screen,green,(650,450,250,150),0)

        # Makes the tiny red rectangle on the screen and configures it speed and size
        
        pygame.draw.rect(screen,red,[lead_x,lead_y,10,10])
        
        pygame.display.update()




run_game()

