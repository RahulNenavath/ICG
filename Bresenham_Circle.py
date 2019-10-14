import pygame
from pygame import gfxdraw
import sys


xc = int(input('Center: Xc =  '))
yc = int(input('Center: Yc = '))
r = int(input('Radius of circle: '))

def Bresenham_Cirle(xc,yc,r):

	p0 = 3 - 2*r

	x,y = 0,r

	pygame.init()

	black = (0,0,0)
	white = (255,255,255)

	size = [600,480]
	screen = pygame.display.set_mode(size)

	screen.fill(black)

	circleQuadrants(screen,white,xc,yc,x,y)

	while x <= y:

		if p0 < 0:

			x,y = x+1, y

			p1 = p0 + 4*x + 6

			p0 = p1

			print('points: {},{}'.format(x,y))

			circleQuadrants(screen,white,xc,yc,x,y)

		if p0 >= 0:

			x,y = x+1, y - 1

			p1 = p0 + 4*(x - y) + 10

			p0 = p1

			print('points: {},{}'.format(x,y))

			circleQuadrants(screen,white,xc,yc,x,y)
			
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()


def circleQuadrants(screen,white,xc,yc,x,y):

	gfxdraw.pixel(screen, int(xc+x), int(yc+y), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc-x), int(yc+y), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc+x), int(yc-y), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc-x), int(yc-y), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc+y), int(yc+x), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc-y), int(yc+x), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc+y), int(yc-x), white)
	pygame.display.update()

	gfxdraw.pixel(screen, int(xc-y), int(yc-x), white)
	pygame.display.update()

	



Bresenham_Cirle(xc,yc,r)