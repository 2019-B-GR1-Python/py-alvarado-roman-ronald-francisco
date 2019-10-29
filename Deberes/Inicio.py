# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
def contenido():
    print("\t Bienvenidos \t")
    print("Seleccione las siguientes opciones:")
    print("1. Buscar")
    print("2. Crear")
    print("3. Eliminar")
    print("4. Editar")
    opcion = input("Ingrese la opcion: ")
    def opcion_seleccionada(opcion1):
        opciones = {
                '1':"hola",
                '2':"ss",
                '3':"s",
                '4':"s",
                    }
        return opciones[opcion1]
    return opcion_seleccionada(opcion)
    

    
def obtener_datos():
    try:
        path = "./intrumentos.txt"
        archivo_abierto = open(path)
        mensaje = archivo_abierto.read()
        print(mensaje)
    except Exception as error:
        print(f"Error: {error}")
        
contenido()
