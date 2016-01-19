import pygame, sys
from pygame.locals import *

pygame.init()

# the above lines are pretty much always necessary in every
# python game. otherwise errors occur

DISPLAYSURF = pygame.display.set_mode ((400, 300))

# pygame.display.set_mode() MUST have (x,y) inside of it
# this tells the program how big to draw the game window
# however, if you input only integers, like ...set_mode(x,y)
# you will get an error. It MUST be written as ...set_mode((x,y))

pygame.display.set_caption ('Hello World!')

# the caption is displayed in the title bar of the game window

while True: # main game loop

# this is simply a "while" statement that has no conditions other
# than "true". Therefore, this function will always be "true" and
# will always occur, unless it is specifically told to stop.

	for event in pygame.event.get ():

			# this "for" line checks and rechecks to see if any new
			# events have been made. these events (pygame.event.event)
			# are made by user input, and other things. This tells the
			# game that something new is happening and it should respond
			# to it with the appropriate response and update the screen

		if event.type == QUIT:
				pygame.quit()
				sys.exit()
	pygame.display.update