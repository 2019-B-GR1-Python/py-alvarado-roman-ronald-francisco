# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:38:17 2019

@author: ro199
"""

def obtener_lista_instrumentos():
    archivo = obtener_datos()
    instrumentos = []
    for cadena in archivo:
        instrumentos.append(tokenizar_cadena(cadena))    
    return instrumentos

def obtener_lista_tipos_instrumentos():
    archivo = obtener_tipos_instrumentos()
    tipos_instrumentos = []
    for cadena in archivo:
        tipos_instrumentos.append(tokenizar_cadena_tipo(cadena))    
    return tipos_instrumentos

def tokenizar_cadena_tipo(cadena):
        token = (cadena + "").replace("\n", "").split(',')
        instrumento = {
            'codigo': token[0],
            'instrumento': token[1],
        }
        return instrumento
    
    
def tokenizar_cadena(cadena):
        token = (cadena + "").replace("\n", "").split(',')
        instrumento = {
            'codigo': token[0],
            'codigoT': token[1],
            'instrumento': token[2],
            'color': token[3],
        }
        return instrumento
    
def obtener_datos():
    try:
        path = "./instrumentos.txt"
        lineas = []
        archivo_abierto = open(path)
        mensaje = archivo_abierto.readlines()
        for linea in mensaje:
            lineas.append(linea)
        archivo_abierto.close()
        return lineas
    except Exception as error:
        print(f"Error: {error}")

def obtener_tipos_instrumentos():
    try:
        path = "./tiposInstrumentos.txt"
        lineas = []
        archivo_abierto = open(path)
        mensaje = archivo_abierto.readlines()
        for linea in mensaje:
            lineas.append(linea)
        archivo_abierto.close()
        return lineas
    except Exception as error:
        print(f"Error: {error}")
    
def agregar_datos(path, opcion, *lineas):
    try:
        archivo = open(path, opcion)
        for linea in lineas:
            archivo.write(linea + '\n')
        archivo.close()
        print('Guardado')
    except Exception as error:
        print(f"Error {error}")
    
    
def obtener_instrumento_por_codigo(codigo):
    lista = obtener_lista_instrumentos()
    for instrumento in lista:
        if instrumento.get('codigo') == codigo:
            break
    else:
        instrumento = None
    return instrumento

def obtener_instrumento_por_codigo_tipo(codigo):
    lista = obtener_lista_instrumentos()
    for instrumento in lista:
        if instrumento.get('codigoT') == codigo:
            break
    else:
        instrumento = None
    return instrumento


def crear_instrumento():
    print("Formulario de la creacion del instrumento:")
    codigo = input("Ingrese el codigo: ")
    print("Tipos de instrumentos: ")
    print("1. Viento")
    print("2. Cuerda")
    print("3. Percusion")
    print("4. Instrumentos electricos")
    tipo = input("Ingrese el codigo de tipo de instrumento")
    instrumento = input("Ingrese el nombre del instrumento: ")
    color = input("Ingrese el color: ")
    lista = codigo+","+tipo+","+instrumento+","+color
    agregar_datos('./instrumentos.txt', 'a', lista)
    
def actualizar_instrumentos(instrumento, nuevo_dato):
    lista = obtener_lista_instrumentos()
    primer_termino = lista.index(instrumento)
    instrumento.update(nuevo_dato)
    lista[primer_termino] = instrumento
    print("Actualizando mascota")
    
def transformar_lista_a_cadenatexto(lista):
    cadena = []
    for instrumento in lista:
        linea = f"{lista['codigo']},{lista['instrumento']},{lista['color']}"
        cadena.append(linea)
    agregar_datos('./instrumentos.txt', 'w', *cadena)
    