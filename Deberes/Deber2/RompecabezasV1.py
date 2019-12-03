# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:12:35 2019

@author: ro199
"""

import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_lista = []
image_array = np.array([])
aux = []

rana_pepe = mpimg.imread('pepe.jpg')
plt.imshow(rana_pepe)

def dividir_imagen(imagen, n):

    matriz = [[0 for x in range(n)] for i in range(n)]
    array_n_dimensiones = np.hsplit(imagen,n)
    for i in range(0,n):
        fila = np.vsplit(array_n_dimensiones[i],n)
        for j in range(0,n):
            matriz[i][j] = np.array(fila[j])  
    return matriz

def mezclar_elementos_matriz(matriz_lista,n):
    global image_array, image_list
    np.random.shuffle(matriz_lista)
    for i in range(0,n):
        np.random.shuffle(matriz_lista[i])
        image_lista.append(np.concatenate(matriz_lista[i],axis=0))
    image_array = np.concatenate(image_lista,axis=1)
    matriz = [[0 for x in range(n)] for i in range(n)]
    array_mesclado = np.hsplit(image_array,n)
    for i in range(0,n):
        image_array1 = np.vsplit(array_mesclado[i],n)
        for j in range(0,n):
            matriz[i][j] = np.array(image_array1[j])     
    return matriz
        
def graficar(imagen_Original, imagen_Mezclada):
    print("Imagen Original")
    plt.imshow(imagen_Original)
    plt.show()
    print("Imagen Mezclada")
    graficar_mov(imagen_Mezclada,4)

def graficar_mov(imagen_mov,n):
    unir_piezas_matriz = []
    reconstruir_piezas_matriz = np.array([])
    for i in range(0,n):
        unir_piezas_matriz.append(np.concatenate(imagen_mov[i],axis=0))
    reconstruir_piezas_matriz = np.concatenate(unir_piezas_matriz,axis=1)
    print("Entre al graficar mov")
    plt.imshow(reconstruir_piezas_matriz)
    plt.show()

def movimiento(matriz_mezclada,muestra_matriz, mov_ini, mov_fin):
    i, j = np.where(muestra_matriz == int(mov_ini))
    k, l = np.where(muestra_matriz == int(mov_fin))
    i, j, k, l = int(i), int(j), int(k), int(l) 
    aux = matriz_mezclada[i][j]
    matriz_mezclada[i][j] = matriz_mezclada[k][l]
    matriz_mezclada[k][l] = aux
    print("Estoy en el movimiento")
    return matriz_mezclada
    
def main(pepe):
    ss = dividir_imagen(pepe, 4)
    ss1 = mezclar_elementos_matriz(ss,4)
    graficar(pepe,ss1)
    muestra_matriz = np.arange(16).reshape(4,4)
    while True:
        mov_ini = input("Ingrese la posicion de entrada: ")
        mov_fin = input("Ingrese la posicion de la salida: ")
        ss2 = movimiento(ss1,muestra_matriz,mov_ini,mov_fin)
        graficar_mov(ss2,4)

main(rana_pepe)