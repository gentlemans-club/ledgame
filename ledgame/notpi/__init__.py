import pygame
import sys

class NotPi:
    def __init__(self):
        pygame.init()
        size = width, height = 8*16, 8*16
        self.screen = pygame.display.set_mode(size)

    def set_pixels(self, pixels):
        self.rects = []
        posy = -1
        posx = -1
        for idx, pixel in enumerate(pixels):
            if idx % 8 == 0:
                posx = 0
            if idx % 8 == 0:
                posy += 1

            self.rects.append((pygame.Rect(posx*16, posy*16, 16, 16), pixel))

            posx += 1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        self.screen.fill((0,0,0))
        for rect, color in self.rects:
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()
