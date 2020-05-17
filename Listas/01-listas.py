#!/usr/bin/python3
# Listas en Python

"""
Listas(Arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre

Para acceder a esos valores podemos usar un indice numerico
"""

pelicula = "Batman"
# Las listas se definen con llaves cuadradas
peliculas = ["Batman","spiderman","El senor de los anillos"]
cantantes = list(("Freddy Mercury", "Karen Carpenter, Tarja Turunen"))
"""
Los elementos dentro de los parentesis internos son una Tupla, con el metodo list y parentesis externos
la convertimos a una lista
"""

years = list(range(2020, 2050)) # creacion de lista con un rango numerico

variada = ["palabrita", 2, True, 4.4]
print(pelicula)
print(type(peliculas))
print(cantantes)
print(years)
print(type(variada))
print(variada)
