import pygame, math
from pygame import gfxdraw

black = (0, 0, 0)
white = (255, 255, 255)

def draw (x,y, iterations, theta, length):
	if iterations > 0:
		length = (length/math.sqrt(2))
		draw(x,y,iterations-1,theta+45,length)
		draw((x + length * math.cos(math.radians (45 + theta))),
			(y + length*math.sin(math.radians(45 + theta))),
			iterations-1,theta - 45,length)

	else:
		X = x + (length * math.cos(math.radians(theta)))
		Y = y + (length * math.cos(math.radians(theta)))
		pygame.draw.line(screen, black, [x,y], [X,Y], 1)
		pygame.display.update()

def initiali_fractal(x,y,iterations,length, theta):
	draw(x,y,iterations,theta,length)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()

x = int(input("Enter the starting x coordinate: "))
y = int(input("Enter the starting x coordinate: "))

iterations = int(input("Enter the number of iterations: "))
length = float(input("Enter the length: "))
theta = 0

pygame.init()
size = [700, 700]
screen = pygame.display.set_mode(size)
screen.fill(white)

initiali_fractal(x,y,iterations,length,theta)

pygame.quit()