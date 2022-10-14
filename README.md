# counterattack
### _Now you can generate your own Counter Attack player cards for real-life players!_

<img src="https://github.com/cbrown4858/counterattack/blob/main/images/logos_big.png" width=100% height=100%>
  
This python package creates a .xlsx file with Counter Attack player card stats for any real-life footballers from their Football Manager attributes. This .xlsx file is intended to be used with the **Counter Attack Custom Card Generator** created by [Konrad Frac](https://github.com/kkoripl). The Football Manager data is scraped from [FMInside](https://fminside.net/).
  
<img src="https://github.com/cbrown4858/counterattack/blob/main/images/bumper_5.png" width=100% height=100%>  

## User Guide
Download the Windows or Mac User Guide [here](https://github.com/cbrown4858/counterattack/guides/)

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
