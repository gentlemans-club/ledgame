from pprint import pprint

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GOLD = [0xFF, 0xD7, 0x00]

class World:
    def __init__(self, mapfile):
        self.map = []
        self.gold = 0
        with open(mapfile) as f:
            for line in f:
                mapline = []
                for char in line:
                    if char == "#":
                        mapline.append(WHITE)
                    elif char == ".":
                        mapline.append(BLACK)
                    elif char == "g":
                        mapline.append(GOLD)
                        self.gold += 1
                self.map.append(mapline)

    def view(self, char):
        subsection = []
        for line in self.map[char.y-4:char.y+4]:
            subsection += line[char.x-4:char.x+4]
        return subsection

