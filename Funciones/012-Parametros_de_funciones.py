#!/usr/bin/python3
# Parametros de funciones

"""
Un parametro es un dato que se le ingresa a una funcion,
 este existe fuera de ella
"""

# Variable fuera de la funcion
nombre = input("Cual es tu nombre?: ")

# Funcion
def mostrarNombre(nombre): # El parametro que se le pasa es nombre
    print(f"Tu nombre es {nombre}")

mostrarNombre(nombre) # Se invoca la funcion con el parametro que se le quiere pasar