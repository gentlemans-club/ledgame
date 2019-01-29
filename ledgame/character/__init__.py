class Character:
    def __init__(self):
        self.color = [0x00, 0x00, 0xFF]
        self.x = 0
        self.y = 0
        self.gold = 0
        self.total_gold = 0

    def start(self, start_pos):
        self.x = start_pos[0] + 9
        self.y = start_pos[1] + 8
        self.moving = {
            "left": False,
            "right": False,
            "down": False,
            "up": False
        }
        self.gold = 0

    def move(self, direction, world):
        delta_x = 0
        delta_y = 0
        if direction == "right":
            delta_x = 1
        elif direction == "left":
            delta_x = -1
        elif direction == "up":
            delta_y = -1
        elif direction == "down":
            delta_y = 1
            
        new_x = self.x + delta_x
        new_y = self.y + delta_y

        if world.map[new_y][new_x - 1] == [0xFF, 0xFF, 0xFF]:
            return

        self.x = new_x
        self.y = new_y

        if world.map[self.y][self.x - 1] == [0xFF, 0xD7, 0x00]:
            world.map[self.y][self.x - 1] = [0x0, 0x0, 0x0]
            self.gold += 1
            print("Current gold: {}".format(self.gold))
