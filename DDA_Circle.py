#Digital differential analyzer (graphics algorithm) For Circle

import pygame
from pygame import gfxdraw
import math
import sys

#input for the center of the circle
print('Provide the co-ordinates for center:')
h = int(input('X co-ordinate:'))
k = int(input('Y co-ordinate:'))
r = int(input('Radius:'))

print('Co-ordinates for center: ({},{}) and Radius: {}'.format(h,k,r))

def DDA_circle(h,k,r):

	
	#Pygame configuration
	pygame.init()

	black = (0, 0, 0)
	white = (255, 255, 255)

	size = [600,480]
	screen = pygame.display.set_mode(size)

	screen.fill(white)

	gfxdraw.pixel(screen, int(100), int(100), black)

	#initialise points:
	x = h 
	y = k 

	#Move from top of the screen to the right for X:
	#Move from top of the screen to the bottom for Y:
	for i in range(x-r-1,x+r+1):
		i += 1
		for j in range(y-r-1,y+r+1):
			j += 1
			result = math.pow((i-h),2) + math.pow((j-k),2)
			Dist = round(math.sqrt(result))
			if Dist == r:
				gfxdraw.pixel(screen, int(i), int(j), black)
				pygame.display.update()

	while True:
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				pygame.quit()
				sys.exit()



DDA_circle(h,k,r)

