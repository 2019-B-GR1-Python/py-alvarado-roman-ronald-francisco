# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import Instrumento
def main():
    print("\t Bienvenidos a Casa Musical Parra\t")
    mostrar_presentacion_general()
    print("Aqui tiene varias opciones para la adquisiscion de su instrumento favorito:")
    while True:
        print("Seleccione las siguientes opciones:")
        print("1. Buscar")
        print("2. Crear")
        print("3. Eliminar")
        print("4. Editar")
        opcion = input("Ingrese la opcion: ")
        if (opcion.isnumeric()):
            option = int(opcion)
            if(option == 0):
                break
        try:
            switch(option)()
        except TypeError:
            print(f'Option {option}')    

def switch(valor):
    try:
        instrumento = {
            0: None,
            1: buscar,
            2: crear,
            3: eliminar,
            4: actualizar
        }
        return instrumento[valor]
    except KeyError:
        print("No existe esa opcion")
        
def buscar():
    print("\tBúsqueda de Instrumento\t")
    codigo = input("Ingrese el codigo del instrumento a buscar: ")
    instrumento_a_buscar=Instrumento.obtener_instrumento_por_codigo(codigo)
    if instrumento_a_buscar != None:
        print('Codigo', 'Instrumento', 'Color')
        print(f"{instrumento_a_buscar['codigo']}, {instrumento_a_buscar['instrumento']}, {instrumento_a_buscar['color']}")
    else:
        print(f"El instrumento con código {codigo} no se encuentra registrado en la base de datos")

def mostrar_presentacion_general():
    lista = Instrumento.obtener_lista_tipos_instrumentos()
    for instrumento in lista:
        inst = instrumento.get('codigoT')
        i= int(inst)
        instrumento_a_buscar=Instrumento.obtener_instrumento_por_codigo_tipo(inst)
        print(instrumento_a_buscar)
        instrumentos = int(instrumento_a_buscar.get('codigoT'))
        if  i == instrumentos:
            print('Codigo',' Tipo de instrumento',' Instrumento', '  Color')
            print(f"{instrumento_a_buscar['codigo']}, {instrumento['instrumento']}, {instrumento_a_buscar['instrumento']}, {instrumento_a_buscar['color']}")
    
    
def eliminar():
    print("\tEliminar Instrumento\t")
    code = input("Ingrese el codigo de instrumento a eliminar: ")
    lista = Instrumento.obtener_lista_instrumentos()
    instrumento_a_eliminar = Instrumento.obtener_instrumento_por_codigo(code)
    if instrumento_a_eliminar != None:
        lista.remove(instrumento_a_eliminar)
    Instrumento.transformar_lista_a_cadenatexto(lista)
    print(f"Se ha eliminado")
    
def crear():
    Instrumento.crear_instrumento()
    
def actualizar():
    print("\tActualización de los datos del instrumento\t")
    codigo = input("Ingrese el codigo del instrumento a actualizar: ")
    lista = Instrumento.obtener_instrumento_por_codigo(codigo)
    if lista != None:
        print('Codigo', 'Instrumento', 'Color')
        print(f"{lista['codigo']}, {lista['instrumento']}, {lista['color']}")
        print("\nSleccione una de las siguientes opciones:")
        print("0. Actualizar nombre del instrumento: ")
        print("1. Actualizar color del instrumento: ")
        read = input("Ingrese una opción: ")
        if (read.isnumeric()):
            opcion = int(read)
        try:
            def opciones(value):
                try:
                    return {
                        0: 'instrumento',
                        1: 'color',
                    }[value]
                except KeyError:
                    print("Opción no definida")
    
            obtener_llave = opciones(opcion)
            dato = input('Ingrese el nuevo dato: ')
            dato_a_actualizar = {
                    obtener_llave: dato
            }
            Instrumento.actualizar_instrumentos(lista, dato_a_actualizar)
        except Exception as error:
            print(f'Error {error}')
    else:
        print(f"No existe el instrumento")

main()