# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:58:05 2019

@author: ro199
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_c = pd.Series(np_numeros)
serie_d = pd.Series([True,
                     False,
                     12,
                     12.12,
                     "Adrian",
                     None,
                     (),
                     [],
                     {"nombre":"Ronald"}])

serie_d[3]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]

serie_ciudad = pd.Series(lista_ciudades, index = ["A","C","L","Q"])

serie_ciudad["Q"]
serie_ciudad[3]

 

Valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito": 8000,
        "Loja": 3000} 

serie_valor_ciudad = pd.Series(Valores_ciudad)

ciudades_menores_5000 = serie_valor_ciudad < 5000

serie_5 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

print("Lima" in serie_valor_ciudad)

print("Loja" in serie_valor_ciudad)

rsquare = np.square(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Montanita": 300,
        "Guayaquil":10000,
        "Quito":2000})

ciudades_dos = pd.Series({
        "Loja":300,
        "Guayaquil":10000})

ciudades_uno["Loja"] = 0

print(ciudades_uno+ciudades_dos)

ciu_add = ciudades_uno.add(ciudades_dos)

ciu_concatenadas = pd.concat([ciudades_uno,ciudades_dos])

ciu_concatenadas = pd.concat([ciudades_uno,ciudades_dos], verify_integrity = True)

ciu_append = ciudades_uno.append(ciudades_dos, verify_integrity = True)

ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)

# Estadistica
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

# Tomar los dos primeros
ciudades_uno.head(2) 

#Tomar los dos ultimos
ciudades_uno.tail(2)

#Ordenar los indices
#Cuando uno ordena va de mayor a menor
ciudades_uno.sort_values(ascending = False).head(2)










