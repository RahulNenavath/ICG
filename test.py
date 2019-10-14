import pygame
from pygame import gfxdraw
import sys

screen = pygame.display.set_mode((640, 480))
running = 1

blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)
white = (255,255,255)
green = (0,128,0)
black = (0,0,0)

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	# screen.fill((0,0,0))

	screen.fill(white)

	pygame.draw.circle(screen, blue, (100,200), 60, 8)
	pygame.draw.circle(screen, black, (230,200), 60, 8)
	pygame.draw.circle(screen, red, (360,200), 60, 8)
	pygame.draw.circle(screen, yellow, (170,260), 60, 8)
	pygame.draw.circle(screen, green, (300,260), 60, 8)


	pygame.display.update()