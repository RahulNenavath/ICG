import pygame
from pygame import gfxdraw
import sys

screen = pygame.display.set_mode((640, 480))
running = 1

blue = 0,0,255
yellow = 255,255,0

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((0,0,0))

	#Basic Box:
	pygame.draw.line(screen,blue, (180,200), (180,350))
	pygame.draw.line(screen,blue, (180,200), (420,200))
	pygame.draw.line(screen,blue, (420,200), (420,350))
	pygame.draw.line(screen,blue, (161,350), (420,350))
	
	#Footer Line for house:
	pygame.draw.line(screen,blue, (420,350), (440,350))
	pygame.draw.line(screen,blue, (440,350), (440,360))
	pygame.draw.line(screen,blue, (160,350), (160,350))
	pygame.draw.line(screen,blue, (160,350), (160,360))
	pygame.draw.line(screen,blue, (160,360), (440,360))

	#top triangle:
	pygame.draw.line(screen,blue, (180,200), (300,100))
	pygame.draw.line(screen,blue, (300,100), (420,200))

	#Sun :) 
	pygame.draw.circle(screen, yellow, (510,100), 50)

	#Door:
	pygame.draw.line(screen,blue, (270,350), (270,290))
	pygame.draw.line(screen,blue, (330,350), (330,290))
	pygame.draw.line(screen,blue, (270,290), (330,290))

	#Window Left:
	pygame.draw.line(screen,blue, (200,250), (240,250))
	pygame.draw.line(screen,blue, (200,280), (240,280))
	pygame.draw.line(screen,blue, (200,250), (200,280))
	pygame.draw.line(screen,blue, (240,250), (240,280))

	#Window Right:
	pygame.draw.line(screen,blue, (360,250), (400,250))
	pygame.draw.line(screen,blue, (360,280), (400,280))
	pygame.draw.line(screen,blue, (360,250), (360,280))
	pygame.draw.line(screen,blue, (400,280), (400,250))

	pygame.display.flip()


