#
#----------------------------------------------
#
#  THE LEGEND OF CTEC
#
# By: Isobel Lennox
#
# March 2014
#
#----------Splash page, will show on start.-----------------
#


#

# --- Press ESCAPE to exit ---

# initialize
import pygame
pygame.init()
pygame.mouse.set_visible(0)

# colours
lightblue = 112,86,57
white = 255,255,255
black = 0,0,0
red = 255,0,0
grey = 119,119,119

# background screen
def backGroundScreen(colour):
   '''Setup background screen
   In: colourTUPLE.
   Return: screenOBJ'''
   screen = pygame.display.set_mode((1200,600))

   screen.fill(lightblue)
   pygame.display.flip()
   return screen

background = lightblue
screen = backGroundScreen(background)
# CREATE BACKGROUND IMAGE IN PHOTOSHOP
background_image = pygame.image.load("background_01.png").convert()


# Create a font
# When font name = None, Pygame returns a default font
def getFont(name = None, size = 20):
   '''Create a font object'''
   font = pygame.font.Font(name, size)
   return font

# Render the text
def putText(fontOBJ, message = "Test", position = (10,10),
            forecolour = black, backcolour = white):
   '''Create a font object'''
   antialias = True
   text = fontOBJ.render(message, antialias, forecolour, backcolour)
   # Create a rectangle
   textRect = text.get_rect()
   textRect.topleft = position
   # Blit the text
   screen.blit(text, textRect)
   pygame.display.update()






# Create a font and render the header line

headerfont = getFont(None,34)
header = "The Legend Of CTEC"
position = 10,10
putText(headerfont, header, position,
	forecolour = red,
	backcolour = background)

# Now the body text

bodylines = [
	[(140, 180), "A Game based on the adventures of Bruce Elgort"],

	[(110, 540), "Made by Isobel Lennox"],
	[(180, 280), "A ,W and D are to fire bullets "],
	[(180, 310), " Arrow Keys to move"],
    #[(180, 310), " Arrow Keys to move"], # explaing point system
    #[(180, 310), " Arrow Keys to move"], # TO SAVE TO SCOREBOARD
	[(140, 320), "Press <ESC> to continue..."]]
bodyfont = getFont(None, 22)
for line in bodylines:
   position, text = line
   putText(bodyfont, text, position,
           forecolour = white,
	   backcolour = background )

# Now the footer text

footerfont = getFont(None, 18)
footerlines = [
	[(110,500), "This demonstration powered by"],
	[(110,515), "Python and Pygame"]]
for line in footerlines:
    position, text = line
    putText(footerfont, text, position,
	backcolour = background)

# Draw symbol

linesToDraw = [
	[(20, 80), (120, 80)],
	[(67, 60), (67, 160)],
	[(55, 140), (80, 140)],
	[(67, 80), (20, 160)],
	[(67, 80), (120, 160)]
	]

colour = grey
width = 10
for line in linesToDraw:
    start, end = line
    pygame.draw.line(
  	screen, colour, start, end,
	width)


screen.blit(background_image,[0,0])
pygame.display.update()

# Wait for keypress
# Loop until keypress = ESCAPE
done = False
while not done:
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if (event.key == pygame.K_ESCAPE):
            done = True