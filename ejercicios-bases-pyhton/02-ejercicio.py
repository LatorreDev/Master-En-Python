#!/usr/bin/python3
# Ejercicio 2 de fundamentos de python

"""
Crear un script que muestre en pantalla 
todos los numeros pares de 1 al 120
"""

contador = 1

while contador <=120:
    if (contador % 2 == 0):
        print(contador)
        contador += 1
    else:
        contador += 1