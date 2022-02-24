"""A module for the Club class.

classes:
    Club: a class containing an array of Player objects along with a football club's information scraped from a Football Manager data website.

        methods, public:
            _init_: Initializes the class with a URL and the option to export the class to a .xlsx file immediately after initialization.
            fetch_player_names: Returns a list of names for each Player in the Club (i.e. self.players).
            fetch_player_surnames: Returns a list of surnames for each Player in the Club (i.e. self.players).
            send_to_df: Returns a pandas DataFrame containing the players in the Club and their Counter Attack stats.
            save_to_xlsx: Exports a pandas DataFrame of Players in the Club to an .xlsx file.
        
        exceptions:
            This module doesn't currently use any try-except blocks.
"""

from counterattack.obj.player import Player
from counterattack.fminside import fminside
import pandas as pd
import xlsxwriter
import os
from tqdm import tqdm


class Club:

    def __init__(
        self, 
        url,
        export_dir=None,
        export_squad_size=25):
        self.url = url
        self.name, self.fm_version, self.players_urls = fminside.fetch_club_fm_data(self.url)
        self.players = self._create_players()
        self.top_players = self._extract_top_players()
        self.value_ca = sum([player.value_ca for player in self.players])        
        self._configure_display_names_for_squad()
        if isinstance(export_dir, str):
            if export_squad_size == 00:
                self.save_to_xlsx(save_dir=export_dir, squad_size=len(self.players))
            else:
                self.save_to_xlsx(save_dir=export_dir, squad_size=export_squad_size)

    def __repr__(self) -> str:
        return self.name

    def _create_players(self):
        BASE_URL = 'https://fminside.net'
        return [Player(BASE_URL+i) for i in tqdm(self.players_urls, desc=f'{self.name}')]

    def _extract_top_players(self, limit=25):
        player_values = {player.name:player.value_ca for player in self.players}
        sorted_player_values = dict(sorted(player_values.items(), key=lambda x:x[1])) # sort dictionary in ascending order based on player.value_ca
        tmp = [key for key in reversed(sorted_player_values.keys())] # create a list of player.name in descending order based on player.value_ca
        tmp = tmp[:limit]
        return [player for player in self.players if player.name in tmp] # create list of player object if player.name in tmp list

    def _configure_display_names_for_squad(self, surname_only=True, cutoff=15):
        squad_surnames = self.fetch_player_surnames()
        counts = {surname:surname.count(surname) for surname in squad_surnames}
        for player in self.players:
            if counts[player.surname]>1 and surname_only==True:
                player.set_display_name(f'{player.first_name[:1]}. {player.surname}')
            elif counts[player.surname]>1 and surname_only==False:
                if len(player.name) > cutoff:
                    if len(player.first_name) == '':
                        player.set_display_name(input(f'{player.name} has no first name and shares their surname with a teammate.\nHow would you like their name to appear on their card? '))
                    else:
                        player.set_display_name(f'{player.first_name[:1]}. {player.surname}')
                else:
                    player.set_display_name(player.name)
            elif counts[player.surname]==1 and surname_only==True:
                player.set_display_name(f'{player.surname}')
            elif counts[player.surname]==1 and surname_only==False:
                if len(player.name) > cutoff:
                    player.set_display_name(player.surname)
                else:
                    player.set_display_name(player.name)
            else:
                print("------>SOMETHING WENT WRONG<------")

    def fetch_player_names(self):
        return [player.name for player in self.players]

    def fetch_player_surnames(self):
        return [player.surname for player in self.players]

    def send_to_df(self, squad_size=25):
        if squad_size == len(self.players):
            return pd.DataFrame([player.get_data_for_ca_card() for player in self.players])
        elif squad_size > len(self.players):
            print(f'Entered squad_size ({squad_size}) is greater than the full squad size ({len(self.players)}). Proceeding with the full squad size.')
            return pd.DataFrame([player.get_data_for_ca_card() for player in self.players])
        elif squad_size < len(self.players):
            return pd.DataFrame([player.get_data_for_ca_card() for player in self._get_top_players(squad_size)])

    def save_to_xlsx(self, save_dir=os.getcwd(), squad_size=25):
        save_path = os.path.join(save_dir, f'{self.name.replace(" ", "")}_{self.fm_version}.xlsx')
        df = self.send_ca_to_df(squad_size)
        column_list = df.columns
        writer = pd.ExcelWriter(save_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
        worksheet = writer.sheets['Sheet1']
        for idx, val in enumerate(column_list): # adds column headers back into sheet without the formatting from pd.to_excel()
            worksheet.write(0, idx, val)
        writer.save()
        print(f'--> Exported to {save_path}')