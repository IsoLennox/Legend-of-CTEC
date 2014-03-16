#
#----------------------------------------------
#
#  THE LEGEND OF CTEC
#
# By: Isobel Lennox
#
# March 2014
#
#------------Splash screen for when your score hits 0-------------------
#

import sys, pygame
pygame.init()
pygame.mouse.set_visible(0) # you will not be able to see the mouse when it hovers over screen!


lightblue = 112,86,57

def backGroundScreen(colour):
   screen = pygame.display.set_mode((1200,600))

   screen.fill(lightblue)
   pygame.display.flip()
   return screen

background = lightblue
screen = backGroundScreen(background)
background_image = pygame.image.load("loser.png").convert()


screen.blit(background_image,[0,0])
pygame.display.update()

# Wait for keypress
# Loop until keypress = ESCAPE
done = False
while not done:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
            done = True


