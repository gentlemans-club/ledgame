# ledgame
THE LABYRINTH OF DOOM

## Requirements

* Python 3.5 or newer
* Sense HAT library
  * Only required on Raspberry Pi.
* notpi

## Installation

Clone the repository. Within the Git repository, run the following:
```sh
pip install --process-dependency-links .
```

To run the game, simply run:
```sh
python -m ledgame
```

### Development version
For development, it is recommended that you clone and install a development version of [notpi](https://github.com/gentlemans-club/notpi) by cloning
and running `pip install -e .` from within the notpi repository.
Then within ledgame's repository, run `pip install -e .` to install that.
This way, you will have editable installations of both notpi and ledgame installed.

* Note: On Mac, you may have to switch out `pip`/`python` commands with
`pip3`/`python3` respectively.


## Creating levels

Creating levels is as easy as using image editing software to draw it. Each pixel represents a cell in the game.
The image format should be PNG with an RGBA format. Examples can be found in the levels directory. Note that this standard will be extended upon with other types of pixels.

The pixel can have one of four colors:

Type |    Hex    | Notes
------|-----------|-------
Floor | `#000000` | The player can walk on this.
Wall | `#FFFFFF` | The player cannot walk nor pass through this.
Player  | `#0000FF` | It is advised to only have a single pixel of this type. In case of several, a random blue pixel will be chosen. The others will be turned to floor.
Gold  | `#FFD700` |There must be at least one gold pixel in the level, as the completion criteria is for the player to pick up every coin in the level.
Box | `#555555` | Can be moved by the player. Boxes cannot move into other objects such as walls, gold, or other boxes.
Key | `#00AA00` | Can be picked up by the player. Unlocks doors, which also consumes the key.
Door | `#C400C4`  | Can be unlocked by a player with a key. Acts like a wall if the player has no keys.
Teleport 1 | `#FF0000` | Teleports to another cell of type teleport 1. If three or more teleports of the same type is present, the teleport sends the player in a cycle through all of them.
Teleport 2 | `#A05000` | Teleports to another cell of type teleport 2.
Teleport 3 | `#00FFFF` | Teleports to another cell of type teleport 3.
