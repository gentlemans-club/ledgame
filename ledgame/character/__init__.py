class Character:
    def __init__(self):
        self.color = [0x00, 0x00, 0xFF]
        self.x = 16
        self.y = 15
        self.gold = 0

    def move(self, delta_x, delta_y, world):
        new_x = self.x + delta_x
        new_y = self.y + delta_y

        if world.map[new_y][new_x - 1] == [0xFF, 0xFF, 0xFF]:
            return

        self.x = new_x
        self.y = new_y

        if world.map[self.y][self.x - 1] == [0xFF, 0xD7, 0x00]:
            world.map[self.y][self.x - 1] = [0x0, 0x0, 0x0]
            self.gold += 1
