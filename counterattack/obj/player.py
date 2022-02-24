"""A module for the Player class.

classes:
    Player: a class containing a real-life player's Counter Attack stats abstracted from their Football Manager stats.

        methods, public:
            _init_: Initializes the class with a URL and the option to export the class to a .xlsx file immediately after initialization.
            fetch_data_for_ca_card: Returns a dictionary of all Counter Attack card information for the Player.
            update_display_name: Sets the name shown on a Counter Attack card.
            send_stats_ca_to_df: Returns a pandas DataFrame containing the information from self.fetch_data_for_ca_card().
            save_to_xlsx: Exports a pandas DataFrame of the information from self.fetch_data_for_ca_card().
        
        exceptions:
            This module doesn't currently use any try-except blocks.

        notes:
            In _calculate_stats_ca() there is a constant variable dictionary FM_TO_CA_DICT that is used to calculate the Counter Attack stats.
            This dictionary can be adjusted to change which Football Manager stats are used to determine Counter Attack stats.
"""

from counterattack.fminside import fminside
import pandas as pd
import os


class Player:
    
    def __init__(
        self, 
        url,
        export_dir=None):
        self.url = url
        self.name, self.nationality, self.stats_fm, self.fm_version = fminside.fetch_player_fm_data(self.url)
        self.first_name = ''
        self.surname = ''
        self.display_name = self.name
        self.position = self._initialize_ca_position()
        self.stats_ca = self._calculate_stats_ca()
        self.value_ca = sum(filter(lambda i: isinstance(i, int), self.stats_ca.values())) # sums only the integers in a list
        self._configure_personal_names()
        if isinstance(export_dir, str):
            self.save_to_xlsx(save_dir=export_dir)
            
    def __repr__(self):
        return self.name

    def _calculate_stats_ca(self):
        FM_TO_CA_DICT = {
            'Pace' : ['acceleration', 'pace'],
            'Dribbling' : ['dribbling', 'technique'],
            'Heading' : ['heading', 'jumping-reach'],
            'High Pass' : ['corners', 'crossing', 'passing', 'kicking', 'technique'],
            'Resilience' : ['bravery', 'natural-fitness'],
            'Shooting' : ['finishing', 'technique'],
            'Tackling' : ['tackling'],
            'Saving' : ['one-on-ones', 'reflexes'],
            'Aerial Ability' : ['aerial-reach'],
            'Handling' : ['handling']
        }
        CONV_RATE = 3 /10
        skills = {}
        for k, v in FM_TO_CA_DICT.items():
            skill = k
            running_total = 0
            running_count = 0
            for i in v:
                if i in self.stats_fm:
                    running_total += self.stats_fm[i]
                    running_count += 1
                else:
                    pass
            if running_count == 0:
                value = None
            else:
                average = running_total / running_count
                value = round(average * CONV_RATE)
                # print(self.name)
                # print(f'{skill}: {value} ({average * CONV_RATE})')
            if value == 0:
                value += 1
            skills[skill] = value
        if self.position == 'Goalkeeper':
            skills['Heading'] = None
            skills['Shooting'] = None
            skills['Tackling'] = None
            return skills
        elif self.position == 'Outfielder':
            skills['Saving'] = None
            skills['Aerial Ability'] = None
            skills['Handling'] = None
            return skills

    def _initialize_ca_position(self):
        if 'handling' in self.stats_fm:
            return 'Goalkeeper'
        elif 'heading' in self.stats_fm:
            return 'Outfielder'

    def _configure_personal_names(self):
        if " " in self.name:
            ind = self.name.index(" ")
            self.first_name = self.name[:ind]
            self.surname = self.name[ind+1:]
        else:
            self.surname = self.name
        
    def fetch_data_for_ca_card(self):
        data = {
            'Name': self.display_name,
            'Country': self.nationality,
            'Pace' : self.stats_ca['Pace'],
            'Dribbling' : self.stats_ca['Dribbling'],
            'Heading' : self.stats_ca['Heading'],
            'High Pass' : self.stats_ca['High Pass'],
            'Resilience' : self.stats_ca['Resilience'],
            'Shooting' : self.stats_ca['Shooting'],
            'Tackling' : self.stats_ca['Tackling'],
            'Saving' : self.stats_ca['Saving'],
            'Aerial Ability' : self.stats_ca['Aerial Ability'],
            'Handling' : self.stats_ca['Handling']
        }
        return data
        
    def update_display_name(self, display_name):
        self.display_name = display_name

    def send_stats_ca_to_df(self):
        self.update_display_name(self.surname)
        return pd.DataFrame(self.fetch_data_for_ca_card(), index=[0])

    def save_to_xlsx(self, save_dir=os.getcwd()):
        save_path = os.path.join(save_dir, f'{self.name.replace(" ", "")}_{self.fm_version}.xlsx')
        df = self.send_stats_ca_to_df()
        column_list = df.columns
        writer = pd.ExcelWriter(save_path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
        worksheet = writer.sheets['Sheet1']
        for idx, val in enumerate(column_list): # adds column headers back into sheet without formatting
            worksheet.write(0, idx, val)
        writer.save()
        print(f'--> Exported to {save_path}')
