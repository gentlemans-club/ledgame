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

last_moved = time.time()
worlds = ["elias.png", "pokepuzzle.png", "laby.png", "teleporttest.png", ]
world_number = 0

def get_level(filename):
    """
    A simple helper function which builds an absolute path to a level filename.
    """
    return path.join(path.dirname(path.abspath(__file__)), "levels", filename)

def animate_load():
    """
    Creates a level transition animation.
    """
    loading_files = ["loading{}.png".format(x) for x in range(1,24)]
    for file in loading_files:
        sense.load_image(path.join(path.dirname(path.abspath(__file__)), "assets", file))
        time.sleep(0.03)

def set_level(world_number, char): # used for changing to a new level and reloading level
    """
    Changes the level and soft-resets the character state.

    The total gold collected is stored, while current gold is reset.
    The character's position is also set to the new world's start position.

    If not all the gold is collected the world will reset when "middle" is held for longer then 3 seconds.
    """
    animate_load()
    char.total_gold += char.gold
    world = World(get_level(worlds[world_number]))
    print("Total gold in this level: {}".format(world.gold))
    char.start(world.player_start)
    return world

def draw(char):
    """
    Creates a world view around the character, and draws it.
    """
    view = world.view(char)
    sense.set_pixels(view)
    sense.set_pixel(3, 4, char.color)

char = Character()
world = set_level(world_number, char)
draw(char)

reset_timer = time.time() # variable that keeps track of when "middle" was pressed
reset_held = False # variable to keep track if "middle" is held

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction in ["right", "left", "up", "down"]:
                if char.move(event.direction, world):
                    last_moved = time.time()
                    char.moving[event.direction] = True
                    draw(char)
            elif event.direction == "middle":
                reset_timer = time.time() #start counting
                reset_held = True
                sense.low_light = not sense.low_light
        if event.action == 'released':
            if event.direction in ["right", "left", "up", "down"]:
                char.moving[event.direction] = False
            elif event.direction == "middle":
                reset_held = False
    if reset_held and time.time() - reset_timer > 3: # released after 3 seconds
                world = set_level(world_number, char)
                print("Level has been reloaled")
                draw(char)
    if any(list(char.moving.values())):
        for direction, value in char.moving.items():
            if value and time.time() - last_moved > 0.15:
                if char.move(direction, world):
                    last_moved = time.time()
                    draw(char)
    if char.gold == world.gold:
        world_number += 1
        if world_number < len(worlds):
            world = set_level(world_number, char)
            draw(char)
        else:
            char.total_gold += char.gold
            sense.show_message("You win!")
            sense.show_message("You earned: {}".format(char.total_gold))
            break
    if type(sense).__name__ == "NotPi":
        sense.update()
