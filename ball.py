import pygame

"""Need to include colors but we should add this to settings file and reference it"""
blue    = (0,0,255)
red     = (255,0,0)
green   = (0,255,0)
cyan    = (0,255,255)
magenta = (255,0,255)
yellow  = (255,255,0)


x = 450
y = 300
changeX = 1
changeY = 1
radius = 25

class Ball():
    def __init__(self, screen):
        """Initialize the ball and its starting position"""
        self.screen = screen

        #Load the ball image
        self.image = pygame.image.load('Images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start ball in center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centerx

    def blitme(self):
        """Draw the ball"""
        self.screen.blit(self.image, self.rect)
