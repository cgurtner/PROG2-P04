# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:08:06 2022

@author: Seitz
"""
from FileRetriever import FileRetriever
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/20964153/master'
file = FileRetriever(url, 'erwerbsquote.csv')

class main_application():
    def __init__(self):
        self.read_data(file.filename)
        self.clean_data()
        self.ch_employed_by_year()
        
    def read_data(self,filename):
        self.df = pd.read_csv('data/' + filename, sep = ';')
    
    #We just want the total numbers
    def clean_data(self):
        self.df = self.df[~self.df.UNIT_MEA.str.contains("in")]
        self.df = self.df[~self.df.ERWP.str.contains("1")]
        self.df = self.df[~self.df.POP1564.str.contains("1")]

    def ch_employed_by_year(self):
       list_of_years = self.df['TIME_PERIOD'].to_list()
       list_of_years = list(dict.fromkeys(list_of_years))
       plt.title('Anzahl Arbeitnehmende Schweiz pro Jahr')
       temp_df = self.df[~self.df.GEO.str.contains("0")]
       plt.bar(list_of_years, temp_df['OBS_VALUE'])

a = main_application()
aa = pd.read_csv('data/'+file.filename, sep = ';')

