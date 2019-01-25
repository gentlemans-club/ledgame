try:
    from sense_hat import SenseHat
    sense = SenseHat()
except ImportError:
    from notpi import NotPi
    sense = NotPi(scale=64)

from ledgame.character import Character
from ledgame.world import World
from os import path
import time

w = [0xFF, 0xFF, 0xFF]
b = [0x0, 0x0, 0x0]

last_moved = time.time()
worlds = ["test.png", "tiny.png", "tiny.png"]
world_number = 0

def get_level(filename):
    return path.join(path.dirname(path.abspath(__file__)), "levels", filename)

def animate_load():
    loading_files = ["loading{}.png".format(x) for x in range(1,24)]
    for file in loading_files:
        sense.load_image(path.join(path.dirname(path.abspath(__file__)), "assets", file))
        time.sleep(0.03)

def change_level(world_number, char):
    animate_load()
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
        if event.action == 'pressed':
            if event.direction == "right":
                char.move(1, 0, world)
                view = world.view(char)
                sense.set_pixels(view)
                sense.set_pixel(3, 4, char.color)
                last_moved = time.time()
                char.moving_right = True
            elif event.direction == "left":
                char.move(-1, 0, world)
                view = world.view(char)
                sense.set_pixels(view)
                sense.set_pixel(3, 4, char.color)
                last_moved = time.time()
                char.moving_left = True
            elif event.direction == "up":
                char.move(0, -1, world)
                view = world.view(char)
                sense.set_pixels(view)
                sense.set_pixel(3, 4, char.color)
                last_moved = time.time()
                char.moving_up = True
            elif event.direction == "down":
                char.move(0, 1, world)
                view = world.view(char)
                sense.set_pixels(view)
                sense.set_pixel(3, 4, char.color)
                last_moved = time.time()
                char.moving_down = True
            elif event.direction == "middle":
                sense.low_light = not sense.low_light
        if event.action == 'released':
            if event.direction == "right":
                char.moving_right = False
            elif event.direction == "left":
                char.moving_left = False
            elif event.direction == "up":
                char.moving_up = False
            elif event.direction == "down":
                char.moving_down = False
    if char.moving_right:
        if time.time() - last_moved > 0.15:
            char.move(1, 0, world)
            view = world.view(char)
            sense.set_pixels(view)
            sense.set_pixel(3, 4, char.color)
            last_moved = time.time()
    if char.moving_left:
        if time.time() - last_moved > 0.15:
            char.move(-1, 0, world)
            view = world.view(char)
            sense.set_pixels(view)
            sense.set_pixel(3, 4, char.color)
            last_moved = time.time()
    if char.moving_down:
        if time.time() - last_moved > 0.15:
            char.move(0, 1, world)
            view = world.view(char)
            sense.set_pixels(view)
            sense.set_pixel(3, 4, char.color)
            last_moved = time.time()
    if char.moving_up:
        if time.time() - last_moved > 0.15:
            char.move(0, -1, world)
            view = world.view(char)
            sense.set_pixels(view)
            sense.set_pixel(3, 4, char.color)
            last_moved = time.time()
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
