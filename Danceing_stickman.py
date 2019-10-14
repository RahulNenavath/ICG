import pygame
from pygame import gfxdraw
import sys,time, math

pygame.init()

screen = pygame.display.set_mode((600,480))
running = 1

blue = 0,0,255
white = 255, 255, 255
black = 0,0,0

while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill(black)

	#Stick man: Act 1:
	pygame.draw.circle(screen, blue, (300,140), 30,1)	#Face
	pygame.draw.circle(screen, white, (290,140), 5,1)	#Eyes
	pygame.draw.circle(screen, white, (310,140), 5,1)
	pygame.draw.arc(screen, blue, [285,142,30,20],(math.pi),0)	#smile
	pygame.draw.line(screen,blue, (300,170),(300,190))	#Neck	
	pygame.draw.line(screen,blue, (300,190),(230,210))	#Left hand
	pygame.draw.line(screen,blue, (300,190),(370,210))	#Right hand
	pygame.draw.line(screen,blue, (300,190),(300,250))	#Body
	pygame.draw.line(screen,blue, (300,250),(250,310))	#Left Leg
	pygame.draw.line(screen,blue, (300,250),(350,310))	#Right Leg
	pygame.draw.line(screen,blue, (250,310),(230,310))	#Left Foot
	pygame.draw.line(screen,blue, (350,310),(370,310))	#Right Foot

	pygame.display.update()
	screen.fill(black)
	pygame.time.delay(500)

	#Stick man: Act 2:
	pygame.draw.circle(screen, blue, (300,140), 30,1)	#Face
	pygame.draw.circle(screen, white, (290,140), 5,1)	#Eyes
	pygame.draw.circle(screen, white, (310,140), 5,1)
	pygame.draw.arc(screen, blue, [285,142,30,20],(math.pi),0)	#smile
	pygame.draw.line(screen,blue, (300,170),(300,190))	#Neck	
	pygame.draw.line(screen,blue, (300,190),(230,210))	#Left hand
	pygame.draw.line(screen,blue, (300,190),(370,210))	#Right hand
	pygame.draw.line(screen,blue, (300,190),(300,250))	#Body
	pygame.draw.line(screen,blue, (230,210),(220,200))	#Left fist
	pygame.draw.line(screen,blue, (370,210),(380,200))	#Right fist
	pygame.draw.line(screen,blue, (300,250),(250,310))	#Left Leg
	pygame.draw.line(screen,blue, (300,250),(350,310))	#Right Leg
	pygame.draw.line(screen,blue, (250,310),(230,310))	#Left Foot
	pygame.draw.line(screen,blue, (350,310),(370,310))	#Right Foot


	pygame.display.update()
	pygame.time.delay(500)
	screen.fill(black)

	#Stick man: Act 3:
	pygame.draw.circle(screen, blue, (300,160), 30,1)	#Face
	pygame.draw.circle(screen, white, (290,160), 5,1)	#Eyes
	pygame.draw.circle(screen, white, (310,160), 5,1)
	pygame.draw.line(screen,blue, (285,170),(315,170))	#Teeth
	pygame.draw.arc(screen, blue, [285,160,30,20],(math.pi),0)
	pygame.draw.line(screen,blue, (300,190),(300,210))	#Neck	
	pygame.draw.line(screen,blue, (300,210),(230,230))	#Left hand
	pygame.draw.line(screen,blue, (300,210),(370,230))	#Right hand
	pygame.draw.line(screen,blue, (300,190),(300,260))	#Body
	pygame.draw.line(screen,blue, (230,230),(220,220))	#Left fist
	pygame.draw.line(screen,blue, (370,230),(380,220))	#Right fist

	pygame.draw.line(screen,blue, (300,260),(250,260))	#Left Leg
	pygame.draw.line(screen,blue, (250,260),(250,310))
	pygame.draw.line(screen,blue, (300,260),(350,260))	#Right Leg
	pygame.draw.line(screen,blue, (350,260),(350,310))

	pygame.draw.line(screen,blue, (250,310),(230,310))	#Left Foot
	pygame.draw.line(screen,blue, (350,310),(370,310))	#Right Foot

	pygame.display.update()
	pygame.time.delay(500)
	screen.fill(black)

	#Stick man: Act 4:
	pygame.draw.circle(screen, blue, (300,160), 30,1)	#Face
	pygame.draw.circle(screen, white, (290,160), 5,1)	#Eyes
	pygame.draw.circle(screen, white, (310,160), 5,1)
	pygame.draw.line(screen,blue, (285,170),(315,170))	#Teeth
	pygame.draw.arc(screen, blue, [285,160,30,20],(math.pi),0)
	pygame.draw.line(screen,blue, (300,190),(300,210))	#Neck	
	pygame.draw.line(screen,blue, (300,210),(230,180))	#Left hand
	pygame.draw.line(screen,blue, (300,210),(370,180))	#Right hand
	pygame.draw.line(screen,blue, (300,190),(300,260))	#Body
	pygame.draw.line(screen,blue, (230,180),(230,170))	#Left fist
	pygame.draw.line(screen,blue, (370,180),(370,170))	#Right fist

	pygame.draw.line(screen,blue, (300,260),(250,260))	#Left Leg
	pygame.draw.line(screen,blue, (250,260),(250,310))
	pygame.draw.line(screen,blue, (300,260),(350,260))	#Right Leg
	pygame.draw.line(screen,blue, (350,260),(350,310))

	pygame.draw.line(screen,blue, (250,310),(230,310))	#Left Foot
	pygame.draw.line(screen,blue, (350,310),(370,310))	#Right Foot

	pygame.display.update()
	pygame.time.delay(500)
	screen.fill(black)

	#Stick man: Act 5:
	pygame.draw.circle(screen, blue, (300,140), 30,1)	#Face
	pygame.draw.circle(screen, white, (290,140), 5,1)	#Eyes
	pygame.draw.circle(screen, white, (310,140), 5,1)
	pygame.draw.arc(screen, blue, [285,142,30,20],(math.pi),0)	#smile
	pygame.draw.line(screen,blue, (300,170),(300,190))	#Neck	
	pygame.draw.line(screen,blue, (300,190),(250,230))	#Left hand
	pygame.draw.line(screen,blue, (300,190),(350,230))	#Right hand
	pygame.draw.line(screen,blue, (300,190),(300,250))	#Body
	pygame.draw.line(screen,blue, (300,250),(270,310))	#Left Leg
	pygame.draw.line(screen,blue, (300,250),(340,310))	#Right Leg
	pygame.draw.line(screen,blue, (270,310),(250,310))	#Left Foot
	pygame.draw.line(screen,blue, (340,310),(360,310))	#Right Foot

	pygame.display.update()
	screen.fill(black)
	pygame.time.delay(500)

