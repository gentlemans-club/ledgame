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

or for a development setup, run:
```sh
pip install -e --process-dependency-links .
```

To run the game, simply run:
```sh
python -m ledgame
```

* Note: On Mac, you may have to switch out `pip`/`python` commands with
`pip3`/`python3` respectively. 
