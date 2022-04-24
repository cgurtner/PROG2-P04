# -*- coding: utf-8 -*-
"""
__author__ = "Michael Seitz"
__email__ = "seitzmi1@students.zhaw.ch"
"""

from FileRetriever import FileRetriever
import pandas as pd
import matplotlib.pyplot as plt

class main_application():
    CANTON_CODES = [
['CH011','Waadt'],
['CH012','Wallis'],
['CH013','Genf'],
['CH021','Bern'],
['CH022','Freiburg'],
['CH023','Solothurn'],
['CH024','Neuenburg'],
['CH025','Jura'],
['CH031','Basel-Stadt'],
['CH032','Basel-Landschaft'],
['CH033','Aargau'],
['CH040','Zürich'],
['CH051','Glarus'],
['CH052','Schaffhausen'],
['CH053','Appenzell Ausserrhoden'],
['CH054','Appenzell Innerrhoden'],
['CH055','St. Gallen'],
['CH056','Graubünden'],
['CH057','Thurgau'],
['CH061','Luzern'],
['CH062','Uri'],
['CH063','Schwyz'],
['CH064','Obwalden'],
['CH065','Nidwalden'],
['CH066','Zug'],
['CH070','Tessin'],]
    def __init__(self):
        self.canton_df = pd.DataFrame(main_application.CANTON_CODES, columns= ['code','canton'])
        self.read_data()
        
    def read_data(self):
        self.data = pd.read_csv('data/erwerbsquote_nach_kanton.csv', sep = ';')

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
        fig, ax = plt.subplots(figsize=(20,15))
        ax.set(title = 'Druchschnittsarbeitslosigkeit von 2010-2020 pro Kanton', ylabel= 'Arbeitslose in %', xlabel= 'Kanton')
        ax.bar(temp_df['code'], temp_df['OBS_VALUE'])
        print('Canton-code legend:')
        print(temp_df[['code', 'canton']])
        

if __name__ == '__main__':
    FileRetriever()
    a = main_application()
    a.ch_employed_by_year()
    a.ch_unemployment_by_year()
    a.avg_unemployment_per_canton()

