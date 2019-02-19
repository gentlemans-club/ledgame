from ledgame import BLACK, WHITE, GOLD, GRAY, BROWN, RED

class Character:
    def __init__(self):
        self.color = [0x00, 0x00, 0xFF]
        self.x = 0
        self.y = 0
        self.gold = 0
        self.moving = {
            "left": False,
            "right": False,
            "down": False,
            "up": False
        }
        self.total_gold = 0

    def start(self, start_pos):
        """
        Sets the character position to a position, and resets
        the gold.
        """
        self.x = start_pos[0] + 9
        self.y = start_pos[1] + 8
        self.gold = 0

    def move(self, direction, world):
        """
        Moves the character in a specified direction. The function
        returns True or False depending on if a move is successful.
        """
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

        if world.map[new_y][new_x - 1] == WHITE:
            return False

        if world.map[new_y][new_x - 1] == GRAY:
            box_y = new_y + delta_y
            box_x = new_x + delta_x
            if world.map[box_y][box_x - 1] == BLACK:
                world.map[box_y][box_x - 1] = GRAY
                world.map[new_y][new_x - 1] = BLACK
                self.x = new_x
                self.y = new_y
                return True
            else:
                return False

        self.x = new_x
        self.y = new_y

        if world.map[self.y][self.x - 1] == GOLD:
            world.map[self.y][self.x - 1] = BLACK
            self.gold += 1
            print("Current gold: {}".format(self.gold))

        if world.map[self.y][self.x - 1] == BROWN:
            print(world.portals["brown"])
            idx = world.portals["brown"].index((self.x - 1, self.y))
            next_portal = world.portals["brown"][(idx + 1) % len(world.portals["brown"])]
            self.x = next_portal[0] + 1
            self.y = next_portal[1]


        return True
