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

class main_application():
    def __init__(self):
        self.read_data()
        self.ch_employed_by_year()
        self.ch_unemployment_by_year()
        
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
        
        
a = main_application()
aa = pd.read_csv('data/erwerbsquote_nach_kanton.csv', sep = ';')

