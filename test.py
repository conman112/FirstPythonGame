import pygame, sys
from pygame.locals import *

pygame.init()

# the above lines are pretty much always necessary in every
# python game. otherwise errors occur

DISPLAYSURF = pygame.display.set_mode ((400, 300)) #also known as the display surface

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

	import pygame	
	spamRect = pygame.Rect(10,20, 200, 300)
	spamRect == (10, 20, 200, 300)

	pygame.display.update

#	import whammy
#		import the module known as "whammy"
#	fizzy()
#		this is calling the function "fizzy" -the program will look for the function
#		called "fizzy" and execute it
#	egg = Wombat()
#		this is calling the Constructor Function "Wombat". It's a safe guess that "Wombat"
#		is a ctor because it has a capital first letter. ctor "Wombat" is stored in the "egg" 
#		variable
#	egg.bluhbluh()
#		use method "bluhbluh" to change or affect variable 'egg"'
#	whammy.spam()
#		Not a method call, but a function call. "whammy" was the module imported earlier
#		this line looks through the "whammy" module for the "spam" function

# anotherSurface = DISPLAYSURF.convert_alpha() <-- must be used to draw with transparent colors