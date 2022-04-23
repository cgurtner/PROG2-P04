# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:08:06 2022

@author: Seitz
"""
from FileRetriever import FileRetriever
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/20964153/master'
file = FileRetriever()
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


class main_application():
    def __init__(self):
        self.canton_df = pd.DataFrame(CANTON_CODES, columns= ['code','canton'])
        self.read_data()
        self.ch_employed_by_year()
        self.ch_unemployment_by_year()
        self.avg_unemployment_per_canton_per_year()
        
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
        self.temp_df = temp_df[temp_df['UNIT_MEA'].str.contains('%', na=False)]
        fig, ax = plt.subplots()
        ax.set(title='Arbeitslose Schweiz',ylabel= 'Anahl Arbeitslose in % der Erwerbspersonen', xlabel= 'Jahr')
        ax.plot(list_of_years, self.temp_df['OBS_VALUE'])
    
    #def unemployment_per_canton(self):
        
        
a = main_application()
aa = pd.read_csv('data/erwerbsquote_nach_kanton.csv', sep = ';')

