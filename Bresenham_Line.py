import pygame
from pygame import gfxdraw
import sys

x0 = int(input('X0 co-ordinates:'))
y0 = int(input('Y0 co-ordinates:'))

x1 = int(input('X1 co-ordinates:'))
y1 = int(input('Y1 co-ordinates:'))


def Bresenham_Line(x0,y0,x1,y1):
    print('Points : {}, {} and {}, {}'.format(x0,y0,x1,y1))

    dy = y1 - y0
    dx = x1 - x0

    m = dy / dx

    print('Slope: {}'.format(m))

    pygame.init()

    black = (0, 0, 0)
    white = (255, 255, 255)

    size = [600,480]
    screen = pygame.display.set_mode(size)

    screen.fill(white)

    DV = (dx - 2*dy)

    print('points {},{}'.format(DV, x0,y0))

    gfxdraw.pixel(screen, int(x0), int(y0), black)
    pygame.display.update()

    if dx > dy:

        while x0 < x1:

            if DV >= 0:

                x0 = x0 + 1
                y0 = y0 

                DV = DV - 2*dy

                print('points {},{}'.format(DV, x0,y0))

                gfxdraw.pixel(screen, int(x0), int(y0), black)
                pygame.display.update()


            if DV < 0:

                x0 = x0 + 1
                y0 = y0 + 1

                DV = DV - 2*(dy - dx)

                print('points {},{}'.format(DV, x0,y0))

                gfxdraw.pixel(screen, int(x0), int(y0), black)
                pygame.display.update()

        while True:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    sys.exit()




Bresenham_Line(x0,y0,x1,y1)
