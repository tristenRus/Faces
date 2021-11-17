#####################################
# Copyright (c) 2021 Tristen Starnes
# CSCI 150, Fall 2021
# Lab 10: Graphics and Animation
#####################################
import math
import pygame
from pygame.locals import *


def draw_all(surface):
    surface.fill('white')
    pygame.draw.polygon(surface, 'black', ((280, 220), (305, 220), (305, 170)))
    pygame.draw.polygon(surface, 'black', ((335, 220), (360, 220), (335, 170)))
    pygame.draw.circle(surface, 'yellow', (320, 240), 50)
    pygame.draw.ellipse(surface, 'black', (295, 220, 15, 30), 15)
    pygame.draw.ellipse(surface, 'black', (330, 220, 15, 30), 15)
    pygame.draw.ellipse(surface, 'black', (318, 245, 5, 10), 5)
    #pygame.draw.arc(surface, 'black', (300, 250, 40, 20), ((5*math.pi)/4), ((7*math.pi)/4), width=3) # Mouth Up
    pygame.draw.arc(surface, 'black', (300, 265, 40, 20), (math.pi / 4), ((3 * math.pi) / 4), width=3) # Mouth Down
    pygame.display.update()


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    running = True
    while running:
        draw_all(surface)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()


if __name__ == '__main__':
    main()
