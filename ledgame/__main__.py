try:
    from sense_hat import SenseHat
    sense = SenseHat()
except ImportError:
    from notpi import NotPi
    sense = NotPi(scale=64)

from ledgame.character import Character
from ledgame.world import World
from os import path

w = [0xFF, 0xFF, 0xFF]
b = [0x0, 0x0, 0x0]

worlds = ["test.png", "tiny.png", "tiny.png"]
world_number = 0

def get_level(filename):
    return path.join(path.dirname(path.abspath(__file__)), "levels", filename)


def change_level(world_number, char):
    char.total_gold += char.gold
    char.gold = 0
    world = World(get_level(worlds[world_number]))
    print("Total gold in this level: {}".format(world.gold))
    char.start(world.player_start)
    view = world.view(char)
    sense.set_pixels(view)
    sense.set_pixel(3, 4, char.color)
    return world

char = Character()
world = change_level(world_number, char)

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "right":
                char.move(1, 0, world)
            elif event.direction == "left":
                char.move(-1, 0, world)
            elif event.direction == "up":
                char.move(0, -1, world)
            elif event.direction == "down":
                char.move(0, 1, world)
            elif event.direction == "middle":
                sense.low_light = not sense.low_light
            view = world.view(char)
            sense.set_pixels(view)
            sense.set_pixel(3, 4, char.color)
    if char.gold == world.gold:
        world_number += 1
        if world_number < len(worlds):
            world = change_level(world_number, char)
        else:
            char.total_gold += char.gold
            sense.show_message("You win!")
            sense.show_message("You earned: {}".format(char.total_gold))
            break
    if type(sense).__name__ == "NotPi":
        sense.update()
