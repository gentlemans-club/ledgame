from ledgame import BLACK, WHITE, GOLD, BLUE, BROWN, RED
from pprint import pprint
from PIL import Image
import random


class World:
    def __init__(self, mapfile):
        self.map = []
        self.portals = {
            "brown": []
        }
        self.gold = 0
        with Image.open(mapfile) as im:
            pix = im.load()
            width, height = im.size
        pad = 7
        real_width = width + (pad*2)
        possible_starts = []

        # first, pad the top of the map with 7 lines of black
        for p in range(pad):
            mapline = [BLACK] * real_width
            self.map.append(mapline)

        # create an outer wall
        self.map.append([BLACK] * pad + [WHITE] * (width+2) + [BLACK] * pad)

        for y in range(height):
            mapline = []
            # pad the line on the left side
            for p in range(pad):
                mapline.append(BLACK)
            # create an outer wall
            mapline.append(WHITE)

            # build from the actual map file
            for x in range(width):
                pixel = list(pix[x, y][:3])
                if pixel == GOLD:
                    self.gold += 1
                if pixel == BLUE:
                    possible_starts.append((x, y))
                    pixel = BLACK
                if pixel == BROWN:
                    self.portals["brown"].append((x + 8, y + 8))
                mapline.append(pixel)

            # create an outer wall
            mapline.append(WHITE)

            # pad the line on the right side
            for p in range(pad):
                mapline.append(BLACK)
            self.map.append(mapline)

        # create an outer wall
        self.map.append([BLACK] * pad + [WHITE] * (width+2) + [BLACK] * pad)

        # pad the bottom of the map with 7 lines of black
        for p in range(pad):
            mapline = [BLACK] * real_width
            self.map.append(mapline)

        self.player_start = random.choice(possible_starts)

    def view(self, char):
        """
        Creates a subsection of the map, centered around the character object.
        """
        subsection = []
        for line in self.map[char.y-4:char.y+4]:
            subsection += line[char.x-4:char.x+4]
        return subsection
