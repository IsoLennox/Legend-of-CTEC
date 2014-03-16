#
#----------------------------------------------
#
#  THE LEGEND OF CTEC
#
# By: Isobel Lennox
#
# March 2014
#
#------------Weapon attributes-----------------
#



import pygame
import random
from player import *
from colliders import *
from platform import *



class Bullet_up(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([3, 10])
        BLACK    = (   0,   0,   0)
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        #shoots up
        self.rect.y -= 15

class Bullet_right(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 3])
        BLACK    = (   0,   0,   0)
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        #shoots right
        self.rect.x += 15

class Bullet_left(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 3])
        BLACK    = (   0,   0,   0)
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        #shoots left
        self.rect.x -= 15
