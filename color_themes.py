import random
import pygame

Themes_Dict = {'Spongebob': [(255, 245, 108), (163, 211, 195), (38, 185, 200), (4, 87, 160), (249, 171, 167),
                             (255, 59, 59), (113, 152, 112), (255, 211, 137)],
               'Pokemon': [(238, 131, 40), (137, 200, 147), (85, 163, 171), (250, 214, 29), (255, 170, 255),
                           (197, 145, 93), (41, 115, 143)],
               'Pacman': [pygame.Color('#FF0000'), pygame.Color('#FFB8FF'), pygame.Color('#00FFFF'),
                          pygame.Color('#FFB852'), pygame.Color('#FFFF00'), pygame.Color('#FD0000'),
                          pygame.Color('#00FF00'), pygame.Color('#2121DE')]}

spongebob_background = pygame.image.load(r'C:\Users\Tristen\Desktop\PycharmProjects\Faces\backgrounds\wp2891267'
                                         r'-spongebob-flower-sky-background.jpg')
pokemon_background = pygame.image.load(r'C:\Users\Tristen\Desktop\PycharmProjects\Faces\backgrounds\nature'
                                       r'-1637029136680-6488.jpg')
pacman_background = pygame.image.load(r'C:\Users\Tristen\Desktop\PycharmProjects\Faces\backgrounds\Pac-Man Maze '
                                      r'Wallpaper by spdy4 on DeviantArt.jpg')


def choose_theme():
    choice = random.choice(list(Themes_Dict))
    return choice, Themes_Dict[choice]
