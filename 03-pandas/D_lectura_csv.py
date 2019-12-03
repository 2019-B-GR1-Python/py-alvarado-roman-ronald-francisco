# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:21:06 2019

@author: ro199
"""

import pandas as pd
import os

# 1) JSON CSV HTML XML ...
# 2) Binary files -> (!#mf-.1234'120)
# 3) Relational Databases

path = open('C:\\Users\\ro19\\Documents\\GitHub\\py-alvarado-roman-ronald-francisco\\03-pandas\\data\\art.csv')
df = pd.read_csv(path, nrows = 10)

columnas = ['id','artist','title','medium','year','acquisitionYear','height']

df2 = pd.read_csv(path,nrows = 10, usecols = columnas)

df3 = pd.read_csv(path,nrows = 10, usecols = columnas, index_col = 'id')

pathGuarda = "C:/Users/ro19/Documents/GitHub/py-alvarado-roman-ronald-francisco/03-pandas/dataartwork_data.csv"

df.to_pickle(pathGuarda)

path_Guardado_bin = ''
df4.to_pickle(path_Guardado_bin)

df5 = pd.read_pickle(path_Guardado)

