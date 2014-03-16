#
#----------------------------------------------
#
#  THE LEGEND OF CTEC
#
# By: Isobel Lennox
#
# March 2014
#
#----------Everything for collision detection--------
#
# platforms, lava, mt dew, etc...
#
#

import pygame
import random
from player import *
from platform import *

class Collect(pygame.sprite.Sprite):
#Though these are called "collect" they are the enemies.
    # Constructor. Pass in the color of the block,
    # and its size
    def __init__(self, color, width, height):  # remove coloor,w,h if graphic
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        #BLUE     = (   0,   0, 255)
        #self.image.fill(BLUE)
        # Load the image
        self.image = pygame.image.load("chris.png").convert()
        WHITE    = ( 255, 255, 255)
        self.image.set_colorkey(WHITE)



        # Fetch the rectangle object that has the dimensions of the
        # image. The position of this object is updated
        # by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    #makes blocks move:

    def reset_position(self):
        self.rect.y = random.randrange(300-20)
        self.rect.x = random.randrange(2700-20)
# move:

    def update(self):
        self.rect.x-=3

        # make the blocks appear to the top when hit bottom:
        if self.rect.x < 10:
            self.reset_position()

class Collect2(pygame.sprite.Sprite):
#Though these are called "collect" they are the enemies.
    # Constructor. Pass in the color of the block,
    # and its size
    def __init__(self, color, width, height):  # remove coloor,w,h if graphic
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        #BLUE     = (   0,   0, 255)
        #self.image.fill(BLUE)
        # Load the image
        self.image = pygame.image.load("chris.png").convert()
        WHITE    = ( 255, 255, 255)
        self.image.set_colorkey(WHITE)



        # Fetch the rectangle object that has the dimensions of the
        # image. The position of this object is updated
        # by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    #makes blocks move:

    def reset_position(self):
        self.rect.y = random.randrange(-300,200)
        self.rect.x = random.randrange(-700,-20)
# move:

    def update(self):
        self.rect.y+=300
        self.rect.x-=3

        # make the blocks appear to the top when hit bottom:
        if self.rect.y < 10:
            self.reset_position()

        if self.rect.x < 10:
            self.reset_position()


class Farther_chris(pygame.sprite.Sprite):
#Though these are called "collect" they are the enemies.
    # Constructor. Pass in the color of the block,
    # and its size
    def __init__(self, color, width, height):  # remove coloor,w,h if graphic
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #self.image = pygame.Surface([width, height])
        #BLUE     = (   0,   0, 255)
        #self.image.fill(BLUE)
        # Load the image
        self.image = pygame.image.load("blue.png").convert()
        WHITE    = ( 255, 255, 255)
        self.image.set_colorkey(WHITE)



        # Fetch the rectangle object that has the dimensions of the
        # image. The position of this object is updated
        # by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    #makes blocks move:

    def reset_position(self):
        self.rect.y = random.randrange(300-20)
        self.rect.x = random.randrange(2700-20)
# move:

    def update(self):
        self.rect.x-=1

        # make the blocks appear to the top when hit bottom:
        if self.rect.x < 10:
            self.reset_position()





class Mt_Dew(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its size
    def __init__(self, color, width, height):  # remove coloor,w,h if graphic
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        ##self.image = pygame.Surface([width, height])
        ##GREEN    = (   0, 255,   0)
        ##self.image.fill(GREEN)
        # Load the image
        self.image = pygame.image.load("mtdew.png").convert()
        WHITE    = ( 255, 255, 255)
        self.image.set_colorkey(WHITE)


        # Fetch the rectangle object that has the dimensions of the
        # image. The position of this object is updated
        # by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


