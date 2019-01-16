# ledgame
THE LABYRINTH OF DOOM

## Requirements

* Python 3.6 or newer
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
