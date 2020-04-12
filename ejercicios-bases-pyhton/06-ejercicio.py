#!/usr/bin/python3
# Ejercicio 6 de fundamentos de python

"""
Script para mostrar todas las tablas de multiplicar del 1 al 10, 
mostrando el titulo de la tabla y luego las multiplicaciones
"""

for contador in range(1,11):
    print (f"Tabla de multiplicar del {contador}")
    print("\n")
    contador2 = 1
    for contador2 in range(contador2, 11):
        print (f"{contador} * {contador2} = {contador * contador2}")
    print("\n")