# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:55:53 2019

@author: ro199
"""
import numpy as np
import pandas as pd
import os
import sqlite3
import xlsxwriter

path = "./data/art-completo"
dfs = pd.read_pickle(path)
df = dfs.iloc[49980:50019,:].copy()

# Tipos archivos
# JSON
# EXCEL
# SQL

### EXCEL  ##

path_guardado = './mi_df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index = False)

columnas = ['artist','title','year']
df.to_excel(path_guardado, columns = columnas)

### Multiples Hojas de Trabajo ###

path_multiple = './mi_df_multiples.xlsx'
writer = pd.ExcelWriter(path_multiple, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda', index = False)
df.to_excel(writer, sheet_name = 'Tercera', columns = columnas)
writer.save()

numero_artistas = df['artist'].value_counts()
path_colores = './data/mi_df_colores.xlsx'
writer = pd.ExcelWriter(path_colores, engine = 'xlsxwriter')

numero_artistas.to_excel(writer, sheet_name = 'Artistas')

hojas_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B4'.format(len(numero_artistas.index) + 1)

formato_artistas = {
        "type": "",
        "min_vslue":"10",
        "min_type":"percentile",
        "max_value": "99",
        "max_type":"percentile"}

hojas_artistas.conditional_format(rango_celdas,formato_artistas)

writer.save()

workbook = xlsxwriter.Workbook('./data/chart_line.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = numero_artistas.values
worksheet.write_column('A1', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

# Insert the chart into the worksheet.
worksheet.insert_chart('C1', chart)

workbook.close()































