
#
#----------------------------------------------
#
#  THE LEGEND OF CTEC
#
# By: Isobel Lennox
#
# March 2014
#
#---------------------Player attributes, gravity, etc---------
#



import pygame
import random
import constants
from main import *

from colliders import *

from platform import *
from platform_scroller import *


class Player(pygame.sprite.Sprite):
    """
Global constants
"""

    # Colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    BLUE     = (   0,   0, 255)
    RED      = ( 255,   0,   0)
    GREEN    = (   0, 255,   0)

    # Screen dimensions
    SCREEN_WIDTH  = 800
    SCREEN_HEIGHT = 600

    """ This class represents the bar at the bottom that the player controls. """
    name=""
    score=0
    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """
        self.name=input("What is your name?")

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Load the image
        self.image = pygame.image.load("player.png").convert()
        WHITE    = ( 255, 255, 255)
        self.image.set_colorkey(WHITE)

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()


        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        ground = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in ground:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        lava = pygame.sprite.spritecollide(self, self.level.lava_list, False)
        for touch in lava:
            #If we are moving right,
            # set our right side to new x
           if self.change_x > 0:
                self.rect.right = -900
           elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = -900


        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        ground = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        lava = pygame.sprite.spritecollide(self, self.level.lava_list, False)
        enemy_hit_list = pygame.sprite.spritecollide(self, block_list, False)
        dew_list = pygame.sprite.spritecollide(self, collect_list, False)

        for block in ground:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

        for touch in lava:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.right = -900



            # Stop our vertical movement
            self.change_y = 0

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 10
        else:
            self.change_y += .85

        # See if we are on the ground.
        if self.rect.y >= 600 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 600 - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move at +/- y friendly speed with frame skip
        # when working with a platform moving down.
        self.rect.y += 8
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 8

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= 600:
            self.change_y = -18

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -8

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 8

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
