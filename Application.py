# -*- coding: utf-8 -*-
"""
__author__ = "Michael Seitz"
__email__ = "seitzmi1@students.zhaw.ch"
"""

from FileRetriever import FileRetriever
import pandas as pd
import matplotlib.pyplot as plt

class Application():
    CANTON_CODES = [
        ['CH011', 'VD', 'Waadt'],
        ['CH012', 'VS', 'Wallis'],
        ['CH013', 'GE', 'Genf'],
        ['CH021', 'BE', 'Bern'],
        ['CH022', 'FR', 'Freiburg'],
        ['CH023', 'SO', 'Solothurn'],
        ['CH024', 'NE', 'Neuenburg'],
        ['CH025', 'JU', 'Jura'],
        ['CH031', 'BS', 'Basel-Stadt'],
        ['CH032', 'BL', 'Basel-Landschaft'],
        ['CH033', 'AG', 'Aargau'],
        ['CH040', 'ZH', 'Zürich'],
        ['CH051', 'GL', 'Glarus'],
        ['CH052', 'SH', 'Schaffhausen'],
        ['CH053', 'AR', 'Appenzell Ausserrhoden'],
        ['CH054', 'AI', 'Appenzell Innerrhoden'],
        ['CH055', 'SG', 'St. Gallen'],
        ['CH056', 'GR', 'Graubünden'],
        ['CH057', 'TG', 'Thurgau'],
        ['CH061', 'LU', 'Luzern'],
        ['CH062', 'UR', 'Uri'],
        ['CH063', 'SZ', 'Schwyz'],
        ['CH064', 'OW', 'Obwalden'],
        ['CH065', 'NW', 'Nidwalden'],
        ['CH066', 'ZG', 'Zug'],
        ['CH070', 'TI', 'Tessin']
    ]
    def __init__(self):
        self.canton_df = pd.DataFrame(Application.CANTON_CODES, columns=['code', 'abbrev', 'canton'])
        self.read_data()
        
    def read_data(self):
        self.data = pd.read_csv(FileRetriever.get_file_path(), sep = ';')

    def ch_employed_by_year(self):
        list_of_years = self.data['TIME_PERIOD'].to_list()
        list_of_years = list(dict.fromkeys(list_of_years))
        fig, ax = plt.subplots()
        temp_df = self.data[~self.data.UNIT_MEA.str.contains("in")]
        temp_df = temp_df[~temp_df.GEO.str.contains("0")]
        temp_df = temp_df[~temp_df.UNIT_MEA.str.contains("in")]
        temp_df = temp_df[~temp_df.ERWP.str.contains("1")]
        temp_df = temp_df[~temp_df.POP1564.str.contains("1")]
        ax.set(title = 'Arbeitnehmende Schweiz', ylabel='Anzahl in Mio', xlabel= 'Jahr')
        ax.plot(list_of_years, temp_df['OBS_VALUE'])
        plt.show()
       
    def ch_unemployment_by_year(self):
        list_of_years = self.data['TIME_PERIOD'].to_list()
        list_of_years = list(dict.fromkeys(list_of_years))
        temp_df = self.data
        temp_df = temp_df[~temp_df.ERWL.str.contains("0")]
        temp_df = temp_df[~temp_df.ERWL.str.contains('Total')]
        temp_df = temp_df[~temp_df.GEO.str.contains("0")]
        temp_df = temp_df[temp_df['UNIT_MEA'].str.contains('%', na=False)]
        fig, ax = plt.subplots()
        ax.set(title='Arbeitslose Schweiz',ylabel= 'Anahl Arbeitslose in % der Erwerbspersonen', xlabel= 'Jahr')
        ax.plot(list_of_years, temp_df['OBS_VALUE'])
        plt.show()
    
    def avg_unemployment_per_canton(self):
        temp_df = self.data
        temp_df = temp_df[~temp_df.ERWP.str.contains("1")]
        temp_df = temp_df[~temp_df.ERWL.str.contains('Total')]
        temp_df = temp_df[~temp_df.ERWL.str.contains("0")]
        temp_df = temp_df.dropna()
        temp_df = temp_df[temp_df['UNIT_MEA'].str.contains('%', na=False)]
        temp_df = temp_df[temp_df['GEO'].str.contains('0', na=False)]
        temp_df = temp_df.groupby(['GEO'], sort=False)['OBS_VALUE'].mean()
        temp_df = temp_df.to_frame().reset_index()
        temp_df = temp_df.rename(columns = {'GEO':'code'})
        temp_df = pd.merge(temp_df, self.canton_df, on = 'code', how= 'outer')
        fig, ax = plt.subplots(figsize=(15,10))
        ax.set(title = 'Druchschnittsarbeitslosigkeit von 2010-2020 pro Kanton', ylabel= 'Arbeitslose in %', xlabel= 'Kanton')
        ax.bar(temp_df['abbrev'], temp_df['OBS_VALUE'])
        plt.show()

if __name__ == '__main__':
    fr = FileRetriever()

    app = Application()
    app.ch_employed_by_year()
    app.ch_unemployment_by_year()
    app.avg_unemployment_per_canton()

