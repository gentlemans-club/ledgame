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

Color |    Hex    | Notes
------|-----------|-------
Black | `#000000` | Represents floor. The player can walk on this.
White | `#FFFFFF` | Represents walls. The player cannot walk nor pass through this.
Blue  | `#0000FF` | Represents the player. It is advised to only have a single pixel of this type. In case of several, a random blue pixel will be chosen. The others will be turned to floor.
Gold  | `#FFD700` | Represents coins or gold. There must be at least one gold pixel in the level, as the completion criteria is for the player to pick up every coin in the level.
