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

world = World(path.join(path.dirname(path.abspath(__file__)), "levels", "Spiral of fuck you.png"))
char = Character(world.player_start)

print("Total gold in this level: {}".format(world.gold))

view = world.view(char)
sense.set_pixels(view)
sense.set_pixel(3, 4, char.color)

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == "right":
                char.moving_right = True
            elif event.direction == "left":
                char.moving_left = True
            elif event.direction == "up":
                char.moving_up = True
            elif event.direction == "down":
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
        char.move(1, 0, world)
        view = world.view(char)
        sense.set_pixels(view)
        sense.set_pixel(3, 4, char.color)
    if char.moving_left:
        char.move(-1, 0, world)
        view = world.view(char)
        sense.set_pixels(view)
        sense.set_pixel(3, 4, char.color)
    if char.moving_down:
        char.move(0, 1, world)
        view = world.view(char)
        sense.set_pixels(view)
        sense.set_pixel(3, 4, char.color)
    if char.moving_up:
        char.move(0, -1, world)
        view = world.view(char)
        sense.set_pixels(view)
        sense.set_pixel(3, 4, char.color)
    if char.gold == world.gold:
        world = World(path.join(path.dirname(path.abspath(__file__)), "levels", "elias2.png"))
        char = Character(world.player_start)
        break
    if type(sense).__name__ == "NotPi":
        sense.update()
