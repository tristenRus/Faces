#####################################
# Copyright (c) 2021 Tristen Starnes
# CSCI 150, Fall 2021
# Lab 10: Graphics and Animation
#####################################
import math
import random
import pygame
import pyautogui
from pygame.locals import *
import color_themes
import pygame.freetype


class Face:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color
        self.velocity_x = random.uniform(0.5, 3) * random.choice([-1, 1])
        self.velocity_y = random.uniform(0.5, 3) * random.choice([-1, 1])
        self.timer = 0

    def draw_no_eyes(self, surface):
        pygame.draw.polygon(surface, 'black', ((self.x-40, self.y-20), (self.x-15, self.y-20), (self.x-15, self.y-70)))
        pygame.draw.polygon(surface, 'black', ((self.x+15, self.y-20), (self.x+40, self.y-20), (self.x+15, self.y-70)))
        pygame.draw.circle(surface, self.color, (self.x, self.y), 50)
        pygame.draw.ellipse(surface, 'black', (self.x - 2, self.y + 5, 5, 10), 5)

    def blink(self, surface):
        self.draw_no_eyes(surface)
        self.draw_mouth_up(surface)
        blink = random.randint(1, 200)
        if blink == 1:
            self.timer = 20
        if self.timer > 0:
            self.draw_eyes_shut(surface)
            self.timer -= 1
        elif blink != 1:
            self.draw_eyes_open(surface)

    def draw_eyes_open(self, surface):
        pygame.draw.ellipse(surface, 'black', (self.x - 25, self.y - 20, 15, 30), 15)
        pygame.draw.ellipse(surface, 'black', (self.x + 10, self.y - 20, 15, 30), 15)

    def draw_eyes_shut(self, surface):
        pygame.draw.line(surface, 'black', (self.x - 25, self.y - 5), (self.x - 10, self.y - 5), width=3)
        pygame.draw.line(surface, 'black', (self.x + 10, self.y - 5), (self.x + 25, self.y - 5), width=3)

    def draw_mouth_up(self, surface):
        pygame.draw.arc(surface, 'black', (self.x-20, self.y+10, 40, 20), ((5*math.pi)/4), ((7*math.pi)/4), width=3)

    def draw_mouth_down(self, surface):
        pygame.draw.arc(surface, 'black', (self.x-20, self.y+25, 40, 20), (math.pi/4), ((3*math.pi)/4), width=3)

    def draw_blush(self, surface):
        self.draw_no_eyes(surface)
        self.draw_eyes_shut(surface)
        self.draw_mouth_up(surface)
        pygame.draw.circle(surface, 'pink', (self.x - 30, self.y + 15), 10)
        pygame.draw.circle(surface, 'pink', (self.x + 30, self.y + 15), 10)

    def draw_angry(self, surface):
        self.draw_no_eyes(surface)
        self.draw_eyes_open(surface)
        self.draw_mouth_down(surface)
        pygame.draw.line(surface, 'black', (self.x - 20, self.y - 32), (self.x - 10, self.y - 22), width=3)
        pygame.draw.line(surface, 'black', (self.x + 10, self.y - 22), (self.x + 20, self.y - 32), width=3)

    def update(self, surface):
        self.x += self.velocity_x
        self.y += self.velocity_y
        if self.x + 50 >= surface.get_width() or self.x - 50 <= 0:
            self.velocity_x *= -1
        if self.y + 50 >= surface.get_height() or self.y - 70 <= 0:
            self.velocity_y *= -1


def faces_blush(surface, shapes, background):
    surface.fill('lightgray')
    surface.blit(background, (0, 0))
    for shape in shapes:
        shape.update(surface)
        shape.draw_blush(surface)
    pygame.display.update()


def faces_angry(surface, shapes, background):
    surface.fill('lightgray')
    surface.blit(background, (0, 0))
    for shape in shapes:
        shape.update(surface)
        shape.draw_angry(surface)
    pygame.display.update()


def draw_all(surface, shapes, background):
    surface.fill('lightgray')
    surface.blit(background, (0, 0))
    for shape in shapes:
        shape.update(surface)
        shape.blink(surface)
    pygame.display.update()


def get_background_theme():
    background, theme = color_themes.choose_theme()
    if background == 'Spongebob':
        background = color_themes.spongebob_background
    elif background == 'Pokemon':
        background = color_themes.pokemon_background
    elif background == 'Pacman':
        background = color_themes.pacman_background
    return background, theme


def delete_10(shapes):
    shapes = shapes[10:]
    return shapes


def main():
    pygame.init()
    width, height = pyautogui.size()
    surface = pygame.display.set_mode((width, height))
    background, theme = get_background_theme()
    shapes = []
    running = True
    while running:
        key = pygame.key.get_pressed()
        if key[pygame.K_b]:
            faces_blush(surface, shapes, background)
        elif key[pygame.K_a]:
            faces_angry(surface, shapes, background)
        else:
            draw_all(surface, shapes, background)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_DELETE:
                    shapes = delete_10(shapes)
                    timer = 125
                    while timer > 0:
                        faces_angry(surface, shapes, background)
                        timer -= 1
            if event.type == MOUSEBUTTONDOWN:
                color_picked = random.choice(theme)
                shapes.append(Face(event.pos[0], event.pos[1], color_picked))
        pygame.time.delay(15)
    pygame.quit()


if __name__ == '__main__':
    main()

# Themes ideas, make a dictionary
# DEL to delete the first 10-20 shapes made, all the rest get sad for a bit
# Angry face?
# Dog?
# Surprised face?
# Cat mouth??
# Collisions
# Button to stop rewriting the background
# Custom backgrounds
