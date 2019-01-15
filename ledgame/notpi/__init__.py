import pygame
import sys

class NotPi:
    def __init__(self, scale=16):
        self.scale = scale
        pygame.init()
        self.size = width, height = 8*self.scale, 8*self.scale
        self.screen = pygame.display.set_mode(self.size)

    def set_pixels(self, pixels):
        self.rects = []
        posy = -1
        posx = -1
        for idx, pixel in enumerate(pixels):
            if idx % 8 == 0:
                posx = 0
            if idx % 8 == 0:
                posy += 1

            self.rects.append((pygame.Rect(posx*self.scale, posy*self.scale, self.scale, self.scale), pixel))

            posx += 1
        self.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        self.screen.fill((0,0,0))
        for rect, color in self.rects:
            pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()
