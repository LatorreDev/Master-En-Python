#!/usr/bin/python3
# Ejercicio 3 de fundamentos de python

"""
Crear un script que muestre los cuadrados (Un numero multiplcado por si mismo)
de los primeros 60 numeros naturales. Resolverlo con for y while
"""

contador = 1

# Con for

for contador in range (61):
    print(contador * contador)
#    print (f"debug, interacion numero {contador}")

# Con while

contador = 1 # Se reinicia el contador

while contador <= 60:
    print(contador * contador)
    contador += 1