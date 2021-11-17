import pygame
from pygame.locals import *


class Face:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.circle(surface, 'red', (self.x, self.y), 100)
        pygame.draw.circle(surface, 'yellow', (self.x - 25, self.y - 25), 35)
        pygame.draw.circle(surface, 'yellow', (self.x + 25, self.y - 25), 35)
        pygame.draw.line(surface, 'orange', (self.x - 20, self.y + 30), (self.x + 20, self.y + 30))


def draw_all(surface, shapes):
    surface.fill('black')
    for shape in shapes:
        shape.draw(surface)
    pygame.display.update()


def main():
    pygame.init()
    surface = pygame.display.set_mode((640, 480))
    shapes = []
    running = True
    while running:
        draw_all(surface, shapes)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                shapes.append(Face(event.pos[0], event.pos[1]))
    pygame.quit()


if __name__ == '__main__':
    main()