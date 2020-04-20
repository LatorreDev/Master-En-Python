#!/usr/bin/python3
# Variables locales y globales en python

"""
Una variable local se define dentro de la funcion y no 
puede usarse fuera de ella

Una variable global puede ser usada por todas las funciones
"""

frase = "ola ke ase" # Variable global

def holaMundo():
    frase = "Hola Mundo!"
    print(f"dentro de la funcion: {frase}")

    global website # se decalara que la variable sea global
    website = "latorredev.com"
    print(f"Dentro: {website}")

holaMundo()
print(f"fuera {website}")