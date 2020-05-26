#!/usr/bin/env python3

"""
Un SET es un tipo de dato para tener una coleccion de
valores, pero no tiene ni indice ni orden
"""

# Definimos un set

personas = {
"David",
"Angela",
"Francesca",
"Leonardo"
}

print(personas)
print(type(personas))

"""
Metodos comunes

add (anade un elemento al set)
remove (remueve un elemento del set)

"""
personas.add("Camilo")
print(personas)
personas.remove("David")
print(personas)
