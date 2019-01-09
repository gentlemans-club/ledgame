import pygame
import sys

pygame.init()
size = width, height = 8*16, 8*16
black = 0, 0, 0

screen = pygame.display.set_mode(size)

def list_to_rects(pixels):
    rects = []
    posy = -1
    posx = -1
    for idx, pixel in enumerate(pixels):
        if idx % 8 == 0:
            posx = 0
        if idx % 8 == 0:
            posy += 1

        if pixel == 'x':
            rects.append(pygame.Rect(posx*16, posy*16, 16, 16))

        posx += 1
    return rects

pixels = [
    'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
    'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
    'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
    'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
    'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
    'o', 'o', 'o', 'x', 'o', 'x', 'o', 'o',
    'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
    'o', 'o', 'o', 'o', 'o', 'o', 'o', 'x',
]

rects = list_to_rects(pixels)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for rect in rects:
        pygame.draw.rect(screen, (255, 0, 0), rect)

    pygame.display.flip()
