# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:33:31 2019

@author: ro199
"""

import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
fila = []
image_lista = []
image_l = []
image_array = np.array([])
image_array1 = np.array([])
aux = []
aux1 = []

rana_pepe = mpimg.imread('pepe.jpg')
plt.imshow(rana_pepe)

def dividir_imagen(imagen, n):
    global fila
    array_n_dimensiones = np.vsplit(imagen,n)
    for i in range(0,n):
        fila.append(np.hsplit(array_n_dimensiones[i],n))
    return fila

def mezclar_elementos_lista(lista,n):
    global image_array, image_lista, image_array1
    matriz = [[0 for x in range(n)] for i in range(n)]
    np.random.shuffle(lista)
    for i in range(0,n):
        np.random.shuffle(lista[i])
        image_array = np.hstack(lista[i])
       # plt.imshow(image_array)
       # plt.show()
        
        image_lista.append(image_array)
        image_array1 = np.vstack(image_lista)
        
        plt.imshow(image_lista[i])
        plt.show()
        
        
        for j in range(0,n):
            matriz[i][j] = np.array(image_lista[i][j])      
    return image_array1, matriz
        
def graficar(imagen_Original, imagen_Mezclada):
    print("Imagen Original")
    plt.imshow(imagen_Original)
    plt.show()
    print("Imagen Mezclada")
    plt.imshow(imagen_Mezclada)
    print(imagen_Mezclada[0].shape)
    plt.show()

def graficar_mov(imagen_mov,n):
    global image_l
    for i in range(0,n):
        image_ar = np.hstack(imagen_mov[i],axis=0)
        image_l.append(image_ar)
        image_ar1 = np.vstack(image_lista, axis=1)
        #unir_piezas_matriz.append(np.concatenate(imagen_mov[i],axis=0))
    #unir_piezas_matriz1 = np.concatenate(unir_piezas_matriz,axis=1)
    print("Entre al graficar mov")
    plt.imshow(image_ar1)
    plt.show()

def movimiento(matriz_mezclada,muestra_matriz, mov_ini, mov_fin,h,w):
    i, j = np.where(muestra_matriz == int(mov_ini))
    k, l = np.where(muestra_matriz == int(mov_fin))
    i = int(i)
    j = int(j)
    k = int(k)
    l = int(l)
    aux = matriz_mezclada[i][j]
    matriz_mezclada[i][j] = matriz_mezclada[k][l]
    matriz_mezclada[k][l] = aux
    print("Estoy en el movimiento")
    plt.imshow(matriz_mezclada[i])
    plt.show()
    plt.imshow(matriz_mezclada[k][l])
    plt.show()
    return matriz_mezclada
    
    
def main(pepe):
    ss = dividir_imagen(pepe, 4)
    ss1, mat = mezclar_elementos_lista(ss,4)
    arr = np.array(ss1)
    h, w, rgb= arr.shape
    print(arr[0][0].shape)
    print(f"h: {h}, w: {w}")
    graficar(pepe,arr)
    muestra_matriz = np.arange(16).reshape(4,4)
    print(muestra_matriz)
    mov_ini = input("ingrese la posicion de entrada: ")
    mov_fin = input("ingrese la posicion de la salida: ")
    ss2 = movimiento(mat,muestra_matriz,mov_ini,mov_fin,h,w)
    graficar_mov(ss2,4)

main(rana_pepe)