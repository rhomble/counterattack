# counterattack
### _Now you can generate your own Counter Attack player cards for real-life players!_

<img src="https://github.com/cbrown4858/counterattack/blob/main/images/logos_big.png" width=100% height=100%>
  
This python package creates a .xlsx file with Counter Attack player card stats for any real-life footballers from their Football Manager attributes. This .xlsx file is intended to be used with the **Counter Attack Custom Card Generator** created by [Konrad Frac](https://github.com/kkoripl). The Football Manager data is scraped from [FMInside](https://fminside.net/).
  
<img src="https://github.com/cbrown4858/counterattack/blob/main/images/bumper_4.png" width=100% height=100%>  
  
## Installation
- Step 1: clone this repository, and cd into it.
- Step 2: create a virtual environment in whatever your favorite way to do that is (e.g. `conda create -n my_env` -> `conda activate my_env`).
- Step 3: `pip install .` will install this repo such that you can use `from counterattack.xxx.yyy import zzz`.
    - NOTE: You may have to install "pip" itself first in the new environement (e.g. `conda install pip`).

## User Guide
### For a player
1. find a player profile on [FMInside](https://fminside.net/)
2. run the following code in the terminal (without the brackets)
    - `python buildplayer.py --url X --export_dir Y`
    - X = URL to player
    - Y = full path to directory to save the resulting .xlsx file
    - _NOTE: this assumes you're in the counterattacl/scripts/ directory_
3. upload .xlsx file to the [Counter Attack Custom Card Generator](https://kkoripl.github.io/CACCGeneratorWeb/custom-cards)
4. click 'Generate PDF' in the card generator's UI. Download the PDF.

### For a club
1. find a club profile on [FMInside](https://fminside.net/)
2. run the following code in the terminal (without the brackets)
    - `python buildclub.py --url X --export_dir Y --export_squad_size Z`
    - X = URL to player
    - Y = full path to directory to save the resulting .xlsx file
    - Z = '_full_' for the full squad, or a number for the top number of players from the squad (this is optional, the default is 25)
    - _NOTE: this assumes you're in the directory /counterattacl/scripts/_
3. upload .xlsx file to the [Counter Attack Custom Card Generator](https://kkoripl.github.io/CACCGeneratorWeb/custom-cards)
4. click 'Generate PDF' in the card generator's UI. Download the PDF.

## Quirks
### Neymar can't tackle
If a player's Football Manager skills translate to a Counter Attack skill score of 0, that skill is given a value of 1 instead. This is due to Counter Attack not using 0s for skill values. According to the current translation (and _not_ adjusting the result to 1), Neymar's tackling rounds down to a Counter Attack tackling score of 0.

## Potential Issues
### Specific country names
  
If you get the error below when loading a .xlsx file to the Custom Card Generator, the issue is the country name on FMInside does not match any of the countries recognized by the Custom Card Generator. Both FMInside's version and the generator's version of the country name need to be added to the NATION_CONV dictionary in the fminside.py module. If you come across this error, let me know and I'll update the code. 
> _Error during player file uploading. Player has wrong country in row: xx_  

## Documentation
Find any documentation on usage of the different modules in the docstrings of their corresponding files.

## Want to contribute?
Fork this repository to make any changes you see fit! In particular, the FM_TO_CA_DICT in the player.py module. This is what translates Football Manager stats to Counter Attack stats (and is currently just my opinion on which should be considered for which). Fun fact: skill. 
