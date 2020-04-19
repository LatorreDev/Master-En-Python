#!/usr/bin/python3
# Parametros opcionales en python

"""
Se le puede pasar o no un paramentro a una funcion
"""

def getEmpleado(nombre, dni = None): # Se le asigna un valor por defecto al parametro que entra
    print("Empleado")
    print(f"Nombre: {nombre}")

    if dni != None: # Condicional para evaluar si mostrar o no el DNI
        print(f"DNI: {dni}")

getEmpleado("Sarah")
print("\n")
getEmpleado("David", 123456789)