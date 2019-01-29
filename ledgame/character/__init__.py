from ledgame import BLACK, WHITE, GOLD

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

        self.x = new_x
        self.y = new_y

        if world.map[self.y][self.x - 1] == GOLD:
            world.map[self.y][self.x - 1] = BLACK
            self.gold += 1
            print("Current gold: {}".format(self.gold))
        return True
