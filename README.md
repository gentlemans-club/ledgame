# ledgame
THE LABYRINTH OF DOOM

Have a look at our [wiki](https://github.com/gentlemans-club/ledgame/wiki) for information about creating or editing levels.

**Developers:**

* [Elias Kløverød Brynestad](https://github.com/KodeGeniElias)
* [Kent Daleng](https://github.com/chinatsu)
* [Julie Hodne Gundersen](https://github.com/Juliehg)
* [Yaguel van der Meij](https://github.com/Yagooza)
* [Phuong Ha Pham](https://github.com/fongha)

**Included repositories**
* [ledgame](https://github.com/gentlemans-club/ledgame)
> Main repository for use with the Raspberry Pi
* [notpi](https://github.com/gentlemans-club/notpi) 
> Secondary repository for use on platforms such as MacOS, Windows & Linux


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

