# counterattack
**Now you can generate your own Counter Attack player cards for real-life players!**

<img src="https://github.com/cbrown4858/counterattack/blob/main/images/counterattack_logo.png" width=100% height=100% align=center>
<img src="https://github.com/cbrown4858/counterattack/blob/main/images/fminside_logo.png" width=30% height=30% align=right>

This python package creates a 'Counter Attack: The Football Strategy Game' player card data file for any real-life player(s) with 'Football Manager' data from [FMInside](https://fminside.net/). The player card data file that is created is intended to be used with the Counter Attack Custom Card Generator created by [Konrad Frac](https://github.com/kkoripl).  
  
_This package wouldn't be possible without the data from FMInside and the custom card generator from Konrad Franc. Thank you._  

## Installation

- Step 1: clone this repository, and cd into it.
- Step 2: create a virtual environment in whatever your favorite way to do that is (e.g. `conda create -n my_env` -> `conda activate my_env`).
- Step 3: `pip install .` will install this repo such that you can use `from counterattack.xxx.yyy import zzz`.
    - NOTE: You may have to install "pip" itself first in the new environement (e.g. `conda install pip`).

## User Guide

### For a player
- Step 1: find a player profile on [FMInside](https://fminside.net/)
- Step 2: run the following code in the terminal (without the brackets)
    - `python buildplayer.py --url X --export_dir Y`
    - X = URL to player
    - Y = full path to directory to save the resulting .xlsx file
    - _this assumes you're in the counterattacl/scripts/ directory_
- Step 3: upload .xlsx file to the [Counter Attack Custom Card Generator](https://kkoripl.github.io/CACCGeneratorWeb/custom-cards)
- Step 4: click 'Generate PDF' in the card generator's UI. Download the PDF.

### For a club
- Step 1: find a player profile on [FMInside](https://fminside.net/)
- Step 2: run the following code in the terminal (without the brackets)
    - `python buildclub.py --url X --export_dir Y --export_squad_size Z`
    - X = URL to player
    - Y = full path to directory to save the resulting .xlsx file
    - Z = 'full' for the full squad, or a number for the top number of players from the squad
    - _this assumes you're in the counterattacl/scripts/ directory_
- Step 3: upload .xlsx file to the [Counter Attack Custom Card Generator](https://kkoripl.github.io/CACCGeneratorWeb/custom-cards)
- Step 4: click 'Generate PDF' in the card generator's UI. Download the PDF.

## Documentation

Find any documentation on usage of the different sections in the DOCSTRING of their corresponding files.
