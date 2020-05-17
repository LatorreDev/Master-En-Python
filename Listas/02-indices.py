#!/usr/bin/python3
# Indices en python

# Lista

peliculas = ["Batman","Spiderman","El Senor de los anillos", "Megamente","Jumanji"]

# indice

print(peliculas[1])
print(peliculas[-1]) #Con negativo recorremos la lista de atras a adelante
print(peliculas[1:3]) # Un rango de inicio y uno de finalizacion
print(peliculas[2:]) # Todos los elementos a partir de un indice determinado

# Modificacion de indice
peliculas[2] = "El Hobbit"
# Nueva lista con indice 2 modificado
print(peliculas)


