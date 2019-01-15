import pygame
import sys
import numpy as np

class NotPi:
    def __init__(self, scale=16):
        black = [0, 0, 0]
        self.pixels = [black] * 64
        self.scale = scale
        pygame.init()
        self.size = width, height = 8*self.scale, 8*self.scale
        self.screen = pygame.display.set_mode(self.size)
        self.update()

    def set_pixels(self, pixels):
        self.pixels = pixels
        self.update()

    def flip_v(self, redraw=True):
        """
        Flips the image on the canvas vertically.
        """
        self.pixels = np.flipud(self.pixels)
        if redraw:
            self.update()


    def update(self):
        rects = []
        posy = -1
        posx = -1
        for idx, pixel in enumerate(self.pixels):
            if idx % 8 == 0:
                posx = 0
                posy += 1

            rects.append((pygame.Rect(posx*self.scale, posy*self.scale, self.scale, self.scale), pixel))
            posx += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        self.screen.fill((0,0,0))
        for rect, color in rects:
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()
