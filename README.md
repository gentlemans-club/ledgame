# ledgame
*This is an open source project part of the course IS-213, which is a course given on the University of Agder in Norway.* 

### THE LABYRINTH OF DOOM

Have a look at our [wiki](https://github.com/gentlemans-club/ledgame/wiki) for information about creating or editing levels. We have also included a Jupyter [notebook](https://github.com/gentlemans-club/ledgame/blob/master/ledgame.ipynb) to be able to illustrate how the code works.

**Developers:**

* [Elias Kløverød Brynestad](https://github.com/KodeGeniElias)
* [Kent Daleng](https://github.com/chinatsu)
* [Julie Hodne Gundersen](https://github.com/Juliehg)
* [Yaguel van der Meij](https://github.com/Yagooza)
* [Phuong Ha Pham](https://github.com/fongha)


**Included repositories**
> The main repository for use with the Raspberry Pi
* [ledgame](https://github.com/gentlemans-club/ledgame)

> Secondary repository for use on platforms such as MacOS, Windows & Linux
* [notpi](https://github.com/gentlemans-club/notpi) 


----

## What

Ledgame is a labyrinth game where the player will attempt to navigate through a labyrinth and encounter dangers as well as treasures. The game will make use of various colours to represent walls, floor, treasures, dangers, and the player itself. 

## Why

The main purpose of ledgame is to get an introduction and exercise on hardware by using Raspberry Pi 3. We wanted to make it as simple and user friendly as possible to give people the opportunity to make their own levels and gain an understanding of the game logic through that. 


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

