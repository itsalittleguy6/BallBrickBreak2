import pygame
from settings import Settings
import sys

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

        # Make most recent screen visible
        
        pygame.display.flip()

run_game()
