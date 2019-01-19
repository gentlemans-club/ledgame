from pprint import pprint
from PIL import Image

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GOLD = [0xFF, 0xD7, 0x00]

class World:
    def __init__(self, mapfile):
        self.map = []
        self.gold = 0
        with Image.open(mapfile) as im:
            pix = im.load()
            width, height = im.size
        for y in range(height):
            mapline = []
            for x in range(width):
                pixel = list(pix[x, y][:3])
                if pixel == GOLD:
                    self.gold += 1
                mapline.append(pixel)
            self.map.append(mapline)

    def view(self, char):
        subsection = []
        for line in self.map[char.y-4:char.y+4]:
            subsection += line[char.x-4:char.x+4]
        return subsection
