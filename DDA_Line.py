#Digital differential analyzer (graphics algorithm) For LINE

import pygame
from pygame import gfxdraw
import sys

#input for the end points of the line

x1 = int(input('X1 co-ordinate:'))
y1 = int(input('Y1 co-ordinate:'))

x2 = int(input('X2 co-ordinate:'))
y2 = int(input('Y2 co-ordinate:'))

print('Straight Line between points: ({},{}) and ({},{})'.format(x1,y1,x2,y2))

def DDA_line(x1,y1,x2,y2):

	#delta values for X and Y
	dx = x2 - x1
	dy = y2 - y1

	#steps from the initial point to the final point is determined 
	#by the maximum of dx and dy

	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)

	print('Steps: {}'.format(steps))

	#amount that X and Y should increment after every iteration to draw the draw
	Xinc = dx / steps
	Yinc = dy / steps

	print('X increments by: {} and Y increments by: {}'.format(Xinc,Yinc))

	#Pygame configuration
	pygame.init()

	black = (0, 0, 0)
	white = (255, 255, 255)

	size = [600,480]
	screen = pygame.display.set_mode(size)

	screen.fill(white)

	#initial points of the line

	x = x1
	y = y1

	#loop to draw the line
	for i in range(0,steps+1):
		gfxdraw.pixel(screen, int(x), int(y), black)
		pygame.display.update()
		x = x + Xinc
		y = y + Yinc

	#for closing the pygame window
	while True:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				pygame.quit()
				sys.exit()




DDA_line(x1,y1,x2,y2)

