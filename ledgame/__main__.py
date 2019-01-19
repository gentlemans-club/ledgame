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

char = Character()
world = World(path.join(path.dirname(path.abspath(__file__)), "test.png"))

view = world.view(char)
sense.set_pixels(view)
sense.set_pixel(3, 4, char.color)

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
            view = world.view(char)
            sense.set_pixels(view)
            sense.set_pixel(3, 4, char.color)
    if char.gold == world.gold:
        sense.clear()
        sense.show_message("You win!")
        break
